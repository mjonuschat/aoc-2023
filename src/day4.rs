use aoc_parse::{parser, prelude::*};
use aoc_runner_derive::*;
use std::collections::{HashMap, HashSet};
// Card   1: 77 45  9 81 96  5 91  3 66 76 |  7 56 66 49 96 58 54 34 37  5 14 85 45 91  9 22 81 50 88 77 76  3 83 93 18

#[aoc_generator(day4)]
fn parse_input(text: &str) -> Vec<(HashSet<u32>, HashSet<u32>)> {
    let p = parser!(lines(
        "Card" " "+ u32 ": " " "* winning:repeat_sep(u32, " "*) " |" " "+ numbers:repeat_sep(u32, " "*)  => (HashSet::from_iter(winning), HashSet::from_iter(numbers))
    ));
    p.parse(text).unwrap()
}

#[aoc(day4, part1)]
pub fn part1(input: &[(HashSet<u32>, HashSet<u32>)]) -> usize {
    input
        .iter()
        .filter_map(|(winning, numbers)| {
            let winners = winning & numbers;
            match winners.len() {
                0 => None,
                len => Some(2usize.pow((len as u32) - 1)),
            }
        })
        .sum()
}

#[aoc(day4, part2)]
pub fn part2(input: &[(HashSet<u32>, HashSet<u32>)]) -> usize {
    let mut duplicates: HashMap<usize, usize> = HashMap::new();
    let mut stack: HashMap<usize, usize> = HashMap::new();

    for (card, (winning, numbers)) in input.iter().enumerate() {
        let winners = winning & numbers;
        let copies = {
            let copies = duplicates.entry(card).or_insert(0);
            *copies += 1;
            *copies
        };

        {
            let c = stack.entry(card).or_insert(0);
            *c += copies
        }

        if !winners.is_empty() {
            for v in 1..=winners.len() {
                let duplicate = duplicates.entry(card + v).or_insert(0);
                *duplicate += copies;
            }
        }
    }

    stack.values().sum()
}

#[cfg(test)]
mod tests {
    // use super::{part1, part2};
}
