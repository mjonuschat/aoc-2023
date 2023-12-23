use aoc_parse::{parser, prelude::*};
use aoc_runner_derive::*;

#[aoc_generator(day9)]
fn parse_input(text: &str) -> Vec<Vec<isize>> {
    let p = parser!(
        lines(repeat_sep(isize, " "+))
    );
    p.parse(text).unwrap()
}

#[aoc(day9, part1)]
pub fn part1(input: &[Vec<isize>]) -> isize {
    input
        .iter()
        .map(|numbers| {
            numbers
                .iter()
                .enumerate()
                .map(|(i, j)| {
                    num::integer::binomial(numbers.len(), i) as isize
                        * (-1_isize).pow((numbers.len() - 1 - i) as u32)
                        * j
                })
                .sum::<isize>()
        })
        .sum()
}

#[aoc(day9, part2)]
pub fn part2(input: &[Vec<isize>]) -> isize {
    input
        .iter()
        .map(|numbers| {
            numbers
                .iter()
                .enumerate()
                .map(|(i, j)| {
                    num::integer::binomial(numbers.len(), i + 1) as isize
                        * (-1_isize).pow(i as u32)
                        * j
                })
                .sum::<isize>()
        })
        .sum()
}

#[cfg(test)]
mod tests {
    // use super::{part1, part2};
}
