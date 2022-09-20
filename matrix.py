class Matrix(object):

    lines = 0
    columms = 0
    body = []

    def __init__(self, lines, columms):
        self.lines = lines
        self.columms = columms
        self.body = self.gerar(lines, columms)

    def gerar(self, lines, columms):
        gerada = []
        for _ in range(lines):
            gerada.append([" "] * columms)
        return gerada

    def show(self):
        return print(self.body)

    def lenght(self):
        return self.lines * self.columms

    def isSquare(self):
        if (self.lines == self.columms) or (self.columms == self.lines):
            return True
        else:
            return False

    def fill(self):
        for line in range(self.lines):
            for columm in range(self.columms):
                self.element = int(input
    (f"Digite um valor na posição [{line}][{columm}]: "
    .format([line],[columm])))
                self.body[line][columm] = self.element
        

    def pDiagonal(self):
        if self.isSquare():
            diagonal_principal = []
            for i in range(len(self.body)):
                diagonal_principal.append(self.body[i][i])
            return diagonal_principal
        else:
            return "matriz não quadradas não possuem diagonal principal"

    def sDiagonal(self):
        if self.isSquare():
            diagonal_secundaria = []
            for i in range(len(self.body)):
                for j in range(len(self.body)):
                    if i == self.columms - 1 - j:
                        diagonal_secundaria.append(self.body[i][j])
            return diagonal_secundaria
        else:
            return "matriz não quadradas não possuem diagonal secundária"

    def multDiagonalPrincipal(self):
        produto = 1
        for numero in self.pDiagonal():
            produto *= numero
        return produto

    def xDiagonal(self, mult):
        if self.isSquare():
            mult = [i * mult for i in self.pDiagonal()]
            return mult
        else:
            return "matriz não quadradas não possuem diagonal principal"

    def feature(self):
        if self.isSquare():
            return sum(self.pDiagonal())
        else:
            return "matriz não quadradas não possuem traço"

    def transpoose(self):
        mat_transpoose = list(map(lambda *i: [j for j in i], *self.body))
        self.body = mat_transpoose
        return self

    def det(self):
        if self.isSquare():
            if (self.lines == 2) and (self.columms == 2):
                return sum(self.pDiagonal()) - sum(self.sDiagonal())
            else:
                pass

    def sum(self, sumMatrix):
        Soma = Matrix (self.lines, self.columms)
        if (self.lines == sumMatrix.lines) and (self.columms == sumMatrix.columms):
            for i in range (self.lines):
                for j in range (self.columms):
                   Soma.body[i][j] = self.body[i][j] + sumMatrix.body[i][j]
            return Soma
        else:
            return "Matrizes de tamanho diferentes não podem ser somadas"

    def getLinha(self, n):
        return [i for i in self.body[n]] 

    def getColuna(self, n):
        return [i[n] for i in self.body]

    def mult(self, multMatrix):
        if (self.columms == multMatrix.lines):
            result = Matrix (self.lines, multMatrix.columms)
            for i in range(self.lines):           
                for j in range(multMatrix.columms):
                    listMult = [x*y for x, y in zip(self.getLinha(i), multMatrix.getColuna(j))]
                    result.body[i][j] = sum(listMult)
            
            return result                
        else:
            return "Matrizes que não podem ser multiplicadas"

