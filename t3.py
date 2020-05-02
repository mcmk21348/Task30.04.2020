a = list(map(int, input('Введите число через пробел: ').split()))
step = int(input('Введите сдвиг: '))


def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())

shift(a, step)
print(a)
    









