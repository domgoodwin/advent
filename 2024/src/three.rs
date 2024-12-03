use std::fs;
use regex::Regex;

pub fn day_three() {
    let data = fs::read_to_string("./inputs/3.txt").expect("Unable to read file");
    part_one(data.clone());
    part_two(data);
}


fn part_one(data: String) {
    let re: Regex = Regex::new("mul\\([0-9]+,[0-9]+\\)").unwrap();
    let mut total = 0;
     for mat in re.find_iter(&data) {
        let to_split = mat.as_str().replace("mul(", "");
        let to_split = to_split.replace(")", "");
        let parts: Vec<&str> = to_split.split(",").collect();
        let left =  parts[0].parse::<i32>().unwrap();
        let right =  parts[1].parse::<i32>().unwrap();
        
        total += left * right;
     }
     println!("part one: {}", total);
}


fn part_two(data: String) {
    let re: Regex = Regex::new("(mul\\([0-9]+,[0-9]+\\)|do\\(\\)|don't\\(\\))").unwrap();
    let mut total = 0;
    let mut enabled = true;
     for mat in re.find_iter(&data) {
        if mat.as_str().contains("mul") {
            if !enabled{
                continue;
            }
            let to_split = mat.as_str().replace("mul(", "");
            let to_split = to_split.replace(")", "");
            let parts: Vec<&str> = to_split.split(",").collect();
            let left =  parts[0].parse::<i32>().unwrap();
            let right =  parts[1].parse::<i32>().unwrap();
            total += left * right;
        }
        if mat.as_str().contains("don") {
            enabled = false;
        } else if mat.as_str().contains("do") {
            enabled = true;
        }

     }
     println!("part two: {}", total);
}