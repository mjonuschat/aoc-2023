use aoc_parse::{parser, prelude::*};
use aoc_runner_derive::*;
use std::iter::zip;

#[aoc_generator(day6)]
fn parse_input(text: &str) -> Vec<Vec<usize>> {
    let p = parser!(
        lines(alpha+ ":" " "+ data:repeat_sep(usize, " "+) => data)
    );
    p.parse(text).unwrap()
}

fn calc(time: &usize, dist: &usize) -> usize {
    for ct in 0..*time {
        if (time - ct) * ct > *dist {
            return time - 2 * ct + 1;
        }
    }
    0
}

#[aoc(day6, part1)]
pub fn part1(input: &[Vec<usize>]) -> usize {
    let time = &input[0];
    let dist = &input[1];

    zip(time, dist).map(|(t, d)| calc(t, d)).product()
}

#[aoc(day6, part2)]
pub fn part2(input: &[Vec<usize>]) -> usize {
    let time: &usize = &input[0]
        .iter()
        .map(|v| v.to_string())
        .collect::<String>()
        .parse()
        .unwrap();
    let dist: &usize = &input[1]
        .iter()
        .map(|v| v.to_string())
        .collect::<String>()
        .parse()
        .unwrap();

    calc(time, dist)
}

#[cfg(test)]
mod tests {
    // use super::{part1, part2};
}
