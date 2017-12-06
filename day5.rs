use std::env;
use std::fs::File;
use std::io::prelude::*;

fn main() {
    day5();

}

fn day5() {
    const INPUT: &str = include_str!("inputs/day5.txt");
    let run = |i: &str| {
        let mut c = i.lines().filter_map(|a| a.parse::<i32>().ok())
                     .collect::<Vec<_>>();
        let mut counter = 0;
        let mut index: i32 = 0;
        while let Some(i) = c.get_mut(index as usize) {
            index += *i;
            // Part 1:
            // *i += 1;
            // Part 2:
            if *i >= 3 { *i -= 1; } else { *i += 1; }
            counter += 1;
        }
        println!("{}: {}",index, counter);
    };
    run(INPUT);
}

//OLD METHOD
// let filename = "inputs/day5.txt";
// println!("In file {}", filename);
//
// let mut f = File::open(filename).expect("file not found");
//
// let mut contents = String::new();
// f.read_to_string(&mut contents)
//     .expect("something went wrong reading the file");
//
// //println!("With text:\n{}", contents);
//
// //println!(contents);
//
// let mut instructions = contents
//     .split('\n').map(|s| s.trim())
//     .filter(|s| !s.is_empty())
//     .map(|x| x.trim().parse().unwrap())
//     .collect::<Vec<i32>>();
// //let intStruction: Vec<i32> = instructions.iter().map(| x | x..parse().unwrap()).collect::<Vec<i32>>();
//
// let mut pos: usize  = 0;
// let mut steps: i32 = 0;
// // for i in instructions{
// //     //println!("Number: {}", i);
// // }
// let length: usize = instructions.len();
// while pos < length{
//     steps += 1;
//     println!("num:{}", steps);
//     //let condition = instructions[pos] + pos as i32 > instructions.len() as i32;
//     //let mut item = ;
//     println!("num2:{}", instructions[pos]);
//     instructions[pos] = instructions[pos] + 1 ;
//     pos = pos + instructions[pos] as usize;
//     //x = x + instructions[x] if condition else instructions.len() + 1;
// }
// println!("[PART1] : number of steps taken={}", steps)
//
