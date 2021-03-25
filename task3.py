from constants_task3 import *


def search_start(array):
    [x, y] = random.randint(0, size - 1), random.randint(0, size - 1)
    while array[x][y] != 1:
        [x, y] = random.randint(0, size - 1), random.randint(0, size - 1)
    return x, y


class Cell:
    def __init__(self, x, y, value):
        self.routes = {'0': False, '1': False, '2': False, '3': False}
        self.visited = False
        self.value = value


stack = [search_start(matrix)]


class Field:
    i = 0
    x_start, y_start = stack[0]
    x_current, y_current = x_start, y_start

    def __init__(self, array):
        self.field = []
        for m in range(size):
            a = []
            for n in range(size):
                a.append(Cell(m, n, array[m][n]))
            self.field.append(a)


def search():
    work_field = Field(matrix)
    work_field.field[Field.x_start][Field.y_start].visited = True
    while Field.i != -1:
        exist = False
        Field.x_current, Field.y_current = stack[Field.i]
        while 0 <= Field.x_current < size - 1:
            Field.x_current += 1
            if work_field.field[Field.x_current][Field.y_current].value == 1:
                stack_current_move.append((Field.x_current, Field.y_current))
                exist = True
                break
        Field.x_current, Field.y_current = stack[Field.i]
        if not exist:
            stack_current_move.append((-1, -1))
        else:
            exist = False

        while 0 < Field.x_current <= size - 1:
            Field.x_current -= 1
            if work_field.field[Field.x_current][Field.y_current].value == 1:
                stack_current_move.append((Field.x_current, Field.y_current))
                exist = True
                break
        Field.x_current, Field.y_current = stack[Field.i]
        if not exist:
            stack_current_move.append((-1, -1))
        else:
            exist = False

        while 0 <= Field.y_current < size - 1:
            Field.y_current += 1
            if work_field.field[Field.x_current][Field.y_current].value == 1:
                stack_current_move.append((Field.x_current, Field.y_current))
                exist = True
                break
        Field.x_current, Field.y_current = stack[Field.i]
        if not exist:
            stack_current_move.append((-1, -1))
        else:
            exist = False

        while 0 < Field.y_current <= 14:
            Field.y_current -= 1
            if work_field.field[Field.x_current][Field.y_current].value == 1:
                stack_current_move.append((Field.x_current, Field.y_current))
                exist = True
                break
        Field.x_current, Field.y_current = stack[Field.i]
        if not exist:
            stack_current_move.append((-1, -1))

        for c in range(len(stack_current_move)):
            x_current, y_current = stack_current_move[c]
            if stack_current_move[c] != (-1, -1):
                if work_field.field[Field.x_current][Field.y_current].routes['0'] and c == 1:
                    continue
                elif work_field.field[Field.x_current][Field.y_current].routes['1'] and c == 0:
                    continue
                elif work_field.field[Field.x_current][Field.y_current].routes['2'] and c == 3:
                    continue
                elif work_field.field[Field.x_current][Field.y_current].routes['3'] and c == 2:
                    continue
                if work_field.field[x_current][y_current].visited:
                    stack.append((x_current, y_current))
                    Field.i = -1
                    break
                else:
                    if c == 0:
                        work_field.field[x_current][y_current].routes['0'] = True
                    elif c == 1:
                        work_field.field[x_current][y_current].routes['1'] = True
                    elif c == 2:
                        work_field.field[x_current][y_current].routes['2'] = True
                    elif c == 3:
                        work_field.field[x_current][y_current].routes['3'] = True

                stack.append(stack_current_move[c])
                Field.i += 1
                stack_current_move.clear()
                work_field.field[x_current][y_current].visited = True
                break


search()
for n in range(len(stack)):
    if n == len(stack) - 1:
        print(format(stack[n]), end=' ')
        break
    print('{}->'.format(stack[n]), end=' ')

a = [[0 for i in range(5)] for j in range(5)]
print(a)
a[1:4, 2] = [1 for i in range(3)]
print(a)
