class Arr:
    def __init__(self):
        self.arr = [0] * 100
        self.size = 0

    def Append(self, value):
        self.arr[self.size] = value
        self.size += 1

    def Display(self):
        for a in range(self.size):
            print(self.arr[a])

    def Insert(self, index, value):   
#        for i in range(self.size, index + 1, -1):
#            self.arr[i+1] = self.arr[i]
#
#        self.arr[index] = value
#        self.size += 1 
        
        for i in range(self.size, index, -1):
            self.arr[i] = self.arr[i - 1]    

        self.arr[index] = value
        self.size += 1    
        

    def Delete_By_Index(self, index):
        for i in range(index, self.size - 1):
            self.arr[i] = self.arr[i + 1]

        self.size -= 1        

    def Delete_By_Value(self, value):
        for i in range(self.size):
            if self.arr[i] == value:
                for j in range(i, self.size - 1):
                    self.arr[j] = self.arr[j + 1]

                self.size -= 1
                return i
        return -1        


    def Search_By_Value(self, value):
        for i in range(self.size):
            if self.arr[i] == value:
                return i
            
        return -1
    
    def Reverse(self):
        for i in range(self.size // 2):
            temp = self.arr[i]
            self.arr[i] = self.arr[self.size - i - 1]
            self.arr[self.size - i - 1] = temp


marr = Arr()

marr.Append(2)
marr.Append(3)
marr.Append(7)
marr.Display()

print("/////////////////////////////")

val = marr.Search_By_Value(2)
print(val)

print("/////////////////////////////")

marr.Reverse()
marr.Display()

print("/////////////////////////////")

marr.Delete_By_Index(0)
marr.Display()

print("/////////////////////////////")

marr.Delete_By_Value(3)
marr.Display()

print("/////////////////////////////")

marr.Insert(0, 6)
marr.Display()

