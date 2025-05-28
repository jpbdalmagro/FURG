class Queue:
    def __init__(self, size):
        self.vector = [None] * size
        self.sup_limit = size - 1
        self.inf_limit = 0
        self.start = self.inf_limit - 1
        self.end = self.sup_limit + 1

    
    def empty(self):
        return self.start < self.inf_limit and self.end > self.sup_limit
    

    def full(self):
        return self.start == self.sup_limit and self.end == self.inf_limit or self.start - 1 == self.end
    

    def insert(self, value):
        if self.empty():
            self.start += 1
            self.end = self.start
            self.vector[self.start] = value
            return True
        
        elif self.full():
            return False
        
        elif self.end == self.sup_limit:
            self.end = self.inf_limit
            self.vector[self.end] = value
            return True
        
        else:
            self.end += 1
            self.vector[self.end] = value
            return True
        

    def remove(self):
        if self.empty():
            return False
        
        elif self.end == self.start:
            self.destroy()

        elif self.start == self.sup_limit:
            self.vector[self.start] = None
            self.start = self.inf_limit
            return True
            
        else:
            self.vector[self.start] = None
            self.start += 1
            return True
        

    def destroy(self):
        self.vector[self.end] = None
        self.start = self.inf_limit - 1
        self.end = self.sup_limit + 1
        return True    


    def print(self):
        for i in self.vector:
            print(i)
        
    def get(self):
        if self.empty():
            return False
        else:
            return self.vector[self.start]

queue = Queue(5)
queue.insert(2)
queue.insert(10)
queue.insert(4)
queue.insert(3)
queue.remove()
queue.remove()
queue.insert(2)
queue.insert(10)
queue.print()