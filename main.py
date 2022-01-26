def check():
    while True:
        x=int(input('Введите начальное значение = '))
        if x>0:
            break
        print('Недопустимое значение')
    return x

def x2(x):
    x = int(x / 2)
    collatz(x)

def x3_1(x):
    x = int(x * 3 + 1)
    collatz(x)
