from cmath import sqrt

z = 0.000000000001
class CubicEq():

    # возвращает set корней
    def __roots(x):
        y = set()
        root1 = x ** (1 / 3)
        root2 = (x ** (1 / 3)) * (-1 / 2 + (sqrt(3) * 1j) / 2)
        root3 = (x ** (1 / 3)) * (-1 / 2 - (sqrt(3) * 1j) / 2)
        y.update({root1, root2, root3})
        return y

    # возвращает текст с корнями
    def cubic(a, b, c, d):
        # базовая проверка
        ans = ""
        if a == 0:
            return "Отсутствует кубический член уравнения"
        
        # решение
        p = (3 * a * c - b ** 2) / (3 * a ** 2)
        q = (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)
        x1 = CubicEq.__roots(-q / 2 + sqrt((q / 2) ** 2 + (p / 3) ** 3))
        x2= CubicEq.__roots(-q / 2 - sqrt((q / 2) ** 2 + (p / 3) ** 3))

        # проверка и вывод корней
        for i in x1:
            for j in x2:
                x = i + j - b / (3 * a)
                test = abs((i * j) + p / 3) <= 0.00000000000000000000001
                if test:
                    test1 = "Корень прошёл проверку"
                    ans = ans + f'Корень: {x} | Проверка: {abs((i * j) + p / 3)}\n{test1}\n'

                elif abs((i * j) + p / 3) <= z:
                    test1 = "Корень не прошёл проверку"
                    ans = ans + f'Корень: {x} | Проверка: {abs((i * j) + p / 3)}\n{test1}\n'


        return ans


if __name__ == "__main__":
    # главный цикл с проверкой корректности ввода
    #try:
    while True:
        a, b, c, d = [complex(i) for i in input("a b c d: ").split()]
        print(CubicEq.cubic(a, b, c, d))
    #except:
        #print('Некорректный ввод')