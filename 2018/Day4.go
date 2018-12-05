//usr/bin/env go run "$0" "$@"; exit
package main

import (
	"fmt"
	"io/ioutil"
	"sort"
	"strconv"
	"strings"
	"time"
)

// Day 4
// [1518-08-07 00:00] Guard #61 begins shift
// [1518-11-06 00:52] wakes up
// [1518-08-24 00:33] falls asleep

func main() {
	b, err := ioutil.ReadFile("inputs/4.txt")
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

type instruction struct {
	eventDate time.Time
	action    string
}

type guard struct {
	id        int
	mins      map[int]int
	totalTime int
}

func part1(lines []string) {
	instructions := make([]instruction, 0)
	// Process into instruction
	for _, line := range lines {
		fmt.Println(line)
		year, _ := strconv.Atoi("20" + line[strings.Index(line, " ")-2:strings.Index(line, " ")])
		month, _ := strconv.Atoi(line[strings.Index(line, "-")+1 : strings.Index(line, "-")+3])
		day, _ := strconv.Atoi(line[strings.Index(line, "-")+4 : strings.Index(line, "-")+6])
		hour, _ := strconv.Atoi(line[strings.Index(line, " ")+1 : strings.Index(line, " ")+3])
		min, _ := strconv.Atoi(line[strings.Index(line, " ")+4 : strings.Index(line, " ")+6])
		date := time.Date(year, time.Month(month), day, hour, min, 0, 0, time.UTC)
		instruction := instruction{date, line[strings.Index(line, "]")+2:]}
		instructions = append(instructions, instruction)
	}
	// Sort list on date
	sort.Slice(instructions, func(i, j int) bool {
		return instructions[i].eventDate.Before(instructions[j].eventDate)
	})

	var lastGuard guard
	guardInfo := make(map[int]guard)
	for i, element := range instructions {
		switch element.action {
		case "wakes up":
			// lastGuard
		case "falls asleep":
			if i < len(instructions) {
				if lastGuard.id == 0 {
					break
				}
				// lastGuard.totalTime +=
				nextEvent := instructions[i+1]
				if element.eventDate.Month() == nextEvent.eventDate.Month() && element.eventDate.Day() == nextEvent.eventDate.Day() {
					lastGuard.totalTime += int(nextEvent.eventDate.Sub(element.eventDate).Minutes())
				} else {
					lastGuard.totalTime += 60 - element.eventDate.Minute()
				}
				minToAdd := int(instructions[i+1].eventDate.Sub(element.eventDate).Minutes())
				j := instructions[i].eventDate.Minute()
				for j < minToAdd && j < 60 {
					//fmt.Println(lastGuard)
					lastGuard.mins[j]++
					j++
				}
				guardInfo[lastGuard.id] = lastGuard
			}
		default:
			//"Guard #61 begins shift"
			id, _ := strconv.Atoi(element.action[strings.Index(element.action, "#")+1 : strings.Index(element.action, "begins")-1])
			if _, ok := guardInfo[id]; !ok {
				guardInfo[id] = guard{id, make(map[int]int), 0}
			}
			lastGuard = guardInfo[id]
			//fmt.Println(lastGuard)
		}
	}
	var sleepTime int
	var sleepyGuard int
	var sleepyMin int
	// var sleepyMinTime int
	for _, v := range guardInfo {
		fmt.Println("guard")
		fmt.Println(v.id)
		totalMin := 0
		highestMinValue := 0
		highestMin := 0
		for k, min := range v.mins {
			totalMin += min
			if highestMinValue < min {
				fmt.Println("in here")
				fmt.Println(k)
				fmt.Println(min)
				highestMin = k
				highestMinValue = min
			}
		}
		if v.totalTime > sleepTime && v.id != 0 {
			fmt.Println(v)
			sleepyGuard = v.id
			sleepTime = v.totalTime
			sleepyMin = highestMin
			// sleepyMinTime = highestMinValue
		}
	}
	fmt.Println(sleepyGuard)
	fmt.Println(sleepyMin)
	fmt.Println("Part 1")
	fmt.Println(sleepyGuard * sleepyMin) // 947, 20834, 43455 too low

}
