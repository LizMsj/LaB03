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
    
def collatz(x):
    if x > 0:
        if x == 1:
            global L
            L.append(x)
            print(L)
        else:
            L.append(x)
            if x % 2 == 0:
                x2(x)
            else:
                x3_1(x)
    else:
        x = int(input('Введите число заново: '))
        collatz(x)

x = int(input('Начальное положительное значение = '))
L = []
collatz(x)
