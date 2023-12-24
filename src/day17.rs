use aoc_parse::{parser, prelude::*};
use aoc_runner_derive::*;
use std::collections::{BinaryHeap, HashMap};

#[aoc_generator(day17)]
fn parse_input(text: &str) -> Vec<Vec<usize>> {
    let p = parser!(lines(digit+));
    p.parse(text).unwrap()
}

fn find_path(grid: &[Vec<usize>], minstep: isize, maxstep: isize) -> i64 {
    let rows = grid.len();
    let cols = grid[0].len();
    let mut dists = HashMap::new();
    let mut queue = BinaryHeap::new();
    queue.push((0, (0, 0, (0, 0))));

    while let Some((cost, (row, col, dir))) = queue.pop() {
        if (row, col) == (rows - 1, cols - 1) {
            return -cost;
        }

        if dists.get(&(row, col, dir)).is_some_and(|&c| -cost > c) {
            continue;
        }

        for (d_row, d_col) in [(-1, 0), (1, 0), (0, -1), (0, 1)] {
            if dir == (d_row, d_col) || dir == (-d_row, -d_col) {
                continue;
            }
            let mut new_cost = -cost;
            for dist in 1..=maxstep {
                let new_row = (row as isize + d_row * dist) as usize;
                let new_col = (col as isize + d_col * dist) as usize;
                if new_row >= rows || new_col >= cols {
                    continue;
                }
                new_cost += grid[new_row][new_col] as i64;
                if dist < minstep {
                    continue;
                }
                let key = (new_row, new_col, (d_row, d_col));
                if new_cost < *dists.get(&key).unwrap_or(&i64::MAX) {
                    dists.insert(key, new_cost);
                    queue.push((-new_cost, key));
                }
            }
        }
    }
    unreachable!()
}

#[aoc(day17, part1)]
pub fn part1(input: &[Vec<usize>]) -> i64 {
    find_path(input, 1, 3)
}

#[aoc(day17, part2)]
pub fn part2(input: &[Vec<usize>]) -> i64 {
    find_path(input, 4, 10)
}

#[cfg(test)]
mod tests {
    // use super::{part1, part2};
}
