def funcionVR(X, tripleta):
  var = 0
  cantidad = 0
  for j in tripleta:
    cantidad += X[var] * j[0] 
    var+= 1
  return cantidad