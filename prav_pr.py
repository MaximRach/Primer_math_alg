def f(x):
    return ((1+pow(x, 0.5))/(1+4*x+3*x**2))

def integral(a,b,e):
    h=e
    x=a
    sum=0
    while(x<b):
        if (x+h)<b:
           x+=h
        else: x=b
        sum+=h*f(x)
    return sum, h

print('Левый предел интегрирования:')
a=float(input())
print('Правый предел интегрирования:')
b=float(input())
print('Необходимая точность:')
e=float(input())
i,h=integral(a,b,e)
print(f'Значение интеграла:{i}')
print(f'Шаг:{h}')