use aoc_parse::{parser, prelude::*};
use aoc_runner_derive::*;
use itertools::Itertools;
use std::collections::HashSet;

type Input = Vec<Hailstone>;

#[derive(Debug)]
pub struct Hailstone {
    x: f64,
    y: f64,
    z: f64,
    vx: f64,
    vy: f64,
    vz: f64,
}

#[aoc_generator(day24)]
fn parse_input(text: &str) -> Input {
    let p = parser!(lines(
        x:f64 ", " y:f64 ", " z:f64 " @ " vx:f64 ", " vy:f64 ", " vz:f64 => Hailstone { x,y,z,vx,vy,vz}
    ));
    p.parse(text).unwrap()
}

fn intersect(hailstones: &Input, start: f64, end: f64) -> usize {
    let mut result = 0;
    for (h1, h2) in hailstones.iter().tuple_combinations() {
        let s1 = h1.vy / h1.vx;
        let i1 = h1.y - s1 * h1.x;

        let s2 = h2.vy / h2.vx;
        let i2 = h2.y - s2 * h2.x;

        if s1 == s2 {
            continue;
        }

        let ix = (i2 - i1) / (s1 - s2);
        let iy = s1 * ix + i1;

        let t1 = (ix - h1.x) / h1.vx;
        let t2 = (ix - h2.x) / h2.vx;

        if t1 < 0.0 || t2 < 0.0 {
            continue;
        }

        if (start..=end).contains(&ix) && (start..=end).contains(&iy) {
            result += 1
        }
    }
    result
}

#[aoc(day24, part1)]
pub fn part1(input: &Input) -> usize {
    intersect(input, 200000000000000.0, 400000000000000.0)
}

#[aoc(day24, part2)]
pub fn part2(input: &Input) -> usize {
    let mut x_candidates = HashSet::from_iter(-1000..1000);
    let mut y_candidates = HashSet::from_iter(-1000..1000);
    let mut z_candidates = HashSet::from_iter(-1000..1000);
    for (h1, h2) in input.iter().tuple_combinations() {
        if h1.vx == h2.vx && h1.vx.abs() > 100.0 {
            let dx = (h2.x - h1.x) as isize;
            let t = (-1000..1000)
                .filter(|v| *v != h1.vx as isize && dx % (h1.vx as isize - v) == 0)
                .collect::<HashSet<_>>();
            x_candidates = x_candidates.intersection(&t).cloned().collect();
        }

        if h1.vy == h2.vy && h1.vy.abs() > 100.0 {
            let dy = (h2.y - h1.y) as isize;
            let t = (-1000..1000)
                .filter(|v| *v != h1.vy as isize && dy % (h1.vy as isize - v) == 0)
                .collect::<HashSet<_>>();
            y_candidates = y_candidates.intersection(&t).cloned().collect();
        }

        if h1.vz == h2.vz && h1.vz.abs() > 100.0 {
            let dz = (h2.z - h1.z) as isize;
            let t = (-1000..1000)
                .filter(|v| *v != h1.vz as isize && dz % (h1.vz as isize - v) == 0)
                .collect::<HashSet<_>>();
            z_candidates = z_candidates.intersection(&t).cloned().collect();
        }
    }

    let rock_vx = *x_candidates.iter().next().unwrap() as f64;
    let rock_vy = *y_candidates.iter().next().unwrap() as f64;
    let rock_vz = *z_candidates.iter().next().unwrap() as f64;

    // Hailstone velocities
    let h1 = &input[0];
    let h2 = &input[1];

    // Subtracting the rock velocities from two hailstones to get a new "line"
    // representing all of the potential start. Algebraic intersection with the
    // two lines created from the hailstones gets the final answer.

    let m1 = (h1.vy - rock_vy) / (h1.vx - rock_vx);
    let m2 = (h2.vy - rock_vy) / (h2.vx - rock_vx);
    let c1 = h1.y - (m1 * h1.x);
    let c2 = h2.y - (m2 * h2.x);

    let sx = (c2 - c1) / (m1 - m2);
    let sy = m1 * sx + c1;
    let sz = h1.z + (h1.vz - rock_vz) * ((sx - h1.x) / (h1.vx - rock_vx));

    (sx + sy + sz) as usize
}

#[cfg(test)]
mod tests {
    // use super::{part1, part2};
}
