use aoc_parse::{parser, prelude::*};
use aoc_runner_derive::*;
use std::collections::HashMap;

#[aoc_generator(day8)]
fn parse_input(text: &str) -> (Vec<usize>, HashMap<String, Vec<String>>) {
    let p = parser!(
        section(line({"L" => 0, "R" => 1}+))
        section(hash_map(lines(string(alnum+) " = (" repeat_sep(string(alnum+), ", ") ")")))
    );
    p.parse(text).unwrap()
}

#[aoc(day8, part1)]
pub fn part1(input: &(Vec<usize>, HashMap<String, Vec<String>>)) -> usize {
    let (direction, m) = (&input.0, &input.1);
    let mut cur = "AAA";
    for (steps, dir) in direction.iter().cycle().enumerate() {
        cur = &m.get(cur).unwrap()[*dir];
        if cur == "ZZZ" {
            return steps + 1;
        }
    }

    unreachable!()
}

#[aoc(day8, part2)]
pub fn part2(input: &(Vec<usize>, HashMap<String, Vec<String>>)) -> usize {
    let (direction, m) = (&input.0, &input.1);
    let mut cur = m.keys().filter(|l| l.ends_with('A')).collect::<Vec<_>>();
    let mut steps = cur.iter().map(|_| -1).collect::<Vec<isize>>();

    for (i, dir) in direction.iter().cycle().enumerate() {
        cur = cur
            .iter()
            .map(|c| &m.get(c.to_owned()).unwrap()[*dir])
            .collect();
        for (j, c) in cur.iter().enumerate() {
            if steps[j] < 0 && c.ends_with('Z') {
                steps[j] = 1 + i as isize;
            }
        }
        if steps.iter().all(|s| *s > 0) {
            break;
        }
    }
    steps
        .iter()
        .fold(1, |a, i| num::integer::lcm(a, *i as usize))
}

#[cfg(test)]
mod tests {
    // use super::{part1, part2};
}
