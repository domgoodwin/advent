use std::env;
mod one;
use one::day_one;
mod two;
use two::day_two;
mod three;
use three::day_three;


fn main() {
    let args: Vec<String> = env::args().collect();
    let day = &args[1];
    if day == "1" {
        let _ = day_one();
    }
    if day == "2" {
        let _ = day_two();
    }
    if day == "3" {
        day_three();
    }
}
