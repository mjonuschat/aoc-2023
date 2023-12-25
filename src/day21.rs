use aoc_parse::{parser, prelude::*};
use aoc_runner_derive::*;
use std::collections::{HashSet, VecDeque};

type Input = Vec<Vec<char>>;

#[aoc_generator(day21)]
fn parse_input(text: &str) -> Input {
    let p = parser!(lines(any_char+));
    p.parse(text).unwrap()
}

fn solve(grid: &Input, n: usize) -> usize {
    let width = grid[0].len();
    let height = grid.len();

    let mut queue = VecDeque::from_iter([(width / 2, height / 2, 0)]);
    let mut reachable = HashSet::new();
    let mut visited = HashSet::new();

    while let Some((x, y, steps)) = queue.pop_front() {
        if visited.contains(&(x, y, steps)) {
            continue;
        }

        visited.insert((x, y, steps));
        if steps == n {
            reachable.insert((x, y));
        } else {
            if x > 0 && grid[y][x - 1] != '#' {
                queue.push_back((x - 1, y, steps + 1))
            }

            if x < width - 1 && grid[y][x + 1] != '#' {
                queue.push_back((x + 1, y, steps + 1))
            }
            if y > 0 && grid[y - 1][x] != '#' {
                queue.push_back((x, y - 1, steps + 1))
            }
            if y < height - 1 && grid[y + 1][x] != '#' {
                queue.push_back((x, y + 1, steps + 1))
            }
        }
    }

    reachable.len()
}

#[aoc(day21, part1)]
pub fn part1(input: &Input) -> usize {
    solve(input, 64)
}

#[aoc(day21, part2)]
pub fn part2(input: &Input) -> usize {
    let width = input[0].len();
    let mut grid = Vec::new();
    for _ in 0..5 {
        for line in input {
            grid.push(line.repeat(5));
        }
    }

    // Extrapolate polynomials
    let n = 26501365 / width as isize;
    let m = 26501365 % width;
    let a0 = solve(&grid, m) as isize;
    let a1 = solve(&grid, width + m) as isize;
    let a2 = solve(&grid, 2 * width + m) as isize;

    // Lagrange interpolation
    let a = a0 / 2 - a1 + a2 / 2;
    let b = -3 * a0 / 2 + 2 * a1 - a2 / 2;
    let c = a0;

    (a * n * n + b * n + c) as usize
}

#[cfg(test)]
mod tests {
    // use super::{part1, part2};
}
