class Matrix:
    def __init__(self, rows:list) -> None:
        self.rows = rows
        self.x = len(self.rows[0])
        self.y = len(self.rows)

    def remove_column(self, index:int):
        for i in range(self.y):
            self.rows[i].pop(index)
        self.x -= 1
        return self
                
    def remove_row(self, index:int):
        self.rows.pop(index)
        self.y -= 1
        return self
        
    def set_column(self, index:int, data:list) -> None:
        for i in range(self.y):
            self.rows[i][index] = data[i]

    def set_row(self, index:int, data:list) -> None:
        self.rows[index] = data

    def get_column(self, index:int) -> list:
        data:list = []
        for i in range(self.y):
            data.append(self.rows[i][index])
        return data

    def get_row(self, index:int) -> list:
        return self.rows[index]

    def duplicate(self):
        rows:list = []
        for row in self.rows:
            new_row:list = []
            for number in row:
                new_row.append(number)
            rows.append(new_row)
        return Matrix(rows)

    def determinant(self) -> float:
        if self.x == self.y:
            determinant:float = 0
            if self.x == 2:
                determinant += (self.rows[0][0] * self.rows[1][1]) - (self.rows[1][0] * self.rows[0][1])
            else:
                for i in range(self.y):
                    determinant += (1 if (i%2) == 0 else -1) * self.rows[0][i] * self.duplicate().remove_row(0).remove_column(i).determinant()
            return determinant
    
    def multiply(self, otherMatrix):
        if (self.X == otherMatrix.Y):
            result = []
            for i in range(self.Y):
                newRow = []
                for k in range(otherMatrix.X):
                    newElement = 0
                    for j in range(self.X):
                        newElement += self.data[i][j] * otherMatrix.data[j][k]
                    newRow.append(newElement)
                result.append(newRow)
            return Matrix(result)
        
    def add(self, otherMatrix):
        if self.x == otherMatrix.x and self.y == otherMatrix.y:
            result:list = []
            for x in range(self.x):
                newRow:list = []
                for y in range(self.y):
                    newRow.append(self.rows[x][y] + otherMatrix.rows[x][y])
                result.append(newRow)
            return Matrix(result)
        
    def subtract(self, otherMatrix):
        if self.x == otherMatrix.x and self.y == otherMatrix.y:
            result:list = []
            for x in range(self.x):
                newRow:list = []
                for y in range(self.y):
                    newRow.append(self.rows[x][y] - otherMatrix.rows[x][y])
                result.append(newRow)
            return Matrix(result)

    def __str__(self) -> str:
        output:str = ''
        for row in self.rows:
            output += '|'
            for number in row:
                output += str(number) + ', '
            output = output[:-2]
            output += '|\n'
        return output
    
data:list = [
	[00,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,00],
	[+1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,+1],
	[+2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,+2],
	[+3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,+3],
	[+4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,+5],
	[+5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,+6],
	[+6,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,+8],
	[+7,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,10],
	[+8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,13],
	[+9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,16],
	[10,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,22],
	[11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,26],
	[12,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,35],
	[13,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,42],
	[14,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,48],
	[15,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,57],
	[16,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,69],
	[17,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,78],
	[18,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,86],
	[19,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,92],
]
def main() -> None:
	DataMatrix:Matrix = Matrix(data)
	print(DataMatrix)
	print(solve(DataMatrix))
	

def solve(matrix:Matrix):
	De:Matrix = matrix.duplicate()
	E:list = De.get_column(De.x - 1)
	De.remove_column(De.x - 1)
	d = De.duplicate().determinant()
	return d
if __name__ == '__main__':
    main()