#!/usr/bin/python3
# Kevin Boyette
# 1/11/2017


class TextEditor(object):

    def __init__(self):
        '''
        Class TextEditor

        Members:
                Input is a string
                Operation Stack is a stack of tuples,
                        ( <operation number, <appended/deleted string> )
        '''
        self.input = ''
        self.operation_stack = []

    def append(self, x: str):
        self.input += x
        self.operation_stack.append((1, x))

    def delete(self, k: int):

        self.operation_stack.append((2, self.input[-k:]))
        self.input = self.input[:-k]

    def print(self, k: int):
        print(self.input[:k])

    def undo(self):
        if len(self.operation_stack) == 0:
            return
        # Operation can be either 1 or 2
        # 1  == APPEND
        # 2  == DELETE
        operation, items = self.operation_stack.pop()
        if operation == 1:
            self.delete(len(items))

        else:
            self.append(items)

if __name__ == '__main__':
    q = int(input())
    textEditor = TextEditor()
    for each_iteration in range(q):
        line = input()

        operation = int(line[0])
        if operation == 1:
            textEditor.append(line.split()[1])
        elif operation == 2:
            textEditor.delete(int(line.split()[1]))
        elif operation == 3:
            textEditor.print(int(line.split()[1]))
        else:
            textEditor.undo()
