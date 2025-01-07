import Stack

class Queue:
    def __init__(self):
        self.stack1 = Stack.Stack()
        self.stack2 = Stack.Stack()

    def EnQueue(self, item):
        self.stack1.Push(item)

    def DeQueue(self):
        while(not(self.stack1.IsEmpty())):
            first = self.stack1.Pop()
            self.stack2.Push(first)

        self.stack2.Pop()

        while(not(self.stack2.IsEmpty())):
            second = self.stack2.Pop()
            self.stack1.Push(second)
                                        

