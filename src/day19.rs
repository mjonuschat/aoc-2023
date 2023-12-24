use aoc_parse::{parser, prelude::*};
use aoc_runner_derive::*;
use itertools::Itertools;
use std::collections::HashMap;

type WorkFlows = HashMap<String, (Vec<(char, bool, usize, String)>, String)>;
type Part = (usize, usize, usize, usize);

#[aoc_generator(day19)]
fn parse_input(text: &str) -> (WorkFlows, Vec<Part>) {
    let p = parser!(
        section(hash_map(lines(name:string(alnum+) "{" workflows:string(any_char+) "}" => {
            let (rules, dest) = workflows.split_at(workflows.rfind(',').unwrap());
            let dest = dest[1..].to_string();
            let rules = rules.split(',').map(|rule| {
                let (cond, next) = rule.split_once(':').unwrap();
                let gt = cond.contains('>');
                let (name, val) = cond.split_once(if gt { '>' } else {'<'}).unwrap();
                (name.chars().next().unwrap(), gt, val.parse::<usize>().unwrap(), next.to_string())
            }).collect::<Vec<_>>();
            (name, (rules, dest))
        })))
        section(lines("{x=" usize ",m=" usize ",a=" usize ",s=" usize "}"))
    );
    p.parse(text).unwrap()
}

fn accept(part: &Part, wf: &str, workflows: &WorkFlows) -> bool {
    let mut cur = wf;
    while cur != "A" && cur != "R" {
        let wf = &workflows[cur];
        cur =
            wf.0.iter()
                .find(|(cat, gt, val, _)| {
                    let p = match cat {
                        'x' => part.0,
                        'm' => part.1,
                        'a' => part.2,
                        's' => part.3,
                        _ => unreachable!(),
                    };

                    if *gt {
                        p > *val
                    } else {
                        p < *val
                    }
                })
                .map(|(_, _, _, dest)| dest)
                .unwrap_or(&wf.1)
    }
    cur == "A"
}

fn count(workflows: &WorkFlows, cur: &str, mut ranges: [Vec<usize>; 4]) -> usize {
    if cur == "A" {
        return ranges.iter().map(|v| v.len()).product();
    }

    if cur == "R" {
        return 0;
    }

    let mut result = 0;
    let wf = &workflows[cur];
    for (cat, gt, val, ref dest) in &wf.0 {
        let i = "xmas".chars().position(|c| c == *cat).unwrap();
        let mut next = ranges.clone();
        (next[i], ranges[i]) = ranges[i]
            .iter()
            .partition(|&&n| if *gt { n > *val } else { n < *val });
        result += count(workflows, dest, next);
    }
    result += count(workflows, &wf.1, ranges);
    result
}
#[aoc(day19, part1)]
pub fn part1(input: &(WorkFlows, Vec<Part>)) -> usize {
    input
        .1
        .iter()
        .filter(|part| accept(part, "in", &input.0))
        .map(|(x, m, a, s)| x + m + a + s)
        .sum()
}

#[aoc(day19, part2)]
pub fn part2(input: &(WorkFlows, Vec<Part>)) -> usize {
    let ranges: [Vec<usize>; 4] = [
        (1..=4000).collect_vec(),
        (1..=4000).collect_vec(),
        (1..=4000).collect_vec(),
        (1..=4000).collect_vec(),
    ];
    count(&input.0, "in", ranges)
}

#[cfg(test)]
mod tests {}
