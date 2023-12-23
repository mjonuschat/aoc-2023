use aoc_runner_derive::*;

fn hsh(step: &str) -> usize {
    step.as_bytes()
        .iter()
        .fold(0usize, |a, i| ((a + *i as usize) * 17) % 256)
}
#[aoc(day15, part1)]
pub fn part1(input: &str) -> usize {
    input.trim().split(',').map(hsh).sum()
}

#[aoc(day15, part2)]
pub fn part2(input: &str) -> usize {
    let mut boxes = vec![Vec::new(); 256];

    for step in input.trim().split(',') {
        if step.contains('=') {
            let (label, lens) = step.split_once('=').unwrap();
            let b = &mut boxes[hsh(label)];
            let lens: usize = lens.parse().unwrap();

            match b.iter().position(|&(l, _)| l == label) {
                Some(i) => b[i] = (label, lens),
                None => b.push((label, lens)),
            }
        } else {
            let label = &step[..step.len() - 1];
            let b = &mut boxes[hsh(label)];
            if let Some(i) = b.iter().position(|&(l, _)| l == label) {
                b.remove(i);
            }
        }
    }

    (0..boxes.len())
        .flat_map(|b| (0..boxes[b].len()).map(move |l| (b, l)))
        .map(|(b, l)| (b + 1) * (l + 1) * boxes[b][l].1)
        .sum()
}

#[cfg(test)]
mod tests {
    // use super::{part1, part2};
}
