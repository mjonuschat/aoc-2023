use aoc_parse::{parser, prelude::*};
use aoc_runner_derive::*;
use itertools::Itertools;

#[aoc_generator(day11)]
fn parse_input(text: &str) -> Vec<Vec<u8>> {
    let p = parser!(lines(
        value:line(string(any_char+)) => value.as_bytes().to_vec()
    ));
    p.parse(text).unwrap()
}

fn solve(grid: &[Vec<u8>], mut galaxies: Vec<(usize, usize)>, size: usize) -> usize {
    let rows = grid.len();
    let cols = grid[0].len();
    let er = (0..rows).filter(|r| grid[*r].iter().all(|c| *c == b'.'));
    let ec = (0..cols).filter(|c| (0..rows).all(|r| grid[r][*c] == b'.'));

    for r in er.rev() {
        for g in &mut galaxies {
            if g.0 > r {
                g.0 += size - 1;
            }
        }
    }
    for c in ec.rev() {
        for g in &mut galaxies {
            if g.1 > c {
                g.1 += size - 1;
            }
        }
    }
    galaxies
        .iter()
        .tuple_combinations()
        .map(|((r1, c1), (r2, c2))| r1.abs_diff(*r2) + c1.abs_diff(*c2))
        .sum()
}

fn galaxies(input: &[Vec<u8>]) -> Vec<(usize, usize)> {
    (0..input.len())
        .cartesian_product(0..input[0].len())
        .filter(|&(row, col)| input[row][col] == b'#')
        .collect::<Vec<_>>()
}
#[aoc(day11, part1)]
pub fn part1(input: &[Vec<u8>]) -> usize {
    solve(input, galaxies(input), 2)
}

#[aoc(day11, part2)]
pub fn part2(input: &[Vec<u8>]) -> usize {
    solve(input, galaxies(input), 1000000)
}

#[cfg(test)]
mod tests {
    // use super::{part1, part2};
}
