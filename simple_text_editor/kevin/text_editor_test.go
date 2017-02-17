package texteditor

import (
	"testing"
)

func TestTextEditor(t *testing.T) {
	text_editor := TextEditor{}

	input := "hello world"
	text_editor.append(input)
	text_editor.print(2)
	if text_editor.input != "hello world" {
		t.Errorf("Text Editor input != %v", input)
	}
	length := len(text_editor.op_stack)
	text_editor.delete(2)

	if text_editor.input != "hello wor" {
		t.Errorf("Testing Delete\nText Editor input != %v", input[:len(input)-2])
	}

	if len(text_editor.op_stack) != (length + 1) {
		t.Errorf("Text Editor Ops Stack Length Error Expected: %v != Actual: %v", length+1, len(text_editor.op_stack))
	}

	length = len(text_editor.op_stack)
	text_editor.undo()
	if text_editor.input != "hello world" {
		t.Errorf("Text Editor undo Expected: %v != Actual: %v", input, text_editor.input)
	}
	if len(text_editor.op_stack) != length {
		t.Errorf("Text Editor Ops Stack Length Error Expected: %v != Actual: %v", length, len(text_editor.op_stack))
	}

}
