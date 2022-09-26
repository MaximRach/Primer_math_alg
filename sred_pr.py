def f(x):
    return ((1+pow(x, 0.5))/(1+4*x+3*x**2))

def integral(a,b,e):
    h=pow(e, 0.5)
    x=a
    sum=0
    while(x<b):
        if (x+h)<b:
           xs=x+h
        else: xs=b
        sum+=h*f((x+xs)/2)
        x=xs
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