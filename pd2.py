from algoritmos.dinamica2 import PD2


def pd2(entrada):

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
    M = int(instrucciones[len(instrucciones)-1][0])
    print(M)
    tripletas = []

    for i in range(3, len(instrucciones)-1):

        tripletas.append(instrucciones[i][0])

    ofertas = []

    for j in tripletas:
        ofertantes = [int(x) for x in j.split(",")]
        tripleta = tuple(ofertantes)
        ofertas.append(tripleta)

    # Transformar
    salida.append(str(PD2(A, B, n, ofertas, M)[0]))
    funcion_salida = PD2(A, B, n, ofertas, M)[1]

    for i in funcion_salida:
        salida.append(str(i))

    with open("outputPD1.txt", "w") as t:
        t.write('\n'.join(salida))


pd2("texto.sub")
