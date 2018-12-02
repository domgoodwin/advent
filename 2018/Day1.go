//usr/bin/env go run "$0" "$@"; exit
package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {
	b, err := ioutil.ReadFile("inputs/1.txt")
	if err != nil {
		fmt.Print(err)
	}
	inputText := string(b)
	// fmt.Println(inputText)

	lines := strings.Split(inputText, "\n")
	i := 0
	// PART 1 - resulting frequency
	var freq int64
	for i < len(lines) {
		mod, err := strconv.ParseInt(lines[i], 10, 64)
		if err != nil {
			fmt.Print(err)
		}
		freq += mod
		i++
	}
	fmt.Println("Part 1")
	fmt.Println(freq)

	// PART 2 - Same freq twice
	i = 0
	freq = 0
	freqs := make(map[int64]int)
	found := false
	freqs[freq] = 1
	for !found {
		mod, err := strconv.ParseInt(lines[i], 10, 64)
		if err != nil {
			fmt.Print(err)
		}
		freq += mod
		if freqs[freq] != 0 && !found {
			fmt.Println("Part 2") // 520 too low
			fmt.Println(freq)
			found = true
		}
		freqs[freq] = 1
		i++
		if i >= len(lines) {
			i = 0
		}
	}
}
