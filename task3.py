from constants_task3 import *


def search_start(array):
    [x, y] = random.randint(0, size - 1), random.randint(0, size - 1)
    while array[x][y] != 1:
        [x, y] = random.randint(0, size - 1), random.randint(0, size - 1)
    print('{}->'.format((x, y)))
    return x, y


class Cell:
    def __init__(self, x, y, value):
        self.routes = {'r': False, 'l': False, 'd': False, 'u': False}
        self.visited = False
        self.value = value
        self.coordinates = (x, y)

    def __repr__(self):
        return '{} {}'.format(self.coordinates[0], self.coordinates[1])


class Field:
    x_current, y_current = search_start(matrix)
    finished = False

    def __init__(self, array):
        self.field = []
        for m in range(size):
            a = []
            for n in range(size):
                a.append(Cell(m, n, array[m][n]))
            self.field.append(a)
        print(self.field[Field.x_current][Field.y_current].value)


work_field = Field(matrix)
