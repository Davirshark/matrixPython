from matrix import Matrix

Davi = Matrix (2,2)
Paulin = Matrix (2,3)

Davi.fill()
Paulin.fill()
resultado = Matrix.mult(Davi, Paulin)
print(resultado.body)
