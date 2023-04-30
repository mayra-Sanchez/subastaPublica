from algoritmos.dinamica1 import PD1
from algoritmos.vr import funcionVR


def accionesPD1(entrada, extension):

    archivo = open(entrada, "r", encoding="utf-8")
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

    if extension == 1:
        for i in range(3, len(instrucciones)):
            tripletas.append(instrucciones[i][0])

    if extension == 2: 
        for i in range(3, len(instrucciones)-1):
            tripletas.append(instrucciones[i][0])

    ofertas = []

    for j in tripletas:
        ofertantes = [int(x) for x in j.split(",")]
        tripleta = tuple(ofertantes)
        ofertas.append(tripleta)

    # Transformar
    salida.append(str(PD1(A,B,n,ofertas)[0]))
    funcion_salida = PD1(A, B, n, ofertas)[1]
    

    for i in funcion_salida:
        salida.append(str(i))
        print(salida)
    
    

    with open("output.txt", "w") as t:
        t.write('\n'.join(salida))
