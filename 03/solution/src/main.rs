use std::collections::HashSet;
use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;

fn priority(item: char) -> i32 {
    let res: i32;
    if item.is_lowercase() {
        res = (item as i32) - ('a' as i32) + 1;
    } else {
        res = (item as i32) - ('A' as i32) + 27;
    }

    res
}

fn _part1() -> std::io::Result<()> {
    let file = File::open("input")?;
    let mut res = 0;

    for line in BufReader::new(file).lines().map(|x| x.unwrap()) {
        assert!(line.len() % 2 == 0);

        let split_idx = line.len() / 2;
        let p1 = &line[..split_idx];
        let p2 = &line[split_idx..];

        let p1_items: HashSet<char> = HashSet::from_iter(p1.chars());
        let p2_items: HashSet<char> = HashSet::from_iter(p2.chars());
        let shared_item = *HashSet::intersection(&p1_items, &p2_items).next().unwrap();
        res += priority(shared_item);
    }

    println!("{}", res);

    Ok(())
}

fn read_three_lines(it: &mut impl Iterator<Item = String>) -> Option<(String, String, String)> {
        let s1 = it.next();
        match s1 {
            Some(_) => (),
            None => return None,
        }
        let s1 = s1.unwrap();
        let s2 = it.next().unwrap();
        let s3 = it.next().unwrap();

        Some((s1, s2, s3))
}

fn _part2() -> std::io::Result<()> {
    let file = File::open("input")?;
    let mut res = 0;

    let mut file_iter = BufReader::new(file).lines().map(|s| s.unwrap());

    loop {
        let lines = read_three_lines(&mut file_iter);
        match lines {
            None => break,
            Some(_) => (),
        }
        let (s1, s2, s3) = lines.unwrap();

        let s1_items: HashSet<char> = HashSet::from_iter(s1.chars());
        let s2_items: HashSet<char> = HashSet::from_iter(s2.chars());
        let s3_items: HashSet<char> = HashSet::from_iter(s3.chars());

        let tmp_intersection: HashSet<char> = HashSet::from_iter(HashSet::intersection(&s1_items, &s2_items).map(|&x| x));
        let badge = *HashSet::intersection(&s3_items, &tmp_intersection).next().unwrap();

        res += priority(badge);
    }

    println!("{}", res);

    Ok(())
}

fn main() -> std::io::Result<()> {
    _part2()
}
