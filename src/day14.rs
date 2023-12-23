use aoc_parse::{parser, prelude::*};
use aoc_runner_derive::*;
use itertools::Itertools;
use std::collections::HashMap;

#[aoc_generator(day14)]
fn parse_input(text: &str) -> Vec<Vec<u8>> {
    let p = parser!(lines(l:string(any_char+) => l.as_bytes().to_vec()));
    p.parse(text).unwrap()
}

fn roll_north(map: &mut Vec<Vec<u8>>) {
    let mut done = false;
    while !done {
        done = true;
        for row in 0..map.len() - 1 {
            for col in 0..map[row].len() {
                if map[row + 1][col] == b'O' && map[row][col] == b'.' {
                    map[row][col] = b'O';
                    map[row + 1][col] = b'.';
                    done = false;
                }
            }
        }
    }
}

fn score(map: &Vec<Vec<u8>>) -> usize {
    (0..map.len())
        .map(|row| {
            (0..map[0].len())
                .filter(|&col| map[row][col] == b'O')
                .map(|_| map.len() - row)
                .sum::<usize>()
        })
        .sum()
}

fn rotate(map: &Vec<Vec<u8>>) -> Vec<Vec<u8>> {
    let mut rotated = vec![vec![0; map.len()]; map[0].len()];
    for (row, col) in (0..map.len()).cartesian_product(0..map[0].len()) {
        rotated[col][map.len() - 1 - row] = map[row][col];
    }
    rotated
}
#[aoc(day14, part1)]
pub fn part1(input: &[Vec<u8>]) -> usize {
    let mut map = input.to_vec();
    roll_north(&mut map);
    score(&map)
}

#[aoc(day14, part2)]
pub fn part2(input: &[Vec<u8>]) -> usize {
    let mut map = input.to_vec();
    let mut seen = HashMap::new();
    for i in 1..1000000000 {
        for _ in 0..4 {
            roll_north(&mut map);
            map = rotate(&map)
        }
        if let Some(seen_at) = seen.insert(map.clone(), i) {
            if (1000000000 - i) % (i - seen_at) == 0 {
                break;
            }
        }
    }
    score(&map)
}

#[cfg(test)]
mod tests {
    // use super::{part1, part2};
}
