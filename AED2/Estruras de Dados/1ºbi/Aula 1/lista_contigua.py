class ListaCont:

    def __init__(self, max):
        self.max = max
        self.vetor = [None] * self.max
        self.ini = None
        self.end = None


    def vazia(self):
        return self.ini == None


    def valor(self, pos):
        if not self.vazia() and pos < self.tam() and pos >= 0:
            return [self.vetor + self.ini]


    def tam(self):
        if not self.vazia():
            return self.fim - self.ini + 1
        return 0


    def pos(self, valor):
        for i in range(self.ini, self.fim + 1):
            if valor == self.vetor[i]:
                return i - self.ini
        return None    


    def inserir(self, index, valor):
        if index >= 0 and index <= self.tam() and self.tam() < self.max:
            if self.vazia():
                self.ini = self.max // 2
                self.fim = self.max // 2
                self.vetor[self.ini] = valor
            elif index == 0 and self.ini != 0:
                self.ini -= 1
                self.vetor[self.ini] = valor
            elif index == self.tam() and self.fim != self.max - 1:
                self.fim += 1
                self.vetor[self.fim] = valor
            elif self.fim == self.max - 1:
                self.ini -= 1
                for i in range(self.ini, index + self.ini):
                    self.vetor[i] = self.vetor[i + 1]
                self.vetor[self.ini + index] = valor
            elif self.ini == 0:
                self.fim += 1
                for i in range(self.fim, index, -1):
                    self.vetor[self.fim] = self.vetor[self.fim - 1]
                self.vetor[self.ini + index] = valor
            else:
                self.ini -= 1
                for i in range(self.ini, index + self.ini):
                    self.vetor[i] = self.vetor[i + 1]
                self.vetor[self.ini + index] = valor
        else:
            return False

    def adicionar(self, valor):
        if self.tam() != self.max:
            if self.vazia():
                self.ini = self.max // 2
                self.fim = self.max // 2
                self.vetor[self.ini] = valor
            elif self.max == self.fim:
                self.ini -= 1
                for i in range(self.ini, self.fim - 1):
                    self.vetor[i] = self.vetor[i + 1]
                self.vetor[self.fim] = valor
            else:
                self.vector[self.fim] = valor
        else:
            return False

    def remover(self, valor):
        if not self.vazia and valor in self.vetor:
            if self.ini > self.max - self.fim:
                pass