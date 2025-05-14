class Pilha:
    def __init__(self, tam):
        self.limite = tam  - 1
        self.vetor = [None] * tam
        self.base = 0
        self.topo = -1

    
    def inserir(self, valor):
        if self.topo != self.limite:
            self.topo += 1
            self.vetor[self.topo] = valor
            return True
        return False
    

    def remover(self):
        if self.topo >= self.base:
            self.vetor[self.topo] = None
            self.topo -= 1
            return True
        return False
    

    def consulta(self):
        if self.topo >= self.base:
            return self.vetor[self.topo]
        return False
    
    
    def modificar(self, valor):
        if self.topo >= self.base:
            self.vetor[self.topo] = valor
            return True
        return False
    

    def mostrar(self):
        if self.topo >= self.base:
            for item in reversed(self.vetor):
                if item != None:
                    print(item)
        else:
            print("Pilha vazia!")


    def destruir(self):
        self.topo = -1
        self.vetor = None
        self.limite = 0


    def inverter(self):
        if self.topo >= self.base:
            aux = [None] * self.limite
            idx = 0
            for i in range(self.topo, 0, -1):
                aux[idx] = self.vetor[i]
                idx += 1

            self.vetor = aux
            return True
        return False
    

    def comparar(self, alvo):
        igual = True

        if self.topo >= self.base and self.topo == alvo.topo:
            for i in range(self.topo):
                if self.vetor[i] != alvo.vetor[i]:
                    igual = False
        else:
            igual = False

        return igual
    
    def menor(self):
        menor = self.vetor[self.base]

        for i in range(self.base + 1, self.topo):
            if self.vetor[i] < menor:
                menor = self.vetor[i]

        return menor

teste = Pilha(10)
teste_2 = Pilha(10)
teste_3 = Pilha(10)
teste_4 = Pilha(5)

teste.inserir(1)
teste.inserir(5)
teste.inserir(8)
teste.inserir(3)
teste.inserir(7)
teste.inserir(1)
teste.inserir(5)
teste.modificar(10)
teste.remover()
print()

teste_2.inserir(1)
teste_2.inserir(5)
teste_2.inserir(8)
teste_2.inserir(1)
teste_2.inserir(7)
teste_2.inserir(1)
teste_2.inserir(5)
teste_2.modificar(10)
teste_2.remover()

teste_3.inserir(1)
teste_3.inserir(5)
teste_3.inserir(8)
teste_3.inserir(3)
teste_3.inserir(7)
teste_3.inserir(1)
teste_3.inserir(5)
teste_3.modificar(10)
teste_3.remover()

teste_4.inserir(1)
teste_4.inserir(5)
teste_4.inserir(8)
teste_4.inserir(3)
teste_4.inserir(7)
teste_4.modificar(10)
teste_4.remover()

print(teste.comparar(teste_2), teste.comparar(teste_3), teste.comparar(teste_4))

print(teste.menor())