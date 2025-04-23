class Nodo:
    def __init__(self, v):
        self.valor = v
        self.prox = None


class ListaEnc:
    def __init__(self):
        self.ini = None
        self.fim = None
        self.tam = 0

    
    def inserir(self, pos, v):
        if pos >= 0:
            aux = Nodo(v)
            if self.tam == 0:
                self.ini = aux
                self.fim = aux
            elif pos == self.tam:
                self.fim.prox = aux
                self.fim = aux
            elif pos == 0:
                aux.prox = self.ini
                self.ini = aux
            else:
                var = self.ini
                for i in range(pos):
                    if i == pos - 1:
                        ant = var
                    var = var.prox
                aux.prox = var
                ant.prox = aux

            self.tam += 1

            return True 
        else:
            return False
        
        
    def imprimir(self):
        if self.ini != None:
            var = self.ini
            while var.prox != None:
                print(var.valor)
                var = var.prox
            if var.prox == None:
                print(var.valor)
        else:
            print('[]')

    
    def valor(self, pos):
        if pos < self.tam:
            cont = 0
            var = self.ini
            if var != None:
                while var.prox != None:
                    if cont == pos:
                        return var.valor
                    var = var.prox
                    cont += 1
                if var.prox == None:
                    return var.valor
            else:
                return False
        else:
            return False
        

    def position(self, value):
        cont = 0
        var = self.ini
        if var != None:
            while var.prox != None:
                if value == var.valor:
                    return cont
                var = var.prox
                cont += 1
            if var.prox == None and value == var.valor:
                return cont
            else:
                return False
        
        else:
            return False