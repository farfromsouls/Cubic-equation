from cmath import *

class CubicEq():

    def __roots(x):
        y = set()
        kor1 = x ** (1 / 3)
        kor2 = (x ** (1 / 3)) * (-1 / 2 + (sqrt(3) * 1j) / 2)
        kor3 = (x ** (1 / 3)) * (-1 / 2 - (sqrt(3) * 1j) / 2)
        y.update({kor1, kor2, kor3})
        return y

    def cubic(a, b, c, d):
        y = set()
        if a != 0:
            p = (3 * a * c - b ** 2) / (3 * a ** 2)
            q = (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)
            x1 = CubicEq.__roots(-q / 2 + sqrt((q / 2) ** 2 + (p / 3) ** 3))
            x2= CubicEq.__roots(-q / 2 - sqrt((q / 2) ** 2 + (p / 3) ** 3))
            for i in x1:
                for j in x2:
                    if abs((i * j) + p / 3) <= 0.0000000001:
                        x = i + j - b / (3 * a)
                        print(f'Корень: {x} | Проверка: {abs((i * j) + p / 3)} \nкорень прошел проверку\n')
                        y.add(x)
        else:
            print("отсутствует куб")
        return  ""


try:
    while True:
        a, b, c, d = map(complex, input().split())
        print(CubicEq.cubic(a, b, c, d))
except:
    print('введены не корректные значения')

