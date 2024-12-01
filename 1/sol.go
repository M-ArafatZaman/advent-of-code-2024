package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func getInput(filename string) ([]int, []int) {
	f, _ := os.ReadFile(filename)

	var arr1 []int
	var arr2 []int

	for _, i := range strings.Split(string(f), "\n") {
		fields := strings.Fields(i)
		num1, _ := strconv.Atoi(fields[0])
		num2, _ := strconv.Atoi(fields[1])
		arr1 = append(arr1, num1)
		arr2 = append(arr2, num2)
	}

	return arr1, arr2
}

func main() {
	arr1, arr2 := getInput("data.txt")
	sort.Ints(arr1)
	sort.Ints(arr2)

	// Part 1
	var total int
	for i := range arr1 {
		total += abs(arr1[i] - arr2[i])
	}
	fmt.Println("Part 1:", total)

	// Part 2
	counts := make(map[int]int)
	for _, num := range arr2 {
		counts[num]++
	}
	var score int
	for _, elem := range arr1 {
		score += elem * counts[elem]
	}
	fmt.Println("Part 2:", score)
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
