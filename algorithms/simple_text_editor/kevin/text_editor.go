package texteditor

import "fmt"

type Operation struct {
	op        int
	input_str string
}

type TextEditor struct {
	input    string
	op_stack []Operation
}

func (t *TextEditor) append(str string) {
	t.input += str
	t.op_stack = append(t.op_stack, Operation{op: 1, input_str: str})
}

func (t *TextEditor) delete(k int) {
	t.op_stack = append(t.op_stack, Operation{op: 2, input_str: t.input[len(t.input)-k:]})
	t.input = t.input[:len(t.input)-k]
}

func (t *TextEditor) print(k int) {
	fmt.Println(t.input[:len(t.input)-k])
}

func (t *TextEditor) undo() {
	if len(t.op_stack) == 0 {
		return
	}
	operation := t.op_stack[len(t.op_stack)-1]
	t.op_stack = t.op_stack[:len(t.op_stack)-1]
	if operation.op == 1 {
		t.delete(len(operation.input_str))
	} else {
		t.append(operation.input_str)
	}

	fmt.Println(t.op_stack)
}
