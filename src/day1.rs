use aoc_parse::{parser, prelude::*};
use aoc_runner_derive::*;

#[aoc_generator(day1)]
fn parse_input(text: &str) -> Vec<Vec<u8>> {
    let p = parser!(lines(
        value:line(string(any_char+)) => value.as_bytes().to_vec()
    ));
    p.parse(text).unwrap()
}

#[aoc(day1, part1)]
pub fn part1(input: &[Vec<u8>]) -> usize {
    input
        .iter()
        .map(|line| {
            let mut digits = (0..line.len()).filter_map(|i| match line[i] {
                b'0'..=b'9' => Some((line[i] - b'0') as usize),
                _ => None,
            });
            let first = digits.next().unwrap();
            let last = digits.last().unwrap_or(first);
            first * 10 + last
        })
        .collect::<Vec<_>>()
        .iter()
        .sum()
}

#[aoc(day1, part2)]
pub fn part2(input: &[Vec<u8>]) -> usize {
    const DIGIT_WORDS: &[&[u8]] = &[
        b"one", b"two", b"three", b"four", b"five", b"six", b"seven", b"eight", b"nine",
    ];
    input
        .iter()
        .map(|line| {
            let mut digits = (0..line.len()).filter_map(|i| match line[i] {
                b'0'..=b'9' => Some((line[i] - b'0') as usize),
                _ => DIGIT_WORDS
                    .iter()
                    .enumerate()
                    .find_map(|(idx, word)| line[i..].starts_with(word).then_some(idx + 1)),
            });
            let first = digits.next().unwrap();
            let last = digits.last().unwrap_or(first);
            first * 10 + last
        })
        .collect::<Vec<_>>()
        .iter()
        .sum()
}

#[cfg(test)]
mod tests {
    // use super::{part1, part2};
}
