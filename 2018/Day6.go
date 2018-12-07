//usr/bin/env go run "$0" "$@"; exit
package main

import (
	"fmt"
	"io/ioutil"
	"strings"
	"unicode"
)

// Day 6

func main() {
	b, err := ioutil.ReadFile("inputs/5.txt")
	if err != nil {
		fmt.Print(err)
	}
	inputText := string(b)
	lines := strings.Split(inputText, "\n")
	// test := "test"
	// fmt.Println(test[0:1] + test[2+1:])
	// Part 1
	part1(lines)

	part2(lines)
}

func part1(lines string[]){

}

func part2(lines string[]){
	
}
