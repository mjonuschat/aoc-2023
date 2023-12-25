use aoc_parse::{parser, prelude::*};
use aoc_runner_derive::*;
use std::collections::{HashMap, VecDeque};

pub type Input = HashMap<String, (ModuleKind, Vec<String>)>;
#[derive(Debug)]
pub enum ModuleKind {
    Normal,
    FlipFlop,
    Conjunction,
}
#[aoc_generator(day20)]
fn parse_input(text: &str) -> Input {
    let p = parser!(hash_map(lines(
        src:string(any_char+) " -> " dests:repeat_sep(string(alpha+), ", ") => {
            let kind = match src.chars().next() {
                Some('%') => ModuleKind::FlipFlop,
                Some('&') => ModuleKind::Conjunction,
                Some(_) => ModuleKind::Normal,
                None => unreachable!()
            };
            let name = match kind {
                ModuleKind::FlipFlop | ModuleKind::Conjunction => (src[1..]).to_string(),
                _ => src,
            };
            (name, (kind, dests))
        }
    )));
    p.parse(text).unwrap()
}

#[aoc(day20, part1)]
pub fn part1(data: &Input) -> usize {
    let mut flipflops: HashMap<&str, bool> = HashMap::new();
    let mut conjunctions: HashMap<String, HashMap<String, usize>> = HashMap::new();
    let mut counts = [0; 2];

    for (src, (_kind, dests)) in data {
        for dest in dests {
            let d = conjunctions.entry(dest.to_owned()).or_default();
            (*d).insert(src.to_owned(), 0);
        }
    }

    for _ in 0..1000 {
        let mut queue = VecDeque::from_iter([(None, "broadcaster", 0)]);
        while let Some((src, module, input)) = queue.pop_front() {
            counts[input] += 1;
            if !data.contains_key(module) {
                continue;
            }

            let (kind, dests) = &data[module];
            let output = match (kind, input) {
                (ModuleKind::Normal, _) => input,
                (ModuleKind::FlipFlop, 0) => {
                    let ff = flipflops.entry(module).or_insert(false);
                    *ff = !*ff;
                    *ff as usize
                }
                (ModuleKind::Conjunction, _) => {
                    let cj = conjunctions.entry(module.to_string()).or_default();
                    (*cj).insert(src.unwrap(), input);
                    (!conjunctions[module].values().all(|v| *v > 0)) as usize
                }
                (_, _) => continue,
            };

            for d in dests {
                queue.push_back((Some(module.to_string()), d, output))
            }
        }
    }
    counts.iter().product()
}

#[aoc(day20, part2)]
pub fn part2(data: &Input) -> usize {
    let mut flipflops: HashMap<&str, bool> = HashMap::new();
    let mut conjunctions: HashMap<String, HashMap<String, usize>> = HashMap::new();
    for (src, (_, dests)) in data {
        for dest in dests {
            let cj = conjunctions.entry(dest.to_string()).or_default();
            (*cj).insert(src.to_string(), 0);
        }
    }

    let rx = data
        .iter()
        .find(|(_src, (_kind, dests))| dests.contains(&"rx".to_string()))
        .map(|(src, _)| src)
        .unwrap();

    let mut counts: HashMap<String, usize> = conjunctions[rx]
        .keys()
        .map(|src| (src.to_owned(), 0))
        .collect();

    for (src, (_kind, dests)) in data {
        for dest in dests {
            let d = conjunctions.entry(dest.to_owned()).or_default();
            (*d).insert(src.to_owned(), 0);
        }
    }

    for press in 1..1_000_000_000 {
        if counts.values().all(|v| *v > 0) {
            break;
        }

        let mut queue = VecDeque::from_iter([(None, "broadcaster", 0)]);
        while let Some((src, module, input)) = queue.pop_front() {
            if !data.contains_key(module) {
                continue;
            }

            let (kind, dests) = &data[module];
            let output = match (kind, input) {
                (ModuleKind::Normal, _) => input,
                (ModuleKind::FlipFlop, 0) => {
                    let ff = flipflops.entry(module).or_insert(false);
                    *ff = !*ff;
                    *ff as usize
                }
                (ModuleKind::Conjunction, _) => {
                    if dests.contains(&"rx".to_string()) {
                        for (k, v) in &conjunctions[module] {
                            if *v > 0 {
                                counts.insert(k.to_string(), press);
                            }
                        }
                    }
                    let cj = conjunctions.entry(module.to_string()).or_default();
                    (*cj).insert(src.unwrap(), input);
                    (!conjunctions[module].values().all(|v| *v > 0)) as usize
                }
                (_, _) => continue,
            };

            for d in dests {
                queue.push_back((Some(module.to_string()), d, output))
            }
        }
    }

    counts.values().product()
}

#[cfg(test)]
mod tests {
    // use super::{part1, part2};
}
