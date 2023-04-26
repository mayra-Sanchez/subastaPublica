from algoritmos.vr import funcionVR
from algoritmos.dinamica2 import funcionPD2

def accionesPD2(entrada):

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

    for i in range(3, len(instrucciones)):
        tripletas.append(instrucciones[i][0])

    ofertas = []

    for j in tripletas:
        ofertantes = [int(x) for x in j.split(",")]
        tripleta = tuple(ofertantes)
        ofertas.append(tripleta)

    # Transformar
    salida.append(str(funcionVR(funcionPD2(A, B, n, ofertas), ofertas)))
    funcion_salida = funcionPD2(A, B, n, ofertas)

    for i in funcion_salida:
        salida.append(str(i))

    with open("output.txt", "w") as t:
        t.write('\n'.join(salida))
