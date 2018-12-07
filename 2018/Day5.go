//usr/bin/env go run "$0" "$@"; exit
package main

import (
	"fmt"
	"io/ioutil"
	"strings"
	"unicode"
)

// Day 5

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

type result struct {
	line     string
	finished bool
}

func part1(lines []string) {
	fmt.Println("Part 1")
	fmt.Println(len(react(lines[0]))) // 8706 too low
}

func part2(lines []string) {
	fmt.Println("Part 2")
	units := "abcdefghijklmnopqrstuvwqyz"
	length := -1
	for _, char := range units {
		line := lines[0]
		fmt.Println("Replacing: ")
		fmt.Println(string(char))
		line = strings.Replace(line, string(char), "", -1)
		line = strings.Replace(line, string(unicode.ToUpper(char)), "", -1)
		reactLength := len(react(line))
		fmt.Println(reactLength)
		if length == -1 || reactLength < length {
			length = reactLength
		}
	}
	fmt.Println(length)
}

func react(line string) string {
	finished := false
	for !finished {
		line, finished = parseLine(line)
	}
	return line
}

func parseLine(line string) (string, bool) {
	newLine := ""
	for i, char := range line {
		if i+1 < len(line) &&
			unicode.ToLower(rune(line[i+1])) == unicode.ToLower(char) &&
			(unicode.IsLower(rune(line[i+1])) == unicode.IsUpper(char) || unicode.IsUpper(rune(line[i+1])) == unicode.IsLower(char)) {

			newLine = line[0:i] + line[i+2:]
			return newLine, false
		}
	}
	return line, true

}
