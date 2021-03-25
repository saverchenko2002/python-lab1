from constants_task3_lvlup import *


def start_point(array):
    [x, y] = np.random.randint(0, size - 1), np.random.randint(0, size - 1)
    while array[x, y] != 1:
        [x, y] = np.random.randint(0, size - 1), np.random.randint(0, size - 1)
    return x, y


class Cell:
    def __init__(self, x, y, value):
        self.routes = {'R': True, 'L': True, 'D': True, 'U': True}
        self.visited = False
        self.value = value

    def __repr__(self):
        return str(self.value)


single_points = [start_point(matrix)]


class Field:
    count = 0
    prev_move = list()
    x_current, y_current = single_points[0]

    def __init__(self, array):
        self.field = [[Cell(i, j, array[i, j]) for j in range(size)] for i in range(size)]
        self.field = np.asarray(self.field)

    def __repr__(self):
        line = ""
        for i in range(size):
            line += "{}\n".format(self.field[i])
        return line


def search():
    work_field = Field(matrix)
    print('{}->'.format(single_points[0]))
    while True:
        prev_iter_count = Field.count
        if single_points[0] == single_points[len(single_points) - 1] and len(single_points) != 1:
            break
        while 0 <= Field.y_current < size - 1:
            Field.y_current += 1
            if work_field.field[Field.x_current, Field.y_current].value == -1 or work_field.field[Field.x_current, Field.y_current].visited:
                work_field.field[single_points[Field.count]].routes['R'] = False
                Field.y_current = single_points[Field.count][1]
                break
            elif work_field.field[Field.x_current, Field.y_current].value == 1 and \
                    work_field.field[Field.x_current, Field.y_current].routes['R'] and not work_field.field[Field.x_current, Field.y_current].visited:
                single_points.append((Field.x_current, Field.y_current))
                work_field.field[Field.x_current, Field.y_current].visited = True
                Field.count += 1
                for i in work_field.field[Field.x_current, single_points[Field.count - 1][1] + 1:single_points[Field.count][1]]:
                    i.value = -1
                work_field.field[single_points[Field.count - 1]].routes['R'] = False
                work_field.field[single_points[Field.count]].routes['L'] = False
                Field.prev_move.append('R')
                break
            elif Field.y_current == size - 1 and work_field.field[Field.x_current, Field.y_current].value != 1:
                work_field.field[single_points[Field.count]].routes['R'] = False
                Field.y_current = single_points[Field.count][1]
                break
        while 0 < Field.y_current <= size - 1:
            Field.y_current -= 1
            if work_field.field[Field.x_current, Field.y_current].value == -1 or work_field.field[Field.x_current, Field.y_current].visited:
                work_field.field[single_points[Field.count]].routes['L'] = False
                Field.y_current = single_points[Field.count][1]
                break
            elif work_field.field[Field.x_current, Field.y_current].value == 1 and \
                    work_field.field[Field.x_current, Field.y_current].routes['L'] and not work_field.field[Field.x_current, Field.y_current].visited:
                single_points.append((Field.x_current, Field.y_current))
                Field.count += 1
                for i in work_field.field[Field.x_current, single_points[Field.count][1] + 1:single_points[Field.count - 1][1]]:
                    i.value = -1
                work_field.field[single_points[Field.count - 1]].routes['L'] = False
                work_field.field[single_points[Field.count]].routes['R'] = False
                Field.prev_move.append('L')
                break
            elif Field.y_current == 0 and work_field.field[Field.x_current, Field.y_current].value != 1:
                work_field.field[single_points[Field.count]].routes['L'] = False
                Field.y_current = single_points[Field.count][1]
                break
        while 0 <= Field.x_current < size - 1:
            Field.x_current += 1
            if work_field.field[Field.x_current, Field.y_current].value == -1 or work_field.field[Field.x_current, Field.y_current].visited:
                work_field.field[single_points[Field.count]].routes['D'] = False
                Field.x_current = single_points[Field.count][0]
                break
            elif work_field.field[Field.x_current, Field.y_current].value == 1 and \
                    work_field.field[Field.x_current, Field.y_current].routes['D'] and not work_field.field[Field.x_current, Field.y_current].visited:
                single_points.append((Field.x_current, Field.y_current))
                Field.count += 1
                for i in work_field.field[single_points[Field.count - 1][0] + 1:single_points[Field.count][0], Field.y_current]:
                    i.value = -1
                work_field.field[single_points[Field.count - 1]].routes['D'] = False
                work_field.field[single_points[Field.count]].routes['U'] = False
                Field.prev_move.append('D')
                break
            elif Field.x_current == size - 1 and work_field.field[Field.x_current, Field.y_current].value != 1:
                work_field.field[single_points[Field.count]].routes['D'] = False
                Field.x_current = single_points[Field.count][0]
                break
        while 0 < Field.x_current <= size - 1:
            Field.x_current -= 1
            if work_field.field[Field.x_current, Field.y_current].value == -1 or work_field.field[Field.x_current, Field.y_current].visited:
                work_field.field[single_points[Field.count]].routes['U'] = False
                Field.x_current = single_points[Field.count][0]
                break
            elif work_field.field[Field.x_current, Field.y_current].value == 1 and \
                    work_field.field[Field.x_current, Field.y_current].routes['U'] and not work_field.field[Field.x_current, Field.y_current].visited:
                single_points.append((Field.x_current, Field.y_current))
                Field.count += 1
                for i in work_field.field[single_points[Field.count][0] + 1:single_points[Field.count - 1][0], Field.y_current]:
                    i.value = -1
                work_field.field[single_points[Field.count - 1]].routes['U'] = False
                work_field.field[single_points[Field.count]].routes['D'] = False
                Field.prev_move.append('U')
                break
            elif Field.x_current == size - 1 and work_field.field[Field.x_current, Field.y_current].value != 1:
                work_field.field[single_points[Field.count]].routes['U'] = False
                Field.x_current = single_points[Field.count][1]
                break
        if prev_iter_count == Field.count:
            work_field.field[Field.x_current, Field.y_current].visited = False
            Field.count -= 1
            Field.x_current = single_points[Field.count][0]
            Field.y_current = single_points[Field.count][1]
            x, y = single_points.pop()
            work_field.field[single_points[Field.count]].routes[Field.prev_move.pop()] = False
            if x == single_points[Field.count][0]:
                if y > single_points[Field.count][1]:
                    for i in work_field.field[x, single_points[Field.count][1]+1:y]:
                        i.value = 0
                if y < single_points[Field.count][1]:
                    for i in work_field.field[x, y+1:single_points[Field.count][1]]:
                        i.value = 0

            if y == single_points[Field.count][1]:
                if x > single_points[Field.count][0]:
                    for i in work_field.field[single_points[Field.count][0]+1:x, y]:
                        i.value = 0
                if y < single_points[Field.count][1]:
                    for i in work_field.field[x+1:single_points[Field.count][0], y]:
                        i.value = 0
        print(single_points)


search()
print(single_points)

# for i in main_field.field[2, 1:4]:
#     i.value = 1
#
# for i in main_field.field[::2, 1:4]:
#     for j in i:
#         j.value = 1
# print(main_field)


#
# a = np.asarray([[0 for i in range(5)] for j in range(5)])
# print(a)
# a[1:4, 2] = [1 for i in range(3)]
# a[2, 1:4] = 1
#
# print(a)
