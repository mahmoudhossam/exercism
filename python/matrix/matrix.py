class Matrix(object):
    def __init__(self, matrix_string):
        rows = matrix_string.split("\n")
        self.matrix = []
        for row in rows:
            self.matrix.append([int(x) for x in row.split()])

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        column = []
        for row in self.matrix:
            column.append(row[index - 1])
        return column
