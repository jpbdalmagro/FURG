class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.start = None
        self.end = None


    def empty(self):
        return self.start == None
    

    def insert(self, value):
        new = Node(value)
        
        if self.empty():
            self.ini = new
        
        else:
            self.end.next = new
        
        self.end = new

    
    def remove(self):
        if not self.empty():
            self.start = self.start.next

    def destroy(self):
        while not self.empty():
            self.remove()
