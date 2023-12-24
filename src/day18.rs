use aoc_parse::{parser, prelude::*};
use aoc_runner_derive::*;
use maplit::hashmap;
use once_cell::sync::Lazy;
use std::collections::HashMap;

static DIRECTIONS: Lazy<HashMap<char, (i64, i64)>> = Lazy::new(|| {
    hashmap! {
        'R'=> (1, 0), 'L'=> (-1, 0), 'U'=> (0, -1), 'D'=> (0, 1),
    }
});

static HEX_TO_DIR: Lazy<HashMap<char, char>> = Lazy::new(|| {
    hashmap! {
        '0' => 'R',
        '1' => 'D',
        '2' => 'L',
        '3' => 'U',
    }
});

fn shoelace(shape: &[(i64, i64)]) -> i64 {
    let mut result = 0;
    for i in 0..shape.len() {
        let prev = if i == 0 {
            shape[shape.len() - 1]
        } else {
            shape[i - 1]
        };
        let cur = shape[i];
        result += prev.0 * cur.1 - cur.1 * cur.0
    }
    result.abs()
}

#[aoc_generator(day18)]
fn parse_input(text: &str) -> Vec<(char, i64, String)> {
    let p = parser!(lines(
        dir:alpha " " len:i64 " (#" color:string(alnum+) ")"
    ));
    p.parse(text).unwrap()
}

#[aoc(day18, part1)]
pub fn part1(input: &[(char, i64, String)]) -> i64 {
    let mut shape = vec![(0i64, 0i64)];
    let mut length = 0;

    for (dir, dist, _) in input {
        let last = &shape[shape.len() - 1];

        let d = DIRECTIONS[dir];
        let steps = dist;

        length += steps;
        shape.push((last.0 + d.0 * steps, last.1 + d.1 * steps));
    }

    shoelace(&shape) + length / 2 + 1
}

#[aoc(day18, part2)]
pub fn part2(input: &[(char, i64, String)]) -> i64 {
    let mut shape = vec![(0i64, 0i64)];
    let mut length = 0;

    for (_, _, color) in input {
        let last = &shape[shape.len() - 1];
        let steps = i64::from_str_radix(&color.chars().take(5).collect::<String>(), 16).unwrap();
        let d = DIRECTIONS[&HEX_TO_DIR[&color.chars().nth(5).unwrap()]];

        length += steps;
        shape.push((last.0 + d.0 * steps, last.1 + d.1 * steps));
    }

    shoelace(&shape) + length / 2 + 1
}

#[cfg(test)]
mod tests {
    // use super::{part1, part2};
}
