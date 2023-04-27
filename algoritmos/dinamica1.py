from algoritmos.vr import funcionVR
import numpy as np


def PD1(A, B, n, ofertas):
    matriz = np.empty((n+1, A+1), dtype=object)
    matriz[:] = None
    X = zeros = [0] * (n+1)

    def valorRecursivo(n, A):
        if matriz[n][A] != None:
            return matriz[n][A]
        if A <= 0 or n <= 0:
            mejorOpcion = (0, ([], []))
        else:
            precio, maximo, minimo = ofertas[n-1]
            mejorOpcion = valorRecursivo(n-1, A)
            maximoAVender = min(A, maximo)
            for accionesVender in range(minimo, maximoAVender+1):
                opcionActual = valorRecursivo(n-1, A-accionesVender)
                nuevovr = precio*accionesVender
                if opcionActual[0]+nuevovr > mejorOpcion[0]:
                    mejorOpcion = (
                        opcionActual[0]+nuevovr, (opcionActual[1][0]+[accionesVender], opcionActual[1][1]+[n]))

        matriz[n][A] = mejorOpcion
        return mejorOpcion

    def construirSolucion(x):
        j = 0
        for i in x[1][1]:
            X[i-1] = x[1][0][j]
            j += 1
        return X

    return construirSolucion(valorRecursivo(n, A))
