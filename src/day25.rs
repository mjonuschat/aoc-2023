use aoc_parse::{parser, prelude::*};
use aoc_runner_derive::*;
use std::collections::{HashMap, HashSet, VecDeque};

type Input = HashMap<String, HashSet<String>>;

#[aoc_generator(day25)]
fn parse_input(text: &str) -> Input {
    let p = parser!(lines(
        wire:string(alpha+) ": " connected:repeat_sep(string(alpha+), " ")
    ));
    let data = p.parse(text).unwrap();
    let mut connections: Input = HashMap::new();
    for (wire, connected) in &data {
        for conn in connected {
            connections
                .entry(wire.to_owned())
                .or_default()
                .insert(conn.to_owned());
            connections
                .entry(conn.to_owned())
                .or_default()
                .insert(wire.to_owned());
        }
    }
    connections
}

fn bfs(graph: &Input) -> usize {
    let start = graph.keys().next().cloned().unwrap();
    let mut queue = VecDeque::from([start]);
    let mut seen = HashSet::new();
    while let Some(curr) = queue.pop_front() {
        if seen.insert(curr.clone()) {
            queue.extend(graph[&curr].iter().cloned())
        }
    }
    seen.len()
}

fn find_link(graph: &Input) -> (String, String) {
    let mut links: HashMap<(String, String), usize> = HashMap::new();
    for start in graph.keys() {
        let mut queue = VecDeque::from([start]);
        let mut seen = HashSet::from([start]);
        while let Some(curr) = queue.pop_front() {
            for node in graph.get(&curr.to_owned()).unwrap() {
                if !seen.insert(node) {
                    continue;
                }
                queue.push_back(node);
                let link = if curr < node {
                    (curr.to_owned(), node.to_owned())
                } else {
                    (node.to_owned(), curr.to_owned())
                };
                *links.entry(link).or_default() += 1;
            }
        }
    }
    links
        .into_iter()
        .max_by_key(|(_k, v)| *v)
        .map(|(k, _v)| (k.0.to_owned(), k.1.to_owned()))
        .unwrap()
}

#[aoc(day25, part1)]
pub fn part1(input: &Input) -> usize {
    let mut graph = input.clone();
    for _ in 0..3 {
        let (src, dest) = find_link(&graph);
        graph.get_mut(&src).map(|v| v.remove(&dest));
        graph.get_mut(&dest).map(|v| v.remove(&src));
    }
    let size = bfs(&graph);
    size * (graph.len() - size)
}

#[cfg(test)]
mod tests {
    // use super::{part1, part2};
}
