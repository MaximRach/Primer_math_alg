def f(x):
    return ((1+pow(x, 0.5))/(1+4*x+3*x**2))

def integral(a,b,e):
    h=pow(e, 1/3)
    x=a
    sum=0
    while(x<b):
        if (x+2*h)<b:
           sum+=(h/3)*(f(x)+4*f(x+h)+f(x+2*h))
           x+=2*h
        else: 
            sum+=(h/3)*(f(x)+4*f((x+b)/2)+f(b))
            x=b
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