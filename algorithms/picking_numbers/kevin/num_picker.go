package numpicker

import (
	"sort"
)

func NumPicker(list []int) int {
	sort.Ints(list)
	max := 0
	counter := 1
	listLength := len(list)
	for index := 0; index < listLength; index++ {
		for innerIndex := index + 1; innerIndex < listLength; innerIndex++ {
			difference := list[index] - list[innerIndex]
			if difference <= 0 {
				difference = -difference
			}
			if difference <= 1 {
				counter++
			} else {
				break
			}
		}
		if counter > max {
			max = counter
		}
		counter = 1
	}
	return max
}
