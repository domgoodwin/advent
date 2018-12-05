//usr/bin/env go run "$0" "$@"; exit
package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

// Day 3
// See overlapping grid
// #13 @ 357,389: 22x23
// #ID @ from-left,from-top: widthXheight

func main() {
	b, err := ioutil.ReadFile("inputs/3.txt")
	if err != nil {
		fmt.Print(err)
	}
	inputText := string(b)
	// fmt.Println(inputText)
	lines := strings.Split(inputText, "\n")
	// fmt.Println(lines)

	// Part 1
	part1(lines)

	//part2(lines)
}

type coord struct {
	x int64
	y int64
}

type gridValue struct {
	count int64
	id    string
}

func part1(lines []string) {
	grid := make(map[coord]gridValue)
	for _, line := range lines {
		id := line[1 : strings.Index(line, "@")-1]
		fromLeft, err := strconv.ParseInt(line[strings.Index(line, "@")+2:strings.Index(line, ",")], 10, 64)
		if err != nil {
			fmt.Println(err)
		}
		fromTop, _ := strconv.ParseInt(line[strings.Index(line, ",")+1:strings.Index(line, ":")], 10, 64)
		width, _ := strconv.ParseInt(line[strings.Index(line, ":")+2:strings.Index(line, "x")], 10, 64)
		height, _ := strconv.ParseInt(line[strings.Index(line, "x")+1:], 10, 64)
		startCoord := coord{fromLeft, fromTop}
		fmt.Println(line)
		grid = fillGrid(startCoord, width, height, id, grid)
	}
	overlapCount := 0

	for _, v := range grid {
		// fmt.Println("k:", k, "v:", v)
		if v.count >= 2 {
			overlapCount++
		}
	}
	// fmt.Println(grid)
	fmt.Println("Part 1")
	fmt.Println(overlapCount) // 998, 26109, 93243 too low

	fmt.Println("Part 2") // 490 too low
	validIDs := make(map[string]int)
	invalidIDs := make(map[string]int)
	for _, v := range grid {
		if v.count == 1 && invalidIDs[v.id] != 1 {
			validIDs[v.id] = 1
		} else {
			invalidIDs[v.id] = 1
		}
	}
	for k, v := range validIDs {
		if invalidIDs[k] == 1 {
			// fmt.Println("Invalid:" + k)
			// fmt.Println(v)
		} else {
			fmt.Println("Valid:" + k)
			fmt.Println(v)
		}
	}
	printGrid(grid)
}
func fillGrid(startCoord coord, width int64, height int64, id string, grid map[coord]gridValue) map[coord]gridValue {
	newGrid := grid
	var x, y int64
	// fmt.Println(startCoord)
	// fmt.Println(width)
	// fmt.Println(height)
	for x = 0; x < width; x++ {
		for y = 0; y < height; y++ {
			posCoord := startCoord
			posCoord.y += y
			posCoord.x += x
			// fmt.Println(posCoord)
			// fmt.Println(newGrid[posCoord])
			val := newGrid[posCoord]
			val.count++
			val.id = id
			newGrid[posCoord] = val
		}
	}
	//fmt.Println(newGrid)
	return newGrid
}

func printGrid(grid map[coord]gridValue) {
	var maxX, maxY int64
	for k, _ := range grid {
		if k.x > maxX {
			maxX = k.x
		}
		if k.y > maxY {
			maxY = k.y
		}
	}
	var x, y int64
	lines := make([]string, 0)
	for x = 0; x < maxX; x++ {
		line := ""
		for y = 0; y < maxY; y++ {
			line += strconv.FormatInt(grid[coord{x, y}].count, 10)
		}
		line += "\n"
		lines = append(lines, line)
	}
	fmt.Println(lines)
}
