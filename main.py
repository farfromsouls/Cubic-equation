class CubicEq():
    def __solution(args):
        from numpy import roots
        x = roots(args)
        CubicEq.__check(x, args)
        return x

    def __check(x, args):
        from numpy import around
        a, b, c, d = args[0], args[1], args[2], args[3]
        counter = 0
        for i in x:
            ans = around(a*(i**3) + b*(i**2) + c*i + d)
            if ans == 0.0:
                print(f'x{counter}: {around(i, 2)} - Проверенно')
            counter += 1

    def Solve(*args):
        try:
            if len(args) == 0:
                args = [float(i) for i in input('\nA B C D: ').split()]
                CubicEq.__solution(args)
            else:
                return CubicEq.__solution([args[0], args[1], args[2], args[3]])
        except:
            print('Некорректный ввод')


if __name__ == "__main__":
    while True:
        CubicEq.Solve()
