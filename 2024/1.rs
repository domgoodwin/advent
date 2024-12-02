use std::io::{self, BufReader};
use std::io::prelude::*;
use std::fs::File;


fn main() -> io::Result<()> {
    let f = File::open("./inputs/1")?;
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

    let mut total_distance = 0;
    for (i, l) in left_numeric.iter().enumerate() {
        let diff = l - right_numeric[i];
        total_distance += diff.abs();
    }

    println!("{}", total_distance);

    Ok(())
    
}