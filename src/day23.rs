use aoc_parse::{parser, prelude::*};
use aoc_runner_derive::*;
use itertools::Itertools;
use std::collections::HashMap;

type Input = Vec<Vec<char>>;
type Node = (usize, usize, usize);
type Coord = (usize, usize);
type Graph = HashMap<Coord, Vec<Node>>;
static DIRECTIONS: &[(isize, isize)] = &[(-1, 0), (0, 1), (1, 0), (0, -1)];

fn dfs(graph: &Graph, seen: &mut Vec<Vec<bool>>, (r, c): (usize, usize)) -> Option<usize> {
    if r == seen.len() - 1 {
        return Some(0);
    }
    let mut max_dist = None;
    for &(rr, cc, d) in &graph[&(r, c)] {
        if !seen[rr][cc] {
            seen[rr][cc] = true;
            if let Some(dist) = dfs(graph, seen, (rr, cc)) {
                max_dist = Some(max_dist.unwrap_or(0).max(d + dist))
            }
            seen[rr][cc] = false;
        }
    }
    max_dist
}

fn solve(grid: &Input, mut graph: Graph) -> usize {
    let paths = graph
        .iter()
        .filter(|(_, n)| n.len() == 2)
        .map(|(&node, _)| node)
        .collect::<Vec<_>>();
    for (row, col) in paths {
        let neighbors = graph.remove(&(row, col)).unwrap();
        let (r1, c1, d1) = neighbors[0];
        let (r2, c2, d2) = neighbors[1];
        let n1 = graph.get_mut(&(r1, c1)).unwrap();
        if let Some(i) = n1.iter().position(|&(rr, cc, _)| (rr, cc) == (row, col)) {
            n1[i] = (r2, c2, d1 + d2);
        }
        let n2 = graph.get_mut(&(r2, c2)).unwrap();
        if let Some(i) = n2.iter().position(|&(rr, cc, _)| (rr, cc) == (row, col)) {
            n2[i] = (r1, c1, d1 + d2);
        }
    }

    dfs(
        &graph,
        &mut vec![vec![false; grid[0].len()]; grid.len()],
        (0, 1),
    )
    .unwrap()
}

#[aoc_generator(day23)]
fn parse_input(text: &str) -> Input {
    let p = parser!(lines(any_char+));
    p.parse(text).unwrap()
}

#[aoc(day23, part1)]
pub fn part1(input: &Input) -> usize {
    let mut graph: Graph = HashMap::new();
    for (row, col) in (0..input.len()).cartesian_product(0..input[0].len()) {
        let neighbors = match input[row][col] {
            '#' => continue,
            '.' => DIRECTIONS,
            '^' => &DIRECTIONS[0..][..1],
            '>' => &DIRECTIONS[1..][..1],
            'v' => &DIRECTIONS[2..][..1],
            '<' => &DIRECTIONS[3..][..1],
            _ => unreachable!(),
        };
        let e = graph.entry((row, col)).or_default();
        for (dr, dc) in neighbors {
            let r = (row as isize + dr) as usize;
            let c = (col as isize + dc) as usize;
            if input
                .get(r)
                .and_then(|row| row.get(c))
                .is_some_and(|&t| t != '#')
            {
                e.push((r, c, 1));
            }
        }
    }
    solve(input, graph)
}

#[aoc(day23, part2)]
pub fn part2(input: &Input) -> usize {
    let mut graph: Graph = HashMap::new();
    for (row, col) in (0..input.len()).cartesian_product(0..input[0].len()) {
        if input[row][col] == '#' {
            continue;
        }
        let neighbors = DIRECTIONS;
        let e = graph.entry((row, col)).or_default();
        for (dr, dc) in neighbors {
            let r = (row as isize + dr) as usize;
            let c = (col as isize + dc) as usize;
            if input
                .get(r)
                .and_then(|row| row.get(c))
                .is_some_and(|&t| t != '#')
            {
                e.push((r, c, 1));
            }
        }
    }
    solve(input, graph)
}

#[cfg(test)]
mod tests {
    // use super::{part1, part2};
}
