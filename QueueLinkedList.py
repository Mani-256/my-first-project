class list_node:
    def __init__(self, data = None, link = None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self.ind = 0
        self.first = None
    
    def InsertAtIndex(self, index, data):
        newnode = list_node(data)
        if index == 0:
            newnode.link = self.first
            self.first = newnode
        else:
            temp = self.first
            for i in range(index - 1):
                temp = temp.link
            newnode.link = temp.link
            temp.link = newnode
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

    def RemoveNodeAtIndex(self, index):
        data = 0
        if index == 0:
            data = self.first.data
            self.first = None
        else:
            temp = self.first
            for i in range(index - 1):
                temp = temp.link
            data = temp.link.data
            temp.link = temp.link.link
        self.ind -= 1

        return data

    def RemoveAtEnd(self):
        return self.RemoveNodeAtIndex(self.ind)

    def RemoveAtBegin(self):
        return self.RemoveNodeAtIndex(0)
    
    def SizeOfList(self):
        return self.ind
    
    def Concatenate(self, LinkedList2):
        if self.first == None:
            self.first = LinkedList2.first
        else:
            temp = self.first
            for i in range(self.ind - 1):
                temp = temp.link
            temp.link = LinkedList2.first

    def Invert(self):
        
        temp = self.first
        prev = None
        while temp:
            """prev = l
            l = l.link
            temp = l
            temp.link = prev"""
            l = temp.link
            temp.link = prev
            prev = temp
            temp = l

        #self.first.link = None
        self.first = prev
            

    def Display(self):
        temp = self.first
        while temp:
            print(temp.data)
            temp = temp.link

class QueueLinkedList:
    def __init__(self):
        pass

    linked_list = LinkedList()
    def Enqueue(self, data):
        self.linked_list.InsertAtEnd(data)

    def Dequeue(self):
        self.linked_list.RemoveAtBegin()
    
    def Show(self):
        self.linked_list.Display()
    
    def IsEmptyQ(self):
        return self.linked_list.SizeOfList() == 0