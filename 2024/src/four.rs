use std::fs::File;
use std::io::prelude::*;
use std::io::{self, BufReader};

pub fn day_four() -> io::Result<()> {
    let f = File::open("./inputs/4.txt")?;
    let f = BufReader::new(f);

    let mut grid = Vec::new();

    for line in f.lines() {
        let line = line?;
        let parts = line.chars().collect();
        grid.push(parts)
    }

    // 1975 too low
    // 2291 too low
    part_one(grid.clone());

    part_two(grid);

    Ok(())
}

fn part_one(grid: Vec<Vec<char>>) {
    let mut found_count = 0;
    for (x, line) in grid.iter().enumerate() {
        for (y, character) in line.iter().enumerate() {
            // First, we only want to start searching on 'X'
            if *character == 'X' {
                found_count += check_horiztonal(line, y);

                found_count += check_vertical(grid.clone(), x, y);

                found_count += check_diagonal(grid.clone(), line, x, y);
            }
        }
    }
    println!("part one: {:?}", found_count);
}

fn check_horiztonal(line: &Vec<char>, start: usize) -> i32 {
    let mut count = 0;
    // go right
    if start + 3 < line.len() {
        if line[start + 1] == 'M' && line[start + 2] == 'A' && line[start + 3] == 'S' {
            count += 1;
        }
    }
    // go left
    if start > 2 {
        if line[start - 1] == 'M' && line[start - 2] == 'A' && line[start - 3] == 'S' {
            count += 1;
        }
    }
    return count;
}

fn check_vertical(grid: Vec<Vec<char>>, start_x: usize, y: usize) -> i32 {
    let mut count = 0;
    // go up
    if start_x > 2 {
        if grid[start_x - 1][y] == 'M' && grid[start_x - 2][y] == 'A' && grid[start_x - 3][y] == 'S'
        {
            count += 1;
        }
    }
    // go down
    if start_x + 3 < grid.len() {
        if grid[start_x + 1][y] == 'M' && grid[start_x + 2][y] == 'A' && grid[start_x + 3][y] == 'S'
        {
            count += 1;
        }
    }

    return count;
}

fn check_diagonal(grid: Vec<Vec<char>>, line: &Vec<char>, start_x: usize, start_y: usize) -> i32 {
    let mut count = 0;
    // go up
    if start_x > 2 {
        // go right
        if start_y + 3 < line.len() {
            if grid[start_x - 1][start_y + 1] == 'M'
                && grid[start_x - 2][start_y + 2] == 'A'
                && grid[start_x - 3][start_y + 3] == 'S'
            {
                count += 1;
            }
        }
        // go left
        if start_y > 2 {
            if grid[start_x - 1][start_y - 1] == 'M'
                && grid[start_x - 2][start_y - 2] == 'A'
                && grid[start_x - 3][start_y - 3] == 'S'
            {
                count += 1;
            }
        }
    }
    // go down
    if start_x + 3 < grid.len() {
        // go right
        if start_y + 3 < line.len() {
            if grid[start_x + 1][start_y + 1] == 'M'
                && grid[start_x + 2][start_y + 2] == 'A'
                && grid[start_x + 3][start_y + 3] == 'S'
            {
                count += 1;
            }
        }
        // go left
        if start_y > 2 {
            if grid[start_x + 1][start_y - 1] == 'M'
                && grid[start_x + 2][start_y - 2] == 'A'
                && grid[start_x + 3][start_y - 3] == 'S'
            {
                count += 1;
            }
        }
    }

    return count;
}

fn part_two(grid: Vec<Vec<char>>) {
    let mut found_count = 0;
    for (x, line) in grid.iter().enumerate() {
        for (y, character) in line.iter().enumerate() {
            // First, we only want to start searching on 'X'
            if *character == 'A' {
                if check_diagonal_part_two(grid.clone(), line, x, y) == 2 {
                    found_count += 1;
                };
            }
        }
    }
    println!("part two: {:?}", found_count);
}

fn check_diagonal_part_two(
    grid: Vec<Vec<char>>,
    line: &Vec<char>,
    start_x: usize,
    start_y: usize,
) -> i32 {
    let mut count = 0;
    // left to right
    if start_x > 0 && start_x + 1 < grid.len() && start_y > 0 && start_y + 1 < line.len() {
        let up_and_left = grid[start_x - 1][start_y - 1];
        let down_and_right = grid[start_x + 1][start_y + 1];
        // up and right should
        if (up_and_left == 'M' && down_and_right == 'S')
            || (down_and_right == 'M' && up_and_left == 'S')
        {
            count += 1;
        }
    }
    // right to left
    if start_x > 0 && start_x + 1 < grid.len() && start_y > 0 && start_y + 1 < line.len() {
        let up_and_right = grid[start_x - 1][start_y + 1];
        let down_and_left = grid[start_x + 1][start_y - 1];
        // up and right should
        if (up_and_right == 'M' && down_and_left == 'S')
            || (down_and_left == 'M' && up_and_right == 'S')
        {
            count += 1;
        }
    }

    return count;
}
