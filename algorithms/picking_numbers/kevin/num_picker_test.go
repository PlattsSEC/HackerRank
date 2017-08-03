package numpicker

import "testing"

func TestNumPicker(t *testing.T) {
	question0 := NumPicker([]int{4, 6, 5, 3, 3, 1})
	question1 := NumPicker([]int{1, 2, 2, 3, 1, 2})

	if question0 != 3 {
		t.Error("Expected 5, got ", question0)
	}

	if question1 != 5 {
		t.Error("Expected 3, got ", question1)
	}
}
