use std::io::{self, BufReader};
use std::io::prelude::*;
use std::fs::File;
use std::collections::HashMap;


pub fn day_one() -> io::Result<()> {
    let f = File::open("./inputs/1.txt")?;
    let f = BufReader::new(f);

    let mut left = Vec::new();
    let mut right = Vec::new();

    for line in f.lines() {
        let line = line?;
        let parts: Vec<&str> = line.split_whitespace().collect();

        if parts.len() != 2 {
            println!("nope");
            continue;
        }
        left.push(parts[0].to_string());
        right.push(parts[1].to_string());
        
    }
    

    let mut left_numeric: Vec<i32> = left
    .iter()
    .filter_map(|s| s.parse::<i32>().ok())
    .collect();

    left_numeric.sort();

    let mut right_numeric: Vec<i32> = right
    .iter()
    .filter_map(|s| s.parse::<i32>().ok())
    .collect();

    right_numeric.sort();

    part_one(&left_numeric, &right_numeric);
    part_two(&left_numeric, &right_numeric);


    Ok(())
    
}

fn part_one(left: &Vec<i32>, right: &Vec<i32>) {
    let mut total_distance = 0;
    for (i, l) in left.iter().enumerate() {
        let diff = l - right[i];
        total_distance += diff.abs();
    }

    println!("part one: {}", total_distance);
}

fn part_two(left: &Vec<i32>, right: &Vec<i32>) {
    let mut similarity = HashMap::new();
    for (_, l) in left.iter().enumerate() {
        let count = right.iter().filter(|&&x| x == *l).count();
        similarity.insert(l, count);
    }
    let mut total = 0;
    for (key, value) in similarity.into_iter() {
        total += key * value as i32;
    }
    
    println!("part two: {:?}", total);
}