<<<<<<< HEAD
<<<<<<< HEAD
from pip._vendor.progress import counter
from pipenv.vendor.orderedmultidict import f
=======
>>>>>>> branch
=======
>>>>>>> e487f2b74c4055cb30724a8ecdf27802fb2f3629

print("Задача 6.")
print('Результативность бега.')
first = int(input('Введите начальный результат: '))
last = int(input('Введите желаемый результат: '))
grow = int(input('Введите, на какой процент вы собираетесь увеличивать результат: '))
d = 0
while first <= last:
    d += 1
    print(d, 'день - {:.2f}'.format(first))
    first = first + (first / grow)

print('Вы достигнете желаемого результата', last, 'километров на', d + 1, 'день.')
