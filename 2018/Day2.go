//usr/bin/env go run "$0" "$@"; exit
package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

//Day 2
// counting the number that have an ID containing exactly two of any
// letter and then separately counting those with exactly three of any letter.
// You can multiply those two counts together to get a rudimentary checksum and compare it to what your device predicts.

func main() {
	b, err := ioutil.ReadFile("inputs/2.txt")
	if err != nil {
		fmt.Print(err)
	}
	inputText := string(b)
	// fmt.Println(inputText)
	lines := strings.Split(inputText, "\n")
	// fmt.Println(lines)

	// Part 1
	part1(lines)

	part2(lines)
}

func part1(lines []string) {
	i := 0
	var twoCount, threeCount int
	for i < len(lines) {
		chars := make(map[rune]int)
		for _, r := range lines[i] {
			chars[r]++
		}
		var twoDone, threeDone bool
		for _, v := range chars {
			// fmt.Println("k:", k, "v:", v)
			if v == 2 && !twoDone {
				twoCount++
				twoDone = true
			} else if v == 3 && !threeDone {
				threeCount++
				threeDone = true
			}
		}
		i++
	}
	fmt.Println("Part 1")
	fmt.Println(twoCount * threeCount)
}

func part2(lines []string) {
	cPos := 0
	for cPos < 26 {
		ids := make(map[string]int)
		i := 0
		for i < len(lines) {
			// fmt.Println(lines[i])
			// fmt.Println(lines[i][0:cPos] + lines[i][cPos+1:])
			if ids[lines[i][0:cPos]+lines[i][cPos+1:]] == 0 {
				ids[lines[i][0:cPos]+lines[i][cPos+1:]] = 1
			} else {
				fmt.Println("Part 2")
				fmt.Println(lines[i][0:cPos] + lines[i][cPos+1:])
				return
			}
			i++
		}
		cPos++
	}
}
