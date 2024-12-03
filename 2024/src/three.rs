use std::fs;
use regex::Regex;

pub fn day_three() {
    let data = fs::read_to_string("./inputs/3.txt").expect("Unable to read file");

    let re: Regex = Regex::new("mul\\([0-9]+,[0-9]+\\)").unwrap();
    if let Some(mat) = re.find(data) {
        println!("{}", mat.as_str())
     }

    
}
