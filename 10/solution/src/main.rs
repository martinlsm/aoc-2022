use std::{collections::HashMap, fs::File, io::BufRead};

fn get_signal_strengh(clock_cycle: u64, signal_strengths: &HashMap<u64, i64>) -> i64 {
    let mut guess = clock_cycle;
    let mut res = None;

    while res.is_none() {
        match signal_strengths.get(&guess) {
            Some(x) => res = Some(*x * clock_cycle as i64),
            None => guess -= 1,
        }
    }

    res.unwrap()
}

fn get_pos(clock_cycle: u64, positions: &HashMap<u64, i64>) -> i64 {
    let mut guess = clock_cycle;
    let mut res = None;

    while res.is_none() {
        match positions.get(&guess) {
            Some(x) => res = Some(*x),
            None => {
                if guess == 0 {
                    res = Some(1);
                } else {
                    guess -= 1;
                }
            }
        }
    }

    res.unwrap()
}

fn _part1() -> std::io::Result<()> {
    let file = File::open("input")?;
    let reader = std::io::BufReader::new(file);

    let mut signal_strengths = HashMap::<u64, i64>::new();
    let mut clock_cycle: u64 = 1;
    let mut reg_x: i64 = 1;

    for line in reader.lines() {
        let line = line?;
        let mut split = line.split(" ");
        let cmd = split.next().unwrap();
        let val = split.next().map(|x| x.parse::<i64>().unwrap());

        match cmd {
            "addx" => {
                clock_cycle += 2;
                let val = val.unwrap();
                reg_x += val;
                signal_strengths.insert(clock_cycle, reg_x);
            }
            "noop" => clock_cycle += 1,
            _ => (),
        }
    }

    let res = (20..221)
        .step_by(40)
        .map(|x| {
            let sig_str = get_signal_strengh(x, &signal_strengths);
            sig_str
        })
        .fold(0, |a, b| a + b);

    println!("{}", res);

    Ok(())
}

fn _part2() -> std::io::Result<()> {
    let file = File::open("input")?;
    let reader = std::io::BufReader::new(file);

    let mut position_map = HashMap::<u64, i64>::new();
    let mut clock_cycle: u64 = 0;
    let mut sprite_pos: i64 = 1;

    for line in reader.lines() {
        let line = line?;
        let mut split = line.split(" ");
        let cmd = split.next().unwrap();
        let val = split.next().map(|x| x.parse::<i64>().unwrap());

        match cmd {
            "addx" => {
                clock_cycle += 2;
                let val = val.unwrap();
                sprite_pos += val;
                position_map.insert(clock_cycle, sprite_pos);
            }
            "noop" => clock_cycle += 1,
            _ => (),
        }
    }

    let positions = (0..clock_cycle).map(|x| {
        let pos = get_pos(x, &position_map);
        pos
    });

    let mut crt: Vec<Vec<char>> = Vec::new();
    for _ in 0..6 {
        let mut inner = Vec::new();
        for _ in 0..40 {
            inner.push(' ');
        }
        crt.push(inner);
    }

    for (cycle, sprite_pos) in positions.enumerate() {
        let (draw_row, draw_col) = ((cycle / 40) % 6, cycle % 40);
        if (sprite_pos - 1..sprite_pos + 2).contains(&(draw_col as i64)) {
            crt[draw_row][draw_col] = '█';
        }
    }

    for row in &crt {
        for c in row {
            print!("{}", c);
        }
        println!();
    }

    Ok(())
}

fn main() -> std::io::Result<()> {
    _part1()?;
    _part2()?;

    Ok(())
}
