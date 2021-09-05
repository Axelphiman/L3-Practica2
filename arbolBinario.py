from nodo import Nodo
import random

class ArbolBinario:
    #Funciones privadas
    def __init__(self,dato = None):
        self.root = Nodo(dato)

    def buildTree(self, cadenaTexto ):
        aleatorio = random
        def separadorString(cadena):
            return [char for char in cadena]
        vectorCaracteres = separadorString(cadenaTexto.get())
        vectorNodos = []

        #Cracion vector de nodos
        for char in vectorCaracteres:
            vectorNodos.append(Nodo(char))

        arbol = [None]*(2**(len(vectorNodos))-1)
        espaciosDisponibles = [0]


        for nodo in vectorNodos:
            numero = aleatorio.randint(0, len(espaciosDisponibles) - 1)
            arbol[espaciosDisponibles[numero]] = nodo
            espaciosDisponibles.append(espaciosDisponibles[numero]*2 + 1)
            espaciosDisponibles.append(espaciosDisponibles[numero] * 2 + 2)
            del espaciosDisponibles[numero]

        for i in range(len(arbol)):

            if arbol[i] is not None and (i*2+2) < len(arbol):
                arbol[i].left = arbol[i*2 + 1]
                arbol[i].right = arbol[i*2 + 2]
        self.root = arbol[0]
        return self.root





