def voraz(A, B, n, ofertas):

  # valor que pagan los ofertantes
  identificador_costo = list(enumerate([i[0] for i in ofertas])) # Asigna identificador a la lista de costos
  ofertas_ordenadas = sorted(identificador_costo, key=lambda x: x[1], reverse=True) # Ordena la lista de costos
  accion_maxima = A
  valor_minimo = B
  zeros = [0] * (n+1)

  for i in ofertas_ordenadas:
    if accion_maxima == 0:
      break
    if accion_maxima>=ofertas[i[0]][1]:
      zeros[i[0]] = ofertas[i[0]][1]
      accion_maxima = accion_maxima-ofertas[i[0]][1]
    elif accion_maxima<ofertas[i[0]][1] and accion_maxima>=ofertas[i[0]][2]:
      zeros[i[0]] = accion_maxima
      accion_maxima = accion_maxima - accion_maxima


  return zeros