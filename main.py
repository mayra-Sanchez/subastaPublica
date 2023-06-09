import tkinter as tk
from tkinter import filedialog, Label, PhotoImage
from texto.accionesV import accionesV
from texto.accionesFB import accionesFB
from texto.accionesPD1 import accionesPD1
from texto.accionesPD2 import accionesPD2
import os
import glob

# Crear una instancia de la ventana
ventana = tk.Tk()

# Definir el título de la ventana
ventana.title("Subasta pública de acciones")
ventana.config(bg="white")

# Definir las dimensiones de la ventana
ventana.geometry("400x400")

# Titulo
titulo = tk.Label(ventana, text="Subasta pública de acciones", fg="white")
titulo.pack()
titulo.config(font=('Times New Roman', 25), bg="black")
titulo.place(x=20, y=10)
# Texto 2
texto_archivo = tk.Label(ventana, text="Seleccione el archivo a leer", fg="black")
texto_archivo.pack()
texto_archivo.config(font=('Times New Roman', 12), bg="white")
texto_archivo.place(x=10, y=70)

# Función para abrir el selector de archivos

def abrir_archivo():
    global extension
    archivo = filedialog.askopenfilename(
        filetypes=[('Subtitles files', '*.sub *.psub')])
    if archivo is not None:
        ruta_archivo.set(archivo)
        extension = os.path.splitext(archivo)[1].lower()
    
# Crear una variable para almacenar la ruta del archivo seleccionado
ruta_archivo = tk.StringVar()

# Crear un label para mostrar el nombre del archivo seleccionado
label_archivo = tk.Label(ventana, textvariable=ruta_archivo)
label_archivo.pack()
label_archivo.config(font=('Arial', 8), bg="white")
label_archivo.place(x=10, y=130)

# Crear un botón para abrir el selector de archivos
boton = tk.Button(ventana, text="Seleccionar archivo",
                  command=abrir_archivo, bg="black", fg="white")
boton.pack()
boton.place(x=10, y=100)

# Texto 3
texto_drop = tk.Label(ventana, text="Seleccione el algoritmo que desea probar", fg="black")
texto_drop.pack()
texto_drop.config(font=('Times New Roman', 12), bg="white")
texto_drop.place(x=10, y=150)

# DropBox
opciones = ["Fuerza bruta", "Voraz", "Dinamica 1", "Dinamica 2"]
variar_opciones = tk.StringVar(ventana)
variar_opciones.set(opciones[0])

drop_box = tk.OptionMenu(ventana, variar_opciones, *opciones)
drop_box.pack()
drop_box.place(x=10, y=180)
drop_box.config(font=('Times New Roman', 10), bg="black", fg="white")

# Texto 4
texto_descarga = tk.Label(ventana, text="Para descargar el archivo de salida, presione el boton", fg="black")
texto_descarga.pack()
texto_descarga.config(font=('Times New Roman', 12), bg="white")
texto_descarga.place(x=10, y=220)

def iniciar_algoritmo():
    algoritmo_seleccionado = variar_opciones.get()
    entrada = ruta_archivo.get()

    if algoritmo_seleccionado == "Fuerza bruta":
        if extension == '.sub':
            accionesFB(entrada, 1)
        elif extension == '.psub':
            accionesFB(entrada, 2)
    elif algoritmo_seleccionado == "Voraz":
        if extension == '.sub':
            accionesV(entrada, 1)
        elif extension == '.psub':
            accionesV(entrada, 2)
    elif algoritmo_seleccionado == "Dinamica 1":
        if extension == '.sub':
            accionesPD1(entrada, 1)
        elif extension == '.psub':
            accionesPD1(entrada, 2)
    elif algoritmo_seleccionado == "Dinamica 2":
            accionesPD2(entrada)

# Botón para iniciar el algoritmo seleccionado
boton_inicio = tk.Button(ventana, text="Iniciar algoritmo", command=iniciar_algoritmo, bg="black", fg="white")
boton_inicio.pack()
boton_inicio.place(x=160, y=182)

# Deshabilitar y habilitar boton de desacarga

def buscar():
    NombreArchivo = "output.txt"
    ruta_archivo = None
    for archivo in os.listdir():
        if archivo == NombreArchivo:
            ruta_archivo = os.path.abspath(archivo)
            break
    return ruta_archivo

def habilitar_descarga():
    ruta = buscar()
    if ruta is not None:
        boton_salida.config(state=tk.NORMAL)
    else:
        boton_salida.config(state=tk.DISABLED)

def descargar_archivo():
    ruta = buscar()
    if ruta is not None:
        archivo = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if archivo is not None:
            with open(ruta, 'r') as archivo_original:
                contenido = archivo_original.read()
                archivo.write(contenido)
                archivo.close()

# Configuraciones del botón
boton_salida = tk.Button(ventana, text="Descargar salida", command=lambda: (habilitar_descarga(),  descargar_archivo()), bg="black", fg="white")
boton_salida.pack()
boton_salida.config(font=('Times New Roman', 10))
boton_salida.place(x=10, y=260)

def mostrar_creditos():
    ventana_creditos = tk.Toplevel(ventana)
    ventana_creditos.title("Créditos")
    ventana_creditos. geometry("300x200")
    ventana_creditos.config(bg="white")

    # Crear una etiqueta para mostrar los créditos del programa
    etiqueta_creditos = tk.Label(
        ventana_creditos, text="Créditos \n  \n Laura Daniela Jaimes - 2040430 \n Santiago Casañas Tabares - 2025301 \n Mayra Alejandra Sanchez - 2040506 \n Jesús Adrian Peña - 2025513")
    etiqueta_creditos.pack()
    etiqueta_creditos.config(font=('Times New Roman', 10), bg="white")
    etiqueta_creditos.place(x=50, y=50)

boton_creditos = tk.Button(ventana, text="Créditos",command=mostrar_creditos, bg="red")
boton_creditos.pack()
boton_creditos.config(font=('Times New Roman', 10))
boton_creditos.place(x=300, y=350)

# Imagen
image = PhotoImage(file="resources/subasta.png")
labelImagen = Label(image=image)
labelImagen.pack()
labelImagen.place(x=10, y=290)
labelImagen.config(bg="white")

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
