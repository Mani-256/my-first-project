class Stack:
    def __init__(self):
        self.top = -1
        self.arr = [None] * 100

    def IsEmpty(self):
        return self.top == -1
    
    def Push(self, item):
        self.top += 1
        self.arr[self.top] = item

    def Pop(self):
        if self.IsEmpty():
            #print("Stack is Empty. Nothing to Pop!")
            return None
        r = self.arr[self.top]
        self.top -= 1
        return r
    
    def Peek(self):
        if self.IsEmpty():
            #print("Stack is Empty. Nothing to Display!")
            return None
        return self.arr[self.top]
    
def main():
    stack1 = Stack()
    stack1.Push(10)
    stack1.Push(20)
    stack1.Push(30)
    stack1.Push(40)
    print("Peek is", stack1.Peek())
    stack1.Pop()
    print("Peek after pop is", stack1.Peek())
    stack1.Pop()
    print("Peek after pop is", stack1.Peek())


if __name__ == "__main__":
    main()    