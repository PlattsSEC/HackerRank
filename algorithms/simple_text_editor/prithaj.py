Q = input()

class Stack:
    def __init__(self):
        self.stack = []
        self.undo_stack = []
        self.delete_tray = []
    def append(self,data):
        self.stack.extend(list(data))
        self.undo_stack.append(('append',data))
    def delete(self,k):
        count = k
        some_list = []
        while count > 0:
            some_list.append(self.stack.pop())
            count -=1
        self.delete_tray.append(some_list)
        self.undo_stack.append(('delete',k))
    def printString(self,k):
        print "".join(self.stack)[k-1]
    def undo(self):
        query,val = self.undo_stack.pop()
        if query == 'append':
            count = len(val)
            while count > 0:
                self.stack.pop()
                count -=1
        elif query == 'delete':
            count = val
            data = self.delete_tray.pop()
            while count > 0:
                self.stack.append(data.pop())
                count -=1

my_stack = Stack()  

for i in range(Q):
    x = raw_input()
    if x[0] == '1':
        b = x.split()[1]
        my_stack.append(b)
    elif x[0] == '2':
        k = int(x.split()[1])
        my_stack.delete(k)
    elif x[0] == '3':
        k = int(x.split()[1])
        my_stack.printString(k)
    elif x[0] == '4':
        my_stack.undo()