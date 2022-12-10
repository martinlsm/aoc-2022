use std::fs::File;
use std::io::BufReader;
use std::io::BufRead;

fn parse_interval(s: &str) -> (usize, usize) {
    let dash_split = s.find('-').unwrap();

    let from = s[..dash_split].parse::<usize>().unwrap();
    let to = s[dash_split+1..].parse::<usize>().unwrap();

    (from, to)
}

fn _part1() -> std::io::Result<()> {
    let input_file = File::open("input")?;
    let mut res = 0;
   
    for line in BufReader::new(input_file).lines() {
        let line = line?;

        let comma_idx = line.find(',').unwrap();
        let (fst, snd) = line.split_at(comma_idx);
        let snd = &snd[1..];

        let (x0, x1) = parse_interval(fst);
        let (y0, y1) = parse_interval(snd);

        res += if (x0 <= y0 && x1 >= y1) || (y0 <= x0 && y1 >= x1) {
            1
        } else {
            0
        };
    }

    println!("{}", res);

    Ok(())
}

fn _part2() -> std::io::Result<()> {
    let input_file = File::open("input")?;
    let mut res = 0;
   
    for line in BufReader::new(input_file).lines() {
        let line = line?;

        let comma_idx = line.find(',').unwrap();
        let (fst, snd) = line.split_at(comma_idx);
        let snd = &snd[1..];

        let (x0, x1) = parse_interval(fst);
        let (y0, y1) = parse_interval(snd);

        res += if (x1 >= y0 && x0 <= y1) || (y1 >= x0 && y0 <= x1) {
            1
        } else {
            0
        };
    }

    println!("{}", res);

    Ok(())
}

fn main() -> std::io::Result<()> {
    _part2()
}
