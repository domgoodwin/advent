package main

import (
    "fmt"
    "io/ioutil"
    "strconv"
    "math"
)

// Day 3
// Amount per loop
// increases up to next square
// Input is 325489

type Coordinate struct {
  X, Y float64
}

func main() {
    // Reading it in from a file to learn how
    b, err := ioutil.ReadFile("inputs/day3.txt")
    if err != nil {
        fmt.Print(err)
    }
    //fmt.Println(b)
    inputText := string(b)
    fmt.Println(inputText)

    // Work out which ring the number is on
    // Converts string to int, base 10, 0means 64bit int
    //goalNumber, _ := strconv.ParseInt(inputText, 10, 8)
    goalNumber, _ := strconv.ParseFloat(inputText, 64)
    var max float64 = 0

    var side int = 1
    for max < goalNumber {
      max = math.Pow(float64(side), 2)
      // fmt.Print(i)
      // fmt.Print("\n")
      // fmt.Print(max)
      // fmt.Print("\n")
      side++
    }
    //fmt.Print(max)
    var back int = int(max) - int(goalNumber)
    var fullSidesBack int = back / side
    fmt.Printf("The number is %v full sides back\n", fullSidesBack)
    fmt.Printf("Side length is %v\n", side)
    var location Coordinate
    location = Coordinate{X: float64(side - (back * (fullSidesBack + 1))),Y: float64(side)}
    fmt.Printf("The coordinates of the number are: %v\n", location)
    midPoint := Coordinate{X: float64((side + 1) / 2), Y: float64((side + 1) / 2)}
    distance := math.Abs(location.X - midPoint.X) + math.Abs(location.Y - midPoint.Y)
    fmt.Printf("The distance between the points is %v\n", distance)




}
