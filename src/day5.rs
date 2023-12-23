use aoc_parse::{parser, prelude::*};
use aoc_runner_derive::*;

#[derive(Debug)]
pub struct Range {
    dst: usize,
    src: usize,
    len: usize,
}

impl Range {
    pub fn start(&self) -> usize {
        self.src
    }

    pub fn end(&self) -> usize {
        self.src + self.len - 1
    }

    pub fn offset(&self) -> usize {
        self.dst - self.src
    }
}
pub struct Almanac {
    seeds: Vec<usize>,
    maps: Vec<Vec<Range>>,
}

#[aoc_generator(day5)]
fn parse_input(text: &str) -> Almanac {
    let p = parser!(
        seeds:section(line("seeds: " repeat_sep(usize, " "+)))
        maps:sections(
            name:line(string(any_char*))
            ranges:lines(d: usize " " s: usize " " l:usize => Range { dst:d, src:s, len:l})
        )
        => Almanac { seeds, maps: maps.into_iter().map(|(_, m)| m).collect() }
    );
    p.parse(text).unwrap()
}

#[aoc(day5, part1)]
pub fn part1(input: &Almanac) -> usize {
    let mut translations: Vec<Vec<usize>> = vec![];
    for seed in &input.seeds {
        let mut translation = vec![*seed];
        let mut lookup = *seed;
        for map in &input.maps {
            for range in map {
                let source = range.src..range.src + range.len;
                if source.contains(&lookup) {
                    lookup = range.dst + lookup - range.src;
                    break;
                }
            }
            translation.push(lookup);
        }
        translations.push(translation)
    }

    *translations
        .iter()
        .filter_map(|row| row.iter().last())
        .min()
        .unwrap()
}

fn translate(start: usize, end: usize, map: &[Range]) -> Vec<(usize, usize)> {
    let mut result = vec![];
    let mut start = start;
    for range in map {
        if start > range.end() || end < range.start() {
            continue;
        }
        if start < range.start() {
            result.append(&mut vec![
                (start, range.start() - 1),
                (
                    range.start() + range.offset(),
                    end.min(range.end()) + range.offset(),
                ),
            ])
        } else {
            result.append(&mut vec![(
                start + range.offset(),
                end.min(range.end()) + range.offset(),
            )])
        }

        if range.end() > end {
            return result;
        }

        start = range.end();
    }

    if result.is_empty() {
        result.push((start, end))
    }

    result
}
#[aoc(day5, part2)]
pub fn part2(input: &Almanac) -> usize {
    let mut locations: Vec<usize> = vec![];
    for pair in input.seeds.chunks(2) {
        let mut sr = vec![(pair[0], pair[0] + pair[1])];
        let mut t = vec![];
        for map in &input.maps {
            t = vec![];
            for (start, end) in sr {
                t.append(&mut translate(start, end, map));
            }

            sr = t.clone()
        }
        locations.push(t.iter().min().unwrap().0);
    }
    *locations.iter().min().unwrap()
}

#[cfg(test)]
mod tests {
    // use super::{part1, part2};
}
