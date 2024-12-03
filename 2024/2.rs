use std::io::{self, BufReader};
use std::io::prelude::*;
use std::fs::File;


fn main() -> io::Result<()> {
    let f = File::open("./inputs/2.txt")?;
    let f = BufReader::new(f);

    let mut reports = Vec::new();

    for line in f.lines() {
        let line = line?;
        let parts: Vec<&str> = line.split_whitespace().collect();

        let levels: Vec<i32> = parts
        .iter()
        .filter_map(|s| s.parse::<i32>().ok())
        .collect();
        reports.push(levels)
        
    }

    part_one(reports.clone());

    // 943 too high
    // 458 too low
    // 820 too high
    part_two(reports);

    Ok(())
    
}

fn part_two(reports: Vec<Vec<i32>>) {
    let mut safe_count = 0;
    for report in reports.iter() {
        if is_safe(report) {
            safe_count += 1;
            continue;
        } 
        // We're not safe in it's current form, so lets try removing numbers to see
        // it's not very efficient doing this for every number in the list but oh well
        
        for (i, _level) in report.iter().enumerate() {
            let mut report_copy = report.clone();
            report_copy.remove(i);
            if is_safe(&report_copy) {
                safe_count += 1;
                // removing 1 element makes it safe, so lets stop checking
                break;
            } 
        }
    }
    println!("part two: {}", safe_count);
}

fn part_one(reports: Vec<Vec<i32>>) {
    let mut safe_count = 0;
    for report in reports.iter() {
        if is_safe(report) {
            safe_count += 1;
        }
    }
    println!("part one: {}", safe_count);
}

fn is_safe(report: &Vec<i32>) -> bool  {
    let mut increasing = false;
    let mut decreasing = false;
    let mut diff_too_large = false;
    let mut previous_number = -1;
    for level in report.iter() {
        let level = *level;
        // if we aren't on our first iteration
        if previous_number != -1 {
            if level > previous_number {
                increasing = true;
            } else if level < previous_number {
                decreasing = true;
            }
            
            let diff = level - previous_number;
            if level == previous_number || diff.abs() > 3 {
                diff_too_large = true;
            }
        }
        previous_number = level;
    }

    // XOR
    return increasing ^ decreasing && !diff_too_large
}