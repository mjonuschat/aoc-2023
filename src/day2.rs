use aoc_parse::{parser, prelude::*};
use aoc_runner_derive::*;
use maplit::hashmap;
use std::collections::HashMap;

#[derive(Clone, Debug)]
pub enum Color {
    Red(usize),
    Green(usize),
    Blue(usize),
}

// Game 100: 7 blue, 6 red, 5 green; 3 blue, 13 green, 11 red; 6 red, 13 green, 14 blue; 8 red, 10 blue, 15 green
// Game 1: 4 red, 3 blue; 6 blue, 16 green; 9 blue, 13 green, 1 red
#[aoc_generator(day2)]
fn parse_input(text: &str) -> Vec<(usize, Vec<Vec<Color>>)> {
    let p = parser!(lines(
        "Game " usize ": " repeat_sep(repeat_sep({amt:usize " blue" => Color::Blue(amt), amt:usize " red" => Color::Red(amt), amt:usize " green" => Color::Green(amt)}, ", "), "; ")
    ));
    p.parse(text).unwrap()
}

#[aoc(day2, part1)]
pub fn part1(input: &[(usize, Vec<Vec<Color>>)]) -> usize {
    input
        .iter()
        .filter_map(|(game, sets)| {
            let mut possible = true;
            for set in sets {
                for kind in set {
                    match kind {
                        Color::Red(cnt) if cnt > &12 => possible = false,
                        Color::Green(cnt) if cnt > &13 => possible = false,
                        Color::Blue(cnt) if cnt > &14 => possible = false,
                        _ => {}
                    }
                }
            }

            match possible {
                true => Some(game),
                false => None,
            }
        })
        .sum()
}

#[aoc(day2, part2)]
pub fn part2(input: &[(usize, Vec<Vec<Color>>)]) -> usize {
    input
        .iter()
        .map(|(_, sets)| {
            let mut power: HashMap<&str, usize> = hashmap! {
                "red" => 0,
                "green" => 0,
                "blue" => 0,
            };

            for set in sets {
                for kind in set {
                    match kind {
                        Color::Red(cnt) => power.insert("red", power["red"].max(*cnt)),
                        Color::Green(cnt) => power.insert("green", power["green"].max(*cnt)),
                        Color::Blue(cnt) => power.insert("blue", power["blue"].max(*cnt)),
                    };
                }
            }

            power["red"] * power["green"] * power["blue"]
        })
        .sum()
}

#[cfg(test)]
mod tests {
    // use super::{part1, part2};
}
