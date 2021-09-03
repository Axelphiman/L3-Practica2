from tkinter import *
import tkinter as tk
from tkinter import messagebox
from arbolBinario import ArbolBinario

#Esta función utilizaría método de la clase arbolBinario
def addTree():

    pass

#Función que crea una nueva ventana para la construcción de Árbol Binario digitado por el Usuario
def openBinaryTreeGUI():
    #Propiedades de la ventana
    windowBinaryTree = Tk()
    windowBinaryTree.resizable(False, False)
    windowBinaryTree.geometry("450x450")
    windowBinaryTree.title("Ingreso de Árbol Binario")
    windowBinaryTree.config(background="#757574")
    #Propiedades del Label
    label = Label(windowBinaryTree, text="Escribe el árbol binario en forma de hilera con comas", font=("Consolas",10), bg="#005e35", fg="#ffffff", width="60",height="2")
    label.place(x=12, y=10)
    #Propiedades de la caja de texto
    text_box = Entry(windowBinaryTree,font=("Consolas",12),stringvariable=cadenaArbol,width="30")
    text_box.place(x=90,y= 80)
    print(cadenaArbol)
    #Propiedades del botón
    button_send = Button(windowBinaryTree, text="Agregar", command="addTree",font=("Consolas",10), bg="#005e35", fg="#ffffff", width="14",height="2")
    button_send.place(x=180,y= 120)
    #Propiedades sección de Resultados
    result_box = Label(windowBinaryTree, text="mostrarArbol",font=("Consolas",10),bg="#005e35", fg="#ffffff", width="60",height="2")
    result_box.place(x=12,y=150)
    windowBinaryTree.mainloop()

#Función para generar los manuales
def openInfoUser():
    messagebox.showinfo(title="Manual de Usuario", message="Aquí el manual de usuario o tecnico")


#Propiedades de la ventana Principal
window = Tk()
window.resizable(False,False)
window.geometry("520x340")
window.title("Práctica #2 - LyR III")
window.config(background = "#757574")
back_Title = tk.Label(text="Segunda práctica de Lógica y Representanción III\n\n Hecho por: Diego Muñoz y Esteban Cossio", font=("Consolas",14), bg="#005e35", fg="#ffffff", width="52",height="8")
back_Title.place(x = 0, y = 80)
#Creando la barra de Menú
barMenu = Menu(window)
mnuTree = Menu(barMenu)
mnuInformation = Menu(barMenu)
#Añadiendo los botones para Árboles Binarios en la barra de Menú
mnuTree.add_command(label="Nuevo Árbol", command=openBinaryTreeGUI)
mnuTree.add_command(label="Árbol aleatorio")
mnuTree.add_command(label="Árbol a partir de recorridos")
#Añadiendo los botones para Información del Programa
mnuInformation.add_command(label="Manual de Usuario", command=openInfoUser)
mnuInformation.add_command(label="Manual técnico")
#La barra de menú es tipo cascada
barMenu.add_cascade(label="Árboles",menu=mnuTree)
barMenu.add_cascade(label="Información",menu=mnuInformation)
window.config(menu=barMenu)

window.mainloop()
