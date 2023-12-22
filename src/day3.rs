use aoc_parse::{parser, prelude::*};
use aoc_runner_derive::*;
use std::collections::HashMap;

fn find_symbol(grid: &[Vec<u8>], row: usize, col: usize) -> Option<(usize, usize, char)> {
    for (row_delta, col_delta) in [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ] {
        let (r, c) = (
            (row as i32 + row_delta) as usize,
            (col as i32 + col_delta) as usize,
        );
        let Some(&s) = grid.get(r).and_then(|line| line.get(c)) else {
            continue;
        };
        if s != b'.' && !s.is_ascii_digit() {
            return Some((r, c, s as char));
        }
    }
    None
}
#[aoc_generator(day3)]
fn parse_input(text: &str) -> HashMap<(usize, usize, char), Vec<usize>> {
    let p = parser!(lines(
        value:line(string(any_char+)) => value.as_bytes().to_vec()
    ));
    let mut symbols = HashMap::new();
    let grid = p.parse(text).unwrap();

    for (row, line) in grid.iter().enumerate() {
        let mut col = 0;
        while col < line.len() {
            let (start, mut symbol) = (col, None);
            while col < line.len() && line[col].is_ascii_digit() {
                symbol = symbol.or_else(|| find_symbol(&grid, row, col));
                col += 1;
            }
            if let Some(symbol) = symbol {
                let number = line[start..col]
                    .iter()
                    .fold(0, |n, c| n * 10 + (c - b'0') as usize);
                symbols.entry(symbol).or_insert(vec![]).push(number);
            }
            col += 1;
        }
    }
    symbols
}

#[aoc(day3, part1)]
pub fn part1(input: &HashMap<(usize, usize, char), Vec<usize>>) -> usize {
    input.values().flatten().sum()
}

#[aoc(day3, part2)]
pub fn part2(input: &HashMap<(usize, usize, char), Vec<usize>>) -> usize {
    input
        .iter()
        .filter(|(&(_, _, symbol), numbers)| symbol == '*' && numbers.len() == 2)
        .map(|(_, numbers)| numbers[0] * numbers[1])
        .sum()
}

#[cfg(test)]
mod tests {
    // use super::{part1, part2};
}
