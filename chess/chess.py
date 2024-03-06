__all__ = ['chess_variants']

from random import randint


def chess_check() -> list:
    n = 8
    x = []
    y = []
    for i in range(n):
        new_x = randint(1, 8)
        new_y = randint(1, 8)
        while True:
            if (new_x in x) and (new_y in y) and (x.index(new_x) == y.index(new_y)):
                new_x = randint(1, 8)
                new_y = randint(1, 8)
            else:
                break
        x.append(new_x)
        y.append(new_y)
    flag = True
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                flag = False
    result = []
    for i in range(n):
        result.append((x[i], y[i]))
    result.append(flag)
    return result


def chess_variants(count: int = 4):
    i = 0
    print("Варианты:")
    while i < count:
        variant = chess_check()
        if variant[-1]:
            print(variant[-2::-1])
            i += 1


if __name__ == '__main__':
    chess_variants(4)
