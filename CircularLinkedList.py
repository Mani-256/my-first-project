class list_node:
    def __init__(self, data = None):
        self.data = data
        self.link = None

class CircularLinkedList:
    def __init__(self):
        self.ind = 0
        self.first = None

    def InsertAtIndex(self, index, data):
        newnode = list_node(data)
        if index == 0:
            if self.first == None:
                newnode.link = newnode
                self.first = newnode
            else:
                temp = self.first
                for i in range(index - 1):
                    temp = temp.link
                newnode.link = temp.link
                temp.link = newnode
            
        else:
            temp = self.first
            for i in range(index - 1):
                temp = temp.link

            newnode.link = temp.link
            temp.link = newnode

        self.ind += 1

    def InsertAtEnd(self, data):
        self.InsertAtIndex(self.ind, data)

    def InsertArBegin(self, data):
        self.InsertAtIndex(0, data)

    def UpdateNode(self, index, data):
        temp = self.first
        for i in range(index - 1):
            temp = temp.link
        temp.link.data = data

    def RemoveAtIndex(self, index):
        data = 0
        if self.SizeOfIndex == 1:
            data = self.first.data
            self.first = None
        else:
            temp = self.first
            for i in range(index -1):
                temp = temp.link
            data = temp.link.data
            temp.link = temp.link.link

        self.ind -= 1
        return data

    def RemoveAtEnd(self):
        return self.RemoveAtIndex(self.ind)

    def RemoveAtBegin(self):
        return self.RemoveAtIndex(0)

    def SizeOfIndex(self):
        return self.ind

    def Concatenate(self, LinkedList2):
        if self.first == None:
            self.first = LinkedList2.first
        else:
            temp1 = self.first
            while temp1.link != self.first:
                temp1 = temp1.link
            temp1.link = LinkedList2.first

            temp2 = LinkedList2.first
            while temp2.link != LinkedList2.first:
                temp2 = temp2.link
            temp2.link = self.first
        
        self.ind += LinkedList2.ind

    def Invert(self):
        temp = self.first
        prev = None
        while True:
            l = temp.link
            temp.link = prev
            prev = temp
            temp = l
            if temp == self.first:
                break
        self.first = prev

    def Display(self):
        temp = self.first
        for i in range(self.ind):
            print(temp.data)
            temp = temp.link


cll = CircularLinkedList()
cll.InsertAtEnd(1)
cll.InsertAtEnd(2)
cll.InsertAtEnd(3)
cll.InsertAtEnd(4)
cll.Display()