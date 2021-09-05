from tkinter import *
import tkinter as tk
from tkinter import messagebox
from auxiliar2 import postOrder
from arbolBinario import ArbolBinario
class VentanaArbol:
    def __init__(self):

        def addTree():
            cadenaArbol.set(text_box.get())
            arbol = ArbolBinario()
            arbol.buildTree(cadenaArbol)
            postOrder(arbol.root)
            print(" ------------------- ")

        # Propiedades de la ventana
        windowBinaryTree = Tk()
        cadenaArbol = StringVar()
        windowBinaryTree.resizable(False, False)
        windowBinaryTree.geometry("450x450")
        windowBinaryTree.title("Ingreso de Árbol Binario")
        windowBinaryTree.config(background="#757574")
        # Propiedades del Label
        label = Label(windowBinaryTree, text="Escribe el árbol binario en forma de hilera con comas",
                      font=("Consolas", 10), bg="#005e35", fg="#ffffff", width="60", height="2")
        label.place(x=12, y=10)
        # Propiedades de la caja de texto
        text_box = Entry(windowBinaryTree, font=("Consolas", 12), textvariable=cadenaArbol, width="30")
        text_box.place(x=90, y=80)
        # Propiedades del botón
        button_send = Button(windowBinaryTree, text="Agregar", command=addTree, font=("Consolas", 10),
                             bg="#005e35", fg="#ffffff", width="14", height="2")
        button_send.place(x=180, y=120)
        # Propiedades sección de Resultados
        result_box = Label(windowBinaryTree, text="mostrarArbol", font=("Consolas", 10), bg="#005e35", fg="#ffffff",
                           width="60", height="2")
        result_box.place(x=12, y=150)
        windowBinaryTree.mainloop()

