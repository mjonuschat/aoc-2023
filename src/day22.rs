use aoc_parse::{parser, prelude::*};
use aoc_runner_derive::*;
use std::collections::HashMap;

type Brick = (usize, usize, usize, usize, usize, usize);
type Input = Vec<Brick>;
#[aoc_generator(day22)]
fn parse_input(text: &str) -> Input {
    let p = parser!(lines(
        usize "," usize "," usize "~" usize "," usize "," usize
    ));
    let mut data = p.parse(text).unwrap();
    data.sort_by_key(|f| f.2);
    data
}

fn disintegrate(bricks: &Input) -> (usize, Input) {
    let mut tallest: HashMap<(usize, usize), usize> = HashMap::new();
    let mut new_bricks = vec![];
    let mut falls = 0;
    for brick in bricks {
        let new_brick = drop_brick(&tallest, brick);
        if new_brick.2 != brick.2 {
            falls += 1;
        }
        new_bricks.push(new_brick);
        for x in brick.0..brick.3 + 1 {
            for y in brick.1..brick.4 + 1 {
                tallest.insert((x, y), new_brick.5);
            }
        }
    }
    (falls, new_bricks)
}

fn drop_brick(tallest: &HashMap<(usize, usize), usize>, brick: &Brick) -> Brick {
    let peak = (brick.0..brick.3 + 1)
        .flat_map(|x| (brick.1..brick.4 + 1).map(move |y| tallest.get(&(x, y)).unwrap_or(&0)))
        .max()
        .unwrap();

    let z = 0.max(brick.2 - peak - 1);
    (brick.0, brick.1, brick.2 - z, brick.3, brick.4, brick.5 - z)
}

#[aoc(day22, part1)]
pub fn part1(input: &Input) -> usize {
    let (_, fallen) = disintegrate(input);
    let mut result = 0;
    for i in 0..fallen.len() {
        let mut removed = fallen[..i].to_vec();
        removed.extend(fallen[i + 1..].iter());
        let (falls, _) = disintegrate(&removed);
        if falls == 0 {
            result += 1
        }
    }

    result
}

#[aoc(day22, part2)]
pub fn part2(input: &Input) -> usize {
    let (_, fallen) = disintegrate(input);
    let mut result = 0;
    for i in 0..fallen.len() {
        let mut removed = fallen[..i].to_vec();
        removed.extend(fallen[i + 1..].iter());
        let (falls, _) = disintegrate(&removed);
        if falls > 0 {
            result += falls
        }
    }

    result
}

#[cfg(test)]
mod tests {
    // use super::{part1, part2};
}
