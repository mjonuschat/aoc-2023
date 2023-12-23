use aoc_parse::{parser, prelude::*};
use aoc_runner_derive::*;
use num::Complex;
use std::collections::{HashMap, HashSet, VecDeque};

#[aoc_generator(day16)]
fn parse_input(text: &str) -> (Vec<String>, HashMap<Complex<isize>, char>) {
    let p = parser!(lines(string(any_char+)));
    let grid = p.parse(text).unwrap();
    let mut locations = HashMap::new();
    for (i, line) in grid.iter().enumerate() {
        for (j, c) in line.chars().enumerate() {
            locations.insert(Complex::new(i as isize, j as isize), c);
        }
    }
    (grid, locations)
}

fn energized(
    start: Complex<isize>,
    dir: Complex<isize>,
    locations: &HashMap<Complex<isize>, char>,
) -> usize {
    let mut seen = HashSet::new();
    let mut deck = VecDeque::new();

    deck.push_back((start - dir, dir));
    while !deck.is_empty() {
        let (l, d) = deck.pop_back().unwrap();
        if seen.contains(&(l, d)) {
            continue;
        }
        seen.insert((l, d));
        let nl = l + d;
        if let Some(tile) = locations.get(&nl) {
            let nd = match *tile {
                '|' if d.im != 0 => vec![Complex::new(1, 0), Complex::new(-1, 0)],
                '-' if d.re != 0 => vec![Complex::new(0, 1), Complex::new(0, -1)],
                '/' => vec![(d * Complex::new(0, 1)).conj()],
                '\\' => vec![(d * Complex::new(0, -1)).conj()],
                _ => vec![d],
            };
            for x in nd {
                deck.push_back((nl, x));
            }
        }
    }
    seen.iter().map(|x| x.0).collect::<HashSet<_>>().len() - 1
}
#[aoc(day16, part1)]
pub fn part1(input: &(Vec<String>, HashMap<Complex<isize>, char>)) -> usize {
    energized(Complex::new(0, 0), Complex::new(0, 1), &input.1)
}

#[aoc(day16, part2)]
pub fn part2(input: &(Vec<String>, HashMap<Complex<isize>, char>)) -> usize {
    let rows = input.0.len() as isize;
    let cols = input.0[0].len() as isize;
    let mut entrypoints = vec![];
    entrypoints.extend((0..cols).map(|i| (Complex::new(0, i), Complex::new(1, 0))));
    entrypoints.extend((0..cols).map(|i| (Complex::new(rows - 1, i), Complex::new(-1, 0))));

    entrypoints.extend((0..rows).map(|i| (Complex::new(i, 0), Complex::new(0, 1))));
    entrypoints.extend((0..rows).map(|i| (Complex::new(i, cols - 1), Complex::new(0, -1))));
    entrypoints
        .iter()
        .map(|(l, d)| energized(*l, *d, &input.1))
        .max()
        .unwrap()
}

#[cfg(test)]
mod tests {
    // use super::{part1, part2};
}
