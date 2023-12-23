use aoc_parse::{parser, prelude::*};
use aoc_runner_derive::*;
use itertools::iproduct;
use std::collections::HashMap;

#[aoc_generator(day7)]
fn parse_input(text: &str) -> Vec<(String, usize)> {
    let p = parser!(
        lines(string(alnum+) " " usize)
    );
    p.parse(text).unwrap()
}

fn score(counts: HashMap<char, i32>) -> i32 {
    let mut dist = HashMap::new();
    let mut score = 0;
    for v in counts.values() {
        let d = dist.entry(*v).or_insert(0);
        *d += 1
    }
    if dist.contains_key(&5) {
        score = 6
    } else if dist.contains_key(&4) {
        score = 5
    } else if dist.contains_key(&3) {
        if dist.contains_key(&2) {
            score = 4
        } else {
            score = 3
        }
    } else if dist.contains_key(&2) {
        if dist.get(&2).unwrap_or(&0) == &2 {
            score = 2
        } else {
            score = 1
        }
    }

    score
}
#[aoc(day7, part1)]
pub fn part1(input: &[(String, usize)]) -> usize {
    let mut res = vec![];
    for (hand, bid) in input {
        let mut counts = HashMap::new();
        for c in hand.chars() {
            let count = counts.entry(c).or_insert(0);
            *count += 1
        }
        let s = score(counts);
        let strength: Vec<usize> = hand
            .chars()
            .filter_map(|c| "23456789TJQKA".find(c))
            .collect();
        res.push((s, strength, *bid));
    }
    res.sort();
    res.iter()
        .enumerate()
        .map(|(i, (_, _, bid))| bid * (i + 1))
        .sum()
}

#[aoc(day7, part2)]
pub fn part2(input: &[(String, usize)]) -> usize {
    let mut res = vec![];
    for (hand, bid) in input {
        let mut m = 0;
        let phand = hand
            .chars()
            .map(|c| {
                if c == 'J' {
                    "23456789TQKA".to_string()
                } else {
                    c.to_string()
                }
            })
            .collect::<Vec<_>>();
        for h in iproduct!(
            phand[0].chars(),
            phand[1].chars(),
            phand[2].chars(),
            phand[3].chars(),
            phand[4].chars()
        ) {
            let mut counts = HashMap::new();
            for c in [h.0, h.1, h.2, h.3, h.4] {
                let x = counts.entry(c).or_insert(0);
                *x += 1;
            }
            let s = score(counts);
            m = m.max(s);
        }
        let strength = hand
            .chars()
            .map(|c| "J23456789TQKA".find(c).unwrap_or(0))
            .collect::<Vec<_>>();
        res.push((m, strength, bid));
    }
    res.sort();
    res.iter()
        .enumerate()
        .map(|(i, (_, _, bid))| *bid * (i + 1))
        .sum()
}

#[cfg(test)]
mod tests {
    // use super::{part1, part2};
}
