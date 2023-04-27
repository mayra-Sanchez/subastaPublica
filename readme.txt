Descripción de archivos entregados...

Archivo main: Este archivo .py es el principal, en el cual se crea la interfaz de usuario. Este archivo también configura las ventanas y llama a los algoritmos almacenados en la 
carpeta "texto". Su función es llamar al algoritmo si este ha sido seleccionado por el usuario en la interfaz. Después de darle "iniciar algoritmo", el usuario podrá descargar 
el archivo de salida generado por el programa.

-> Carpeta algoritmos

    Este archivo recibe (x, ofertantes), x siendo la asignacion devuelta como la mas optima de los algoritmos y recibe toda la tripleta de ofertantes para hacer el calculo de vr 
    de esa asignacion optima.

    -> vr.py: En este archivo se tiene la función que calcula el valor recibido y es muy importante, es usada en todos los archivos.

    Todos los siguientes archivos reciben 4 entradas (A, B, n. ofertantes)

    -> voraz.py: En este archivo se tiene el algoritmo voraz.
    -> fueraBruta.py: En este archivo se tiene el algoritmo de fuerza bruta.
    -> dinamica1.py: En este archivo se tiene el algoritmo de programacion dinamica original.
    -> dinamica2.py: En este archivo se tiene el algoritmo de programacion dinamica modificado.

-> Carpeta texto

    La funcionalidad de todos estos archivos es recibir la entrada que da el usuario, procesar según el algoritmo que sea seleccionado en la interfaz y finalmente generar un archivo 
    de texto con la respuesta final al problema dado.

    -> accionesFB.py: Este archivo importa de carpeta de algoritmos el algoritmo fuerzaBruta.py y funcionVR
    -> accionesV.py: Este archivo importa de carpeta de algoritmos el algoritmo voraz.py y funcionVR
    -> accionesPD1.py: Este archivo importa de carpeta de algoritmos el algoritmo dinamica1.py y funcionVR
    -> accionesPD2.py: Este archivo importa de carpeta de algoritmos el algoritmo dinamica2.py y funcionVR

Instrucciones para ejecutar el programa: