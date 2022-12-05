use std::collections::VecDeque;
use std::fs::File;
use std::io::BufRead;

fn col_to_idx(col: usize) -> usize {
    col / 4
}

fn do_instruction(num: usize, from: usize, to: usize, stacks: &mut Vec<VecDeque<char>>) {
    let stack = &mut stacks[from];
    let drain: Vec<char> = stack.drain(stack.len() - num..).collect();

    let stack = &mut stacks[to];
    stack.extend(drain)
}

fn stack_msg(stacks: &Vec<VecDeque<char>>) -> String {
    let mut msg = String::new();
    for stack in stacks {
        msg.push(*stack.back().unwrap());
    }

    msg
}

fn _part2() -> std::io::Result<()> {
    let file = File::open("input")?;
    let mut reader = std::io::BufReader::new(file);

    let mut stacks: Vec<VecDeque<char>> = (0..9).map(|_| VecDeque::<char>::new()).collect();

    let mut line = String::new();
    loop {
        line.clear();
        reader.read_line(&mut line)?;
        if line.contains("1") {
            break;
        }

        let line_iter = (0..line.len())
            .zip(line.chars())
            .filter(|(_, c)| c.is_uppercase())
            .map(|(i, c)| (col_to_idx(i), c));
        
        for (i,c) in line_iter {
            stacks[i].push_front(c);
        }
    }

    reader.read_line(&mut line)?;

    loop {
        line.clear();
        if let Ok(0) = reader.read_line(&mut line) {
            break;
        }

        let instr: String = line.chars().filter(|c| !c.is_alphabetic()).collect();
        let instr: Vec<usize> = instr.split_whitespace().map(|s| s.parse::<usize>().unwrap()).collect();

        do_instruction(instr[0], instr[1] - 1, instr[2] - 1, &mut stacks);
    }

    println!("{}", stack_msg(&stacks));

    Ok(())
}

fn main() -> std::io::Result<()> {
    _part2()
}
