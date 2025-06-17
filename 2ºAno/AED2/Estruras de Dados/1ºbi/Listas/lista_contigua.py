class ListContigua:
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.vector = [None] * max_size
        self.start = -1
        self.end = -1
        
    def __str__(self):
        if self.is_empty():
            return "[]"
        return str(self.vector[self.start : self.end + 1])

    def __getitem__(self, index):
        return self.get(index)
    
    @property
    def size(self):
        if self.is_empty():
            return 0
        return self.end - self.start + 1
        
    def is_empty(self):
        return self.start == -1

    def is_full(self):
        return self.size == self.max_size

    def insert(self, value, index):
        if self.is_full():
            print(f"Erro: A lista está cheia. Não é possível inserir {value}.")
            return
            
        if not (0 <= index <= self.size):
            print(f"Erro: Índice {index} fora do intervalo válido [0, {self.size}]")
            return

        if self.is_empty():
            self.start = self.max_size // 2
            self.end = self.start
            self.vector[self.start] = value
            return

        if index < self.size / 2:
            if self.start > 0:
                self.start -= 1
                for i in range(self.start, self.start + index):
                    self.vector[i] = self.vector[i + 1]
            else:
                self.end += 1
                for i in range(self.end, self.start + index, -1):
                    self.vector[i] = self.vector[i - 1]
        else:
            if self.end < self.max_size - 1:
                self.end += 1
                for i in range(self.end, self.start + index, -1):
                    self.vector[i] = self.vector[i - 1]
            else:
                self.start -= 1
                for i in range(self.start, self.start + index):
                    self.vector[i] = self.vector[i + 1]
        
        self.vector[self.start + index] = value
        
    def remove(self, index):
        if self.is_empty() or not (0 <= index < self.size):
            raise IndexError("Índice de remoção fora do intervalo válido.")

        removed_value = self.vector[self.start + index]

        if self.size == 1:
            self.vector[self.start] = None
            self.start = -1
            self.end = -1
            return removed_value

        if index < self.size / 2:
            for i in range(self.start + index, self.start, -1):
                self.vector[i] = self.vector[i - 1]
            self.vector[self.start] = None
            self.start += 1
        else:
            for i in range(self.start + index, self.end):
                self.vector[i] = self.vector[i + 1]
            self.vector[self.end] = None
            self.end -= 1
            
        return removed_value

    def find(self, value):
        if self.is_empty():
            return -1
        
        for i in range(self.start, self.end + 1):
            if self.vector[i] == value:
                return i - self.start
        return -1

    def get(self, index):
        if not (0 <= index < self.size):
            raise IndexError("Índice fora do intervalo válido.")
        return self.vector[self.start + index]
