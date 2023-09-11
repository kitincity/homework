# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)

from random import randint
from itertools import product

class Matrix:

    def __init__(self, height, width):
        self.data = [[None for _ in range(width)] for _ in range(height)]
        self.height = height
        self.width = width

    def __str__(self):
        return "\n".join(map(str, self.data))

    def __repr__(self):
        return f'{self.__class__.__name__}({self.height!r}, {self.width!r})'

    def len(self):
        print('Количество строк ',len(self.data))
        print('Количество столбцов ',len(self.data[0]))


    def remove(self, item):
        return

    def fill(self, fill_list):
        values = iter(fill_list)

        indices = product(range(self.height), range(self.width))

        for (i, j), value in zip(indices, values):
            self.data[i][j] = value

        return values

   
    
    def replace(self,row_index,column_index,value):
        
        self.data[row_index][column_index] = value

myMat = Matrix(10,10)
overflow = myMat.fill([randint(1,10) for i in range(100)])

print(myMat)
myMat.len()
myMat.replace(2,2,777)
print(myMat)

