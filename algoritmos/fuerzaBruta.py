from algoritmos.vr import funcionVR

def bruta(A, B, n, tripleta):

  valores = [i[1] for i in tripleta]
  zeros = [0] * (n+1)
  combinaciones = []

  for i in range(2**(n+1)):
    binario = bin(i)[2:].zfill(n+1)
    suma = 0
    combinacion = []
    valor = 0
    
    for j in range(n+1):
        if binario[j] == '1':
            
            suma += valores[j]
            combinacion.append(valores[j])
        else:
            combinacion.append(zeros[j])
    
    if suma <= A :
        valor = A - suma 
        combinacion[-1] = valor
        combinaciones.append(combinacion)

  listaFinal = list(filter(lambda x: not all(i == 0 for i in x), combinaciones))

  return max(listaFinal, key = lambda x: funcionVR(x, tripleta))