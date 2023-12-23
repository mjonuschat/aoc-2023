use aoc_parse::{parser, prelude::*};
use aoc_runner_derive::*;
use michie::memoized;
use std::collections::HashMap;

#[aoc_generator(day12)]
fn parse_input(text: &str) -> Vec<(Vec<u8>, Vec<usize>)> {
    let p = parser!(lines(groups:string(any_char+) " " counts:repeat_sep(usize, ",") => (groups.as_bytes().to_vec(), counts)));
    p.parse(text).unwrap()
}

#[allow(clippy::type_complexity)]
#[memoized(key_expr = (group.to_owned(), within, counts.to_owned()), store_type = HashMap<(Vec<u8>, Option<usize>, Vec<usize>), usize>)]
fn solve(group: &[u8], within: Option<usize>, counts: &[usize]) -> usize {
    if group.is_empty() {
        return match within {
            None if counts.is_empty() => 1,
            Some(v) if counts.len() == 1 && v == counts[0] => 1,
            _ => 0,
        };
    }

    let more = group.iter().filter(|c| **c == b'#' || **c == b'?').count();
    if let Some(v) = within {
        if more + v < counts.iter().sum() {
            return 0;
        }
        if counts.is_empty() {
            return 0;
        }
    } else if more < counts.iter().sum() {
        return 0;
    }

    let mut poss = 0;
    if group[0] == b'.' {
        if let Some(within) = within {
            if within != counts[0] {
                return 0;
            }
        }
    }

    if group[0] == b'.' && within.is_some() {
        poss += solve(&group[1..], None, &counts[1..])
    }

    if group[0] == b'?' {
        if let Some(within) = within {
            if within == counts[0] {
                poss += solve(&group[1..], None, &counts[1..]);
            }
        }
    }

    if group[0] == b'#' || group[0] == b'?' {
        if let Some(within) = within {
            poss += solve(&group[1..], Some(within + 1), counts);
        }
    }

    if (group[0] == b'?' || group[0] == b'#') && within.is_none() {
        poss += solve(&group[1..], Some(1), counts);
    }

    if (group[0] == b'?' || group[0] == b'.') && within.is_none() {
        poss += solve(&group[1..], None, counts)
    }

    poss
}

#[aoc(day12, part1)]
pub fn part1(input: &[(Vec<u8>, Vec<usize>)]) -> usize {
    input
        .iter()
        .map(|(group, counts)| solve(group, None, counts))
        .sum()
}

#[aoc(day12, part2)]
pub fn part2(input: &[(Vec<u8>, Vec<usize>)]) -> usize {
    input
        .iter()
        .map(|(group, counts)| {
            let mut a = group.clone();
            for _ in 0..4 {
                a.push(b'?');
                a.extend(group.clone());
            }
            solve(&a, None, &counts.repeat(5))
        })
        .sum()
}

#[cfg(test)]
mod tests {
    // use super::{part1, part2};
}
