from list import ListaEnc

lista = ListaEnc()

lista.inserir(0, 'A')
lista.inserir(1, 'B')
lista.inserir(0, 'C')
lista.inserir(1, 'D')

lista.imprimir()
print(lista.tam)
print()
print(lista.position('B'))
print(lista.valor(3))