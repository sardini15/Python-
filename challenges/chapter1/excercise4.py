# 分数電卓


from fractions import Fraction

def add(a, b):
    print(f'{a} + {b} = {a + b}')

def subtract(a, b):
    print(f'{a} - {b} = {a - b}')

def multiply(a, b):
    print(f'{a} * {b} = {a * b}')

def devide(a, b):
    print(f'{a} / {b} = {a / b}')


if __name__ == '__main__':
    try:
        a = Fraction(input('Enter first fraction: '))
        b = Fraction(input('Enter second fraction: '))
        op = input('Operation to perform - Add, Subtract, Multiply, Devide: ')
        if op == 'Add':
            add(a, b)
        elif op == 'Subtract':
            subtract(a, b)
        elif op == 'Multiply':
            multiply(a, b)
        elif op == 'Devide':
            devide(a, b)
        else:
            print('Invalid operation')
    except ValueError:
            print('You entered an invalid number')