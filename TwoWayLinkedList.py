class list_node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None

class TwoWayLinkedList:
    def __init__(self):
        self.ind = 0
        self.first = None
        self.last = None
    
    def InsertAtIndex(self, index, data):
        newnode = list_node(data)
        if index == 0:
            if self.first == None:
                self.first = newnode
                self.last = newnode
            else: 
                newnode.next = self.first
                self.first.prev = newnode
                self.first = newnode
        elif index == self.ind:
            newnode.prev = self.last
            self.last.next = newnode
            self.last = newnode
            
        else:
            temp = self.first
            for i in range(index - 1):
                temp= temp.next
            newnode.next = temp.next
            newnode.prev = temp
            temp.next.prev = newnode
            temp.next = newnode

        self.ind += 1


    def InsertAtEnd(self, data):
        self.InsertAtIndex(self.ind, data)

    def InsertAtBegin(self, data):
        self.InsertAtIndex(0, data)

    def UpdateNode(self, index, data):
        temp = self.first
        for i in range(index - 1):
            temp = temp.link
        temp.link.data = data

    def RemoveAtIndex(self, index):
        if self.ind == 1:
            data = self.first.data
            self.first = None
            self.last = None


        elif index == 0:
            data = self.first.data
            self.first = self.first.next
            self.first.prev = None

        elif index == self.size - 1:
            data = self.last.data
            self.last = self.last.prev
            self.last.next = None


        else:
            temp = self.first
            for i in range(index):
                temp = temp.next
            data = temp.data
            temp.prev.next = temp.next
            temp.next.next = temp.prev

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
            self.last = LinkedList2.last
        else:
            self.last.next = LinkedList2.first
            LinkedList2.first.prev = self.last
            self.last = LinkedList2.last

        self.ind += LinkedList2.ind
