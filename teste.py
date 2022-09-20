from matrix import Matrix

Davi = Matrix (2,2)
Paulin = Matrix (2,2)

Davi.fill()
Paulin.fill()
resultado = Matrix.sum(Davi, Paulin)
print(resultado)
