use aoc_parse::{parser, prelude::*};
use aoc_runner_derive::*;
use maplit::hashmap;
use once_cell::sync::Lazy;
use std::collections::{HashMap, VecDeque};

static PIPES: Lazy<HashMap<char, Vec<char>>> = Lazy::new(|| {
    hashmap! {
      '|' => vec!['N', 'S'],
      '-'=> vec!['W', 'E'],
      'L'=> vec!['N', 'E'],
      'J'=> vec!['N', 'W'],
      '7'=> vec!['S', 'W'],
      'F'=> vec!['S', 'E'],
      'S'=> vec!['N', 'E', 'S', 'W'],
    }
});

static DIRECTIONS: Lazy<HashMap<char, (isize, isize, char)>> = Lazy::new(|| {
    hashmap! {
        'N'=> (-1, 0, 'S'),
        'S'=> (1, 0, 'N'),
        'W'=> (0, -1, 'E'),
        'E'=> (0, 1, 'W'),
    }
});

#[aoc_generator(day10)]
fn parse_input(text: &str) -> Vec<Vec<char>> {
    let p = parser!(
        lines(any_char*)
    );
    p.parse(text).unwrap()
}

fn find_loop(m: &[Vec<char>], start_tile: Option<char>) -> (HashMap<(isize, isize), i32>, i32) {
    let (start_row, start_col) = find_start(m);
    let mut visited = HashMap::new();
    let mut queue = VecDeque::new();
    queue.push_back(((start_row, start_col), 0));
    while let Some((loc, distance)) = queue.pop_front() {
        if visited.contains_key(&loc) {
            continue;
        }
        visited.insert(loc, distance);
        let (row, col) = loc;
        for connection in &PIPES[&m[row as usize][col as usize]] {
            let (nr, nc, reverse) = DIRECTIONS[connection];
            if row + nr < 0 || row + nr > m.len() as isize {
                continue;
            }
            if col + nc < 0 || col + nc > m[(col + nc) as usize].len() as isize {
                continue;
            }
            let mut dest = &m[(row + nr) as usize][(col + nc) as usize];
            if *dest == 'S' {
                if let Some(t) = start_tile.as_ref() {
                    dest = t;
                }
            }
            if !PIPES.contains_key(dest) {
                continue;
            }
            if PIPES[dest].contains(&reverse) {
                queue.push_back(((row + nr, col + nc), distance + 1))
            }
        }
    }

    let max_distance = visited.values().max().unwrap().to_owned();
    (visited, max_distance)
}

fn find_start(m: &[Vec<char>]) -> (isize, isize) {
    for (i, row) in m.iter().enumerate() {
        for (j, col) in row.iter().enumerate() {
            if *col == 'S' {
                return (i as isize, j as isize);
            }
        }
    }
    unreachable!()
}

fn enclosed(m: &[Vec<char>], visited: HashMap<(isize, isize), i32>) -> usize {
    let mut area = m.to_owned();

    for (i, row) in area.iter_mut().enumerate() {
        let mut verticals = 0;
        for (j, col) in row.iter_mut().enumerate() {
            if visited.contains_key(&(i as isize, j as isize)) {
                let directions = &PIPES[col];
                if directions.contains(&'N') {
                    verticals += 1
                }
                continue;
            }
            if verticals % 2 == 0 {
                *col = '.'
            } else {
                *col = 'I'
            }
        }
    }

    area.iter()
        .map(|row| row.iter().filter(|c| **c == 'I').count())
        .sum()
}
#[aoc(day10, part1)]
pub fn part1(input: &[Vec<char>]) -> i32 {
    let (_, max_distance) = find_loop(input, None);
    max_distance
}

#[aoc(day10, part2)]
pub fn part2(input: &[Vec<char>]) -> usize {
    let (visited, _) = find_loop(input, Some('L'));
    enclosed(input, visited)
}

#[cfg(test)]
mod tests {
    // use super::{part1, part2};
}
