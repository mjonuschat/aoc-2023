use aoc_parse::{parser, prelude::*};
use aoc_runner_derive::*;

#[aoc_generator(day13)]
fn parse_input(text: &str) -> Vec<Vec<Vec<u8>>> {
    let p = parser!(sections(lines(l:string(any_char+) => l.as_bytes().to_vec())));
    p.parse(text).unwrap()
}

fn find_col(grid: &Vec<Vec<u8>>, limit: usize) -> Option<usize> {
    (0..grid[0].len() - 1).find(|&c| {
        let incorrect: usize = (0..=c.min(grid[0].len() - c - 2))
            .map(|dc| {
                let a = c - dc;
                let b = c + 1 + dc;
                (0..grid.len())
                    .filter(|&r| grid[r][a] != grid[r][b])
                    .count()
            })
            .sum();
        incorrect == limit
    })
}

fn find_row(grid: &Vec<Vec<u8>>, limit: usize) -> Option<usize> {
    (0..grid.len() - 1).find(|&r| {
        let incorrect: usize = (0..=r.min(grid.len() - r - 2))
            .map(|dr| {
                let a = r - dr;
                let b = r + 1 + dr;
                (0..grid[0].len())
                    .filter(|&c| grid[a][c] != grid[b][c])
                    .count()
            })
            .sum();
        incorrect == limit
    })
}

fn solve(grids: &[Vec<Vec<u8>>], limit: usize) -> usize {
    grids
        .iter()
        .map(|grid| {
            find_row(grid, limit)
                .map(|r| (r + 1) * 100)
                .or_else(|| find_col(grid, limit).map(|c| c + 1))
                .unwrap()
        })
        .sum()
}

#[aoc(day13, part1)]
pub fn part1(input: &[Vec<Vec<u8>>]) -> usize {
    solve(input, 0)
}

#[aoc(day13, part2)]
pub fn part2(input: &[Vec<Vec<u8>>]) -> usize {
    solve(input, 1)
}

#[cfg(test)]
mod tests {
    // use super::{part1, part2};
}
