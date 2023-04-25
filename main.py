import tkinter as tk
from tkinter import filedialog
from algoritmos.vr import funcionVR
from algoritmos.fuerzaBruta import bruta
from algoritmos.voraz import voraz

# Crear una instancia de la ventana
ventana = tk.Tk()

# Definir el título de la ventana
ventana.title("Subasta pública de acciones")
ventana.config(bg="white")

# Definir las dimensiones de la ventana
ventana.geometry("400x400")

#Titulo
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
    archivo = filedialog.askopenfile()
    if archivo is not None:
        ruta_archivo.set(archivo.name)

# Crear una variable para almacenar la ruta del archivo seleccionado
ruta_archivo = tk.StringVar()

# Crear un label para mostrar el nombre del archivo seleccionado
label_archivo = tk.Label(ventana, textvariable=ruta_archivo)
label_archivo.pack()
label_archivo.config(font=('Arial',8))
label_archivo.place(x=10, y=130)

# Crear un botón para abrir el selector de archivos
boton = tk.Button(ventana, text="Seleccionar archivo", command=abrir_archivo, bg="black", fg="white")
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

def leer_archivos(ruta_archivo):
    archivo= open(ruta_archivo, "r", encoding="utf-8")
    instrucciones = []
    salida = []
    
    # Lee el archivo de entrada y almacena las instrucciones A, B, n, oferta(p,c,r), gobierno
    while (True):
       line = archivo.readline()
       listLine = line.split()
       if listLine == []:
          break
       instrucciones.append(listLine)
    
    A = int(instrucciones[0][0])
    B = int(instrucciones[1][0])
    n = int(instrucciones[2][0])
    tripletas = []
    
    for i in range(3,len(instrucciones)):
       tripletas.append(instrucciones[i][0])
    
    ofertas = []
    
    for j in tripletas:
        ofertantes = [int(x) for x in j.split(",")]
        tripleta = tuple(ofertantes)
        ofertas.append(tripleta)
    
    if variar_opciones.get() == "Fuerza bruta":
        salida.append(str(bruta(A,B,n,ofertas)))
        funcion_salida = bruta(A,B,n,ofertas)
    elif variar_opciones.get() == "Voraz":
        salida.append(str(funcionVR(voraz(A,B,n,ofertas), ofertas)))
        funcion_salida = voraz(A,B,n,ofertas)
    elif variar_opciones.get() == "Dinamica 1":
        # implementar el código para Dinamica 1
        pass
    elif variar_opciones.get() == "Dinamica 2":
        # implementar el código para Dinamica 2
        pass
    else:
        # no se seleccionó ninguna opción válida
        pass

    # Resto del código para generar la salida y descargar el archivo
    for i in funcion_salida:
        salida.append(str(i))
        
    with open("salidaSubasta.txt", "w") as t:
        t.write('\n'.join(salida))

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
