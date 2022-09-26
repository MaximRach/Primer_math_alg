import matplotlib.pyplot as plt
import numpy as np
from sympy import * 
#получение таблицы значений из файла
#в файле первая строка x, вторая y
tabl_znach=[]
with open("tabl_znach.txt") as file_object:
    for line in file_object:
        tabl_znach.append(line.split())
x=[float(elem)for elem in tabl_znach[0]]
y=[float(elem)for elem in tabl_znach[1]]
#Параметры окна отображения графиков
plt.title("Lab3")
plt.xlabel("X")
plt.ylabel("Y")
legend = []
#Область отображения графиков
fx = np.linspace(x[0]-2,x[-1] + 2, 1000)
#метод наименьших квадратов
c=[]
for m in range(7):
    temp=0
    for i in range(len(x)):
        temp+=x[i]**m
    c.append(temp)

d=[]
for j in range(4):
    temp=0
    for i in range(len(x)):
        temp+=y[i]*(x[i]**j)
    d.append(temp)

def slau(n):
    m=np.array(n, dtype=np.float64)
    for i in range(len(m)):
        j=i+1
        for j in range(len(m)):
            if m[i][i]<m[j][i]:
                m[i],m[j]=m.copy()[j],m.copy()[i]        
    for i in range(len(m)):
        j=0
        for j in range(len(m)):
            if (i!=j):
                k=m[j][i]/m[i][i]
                m[j]=m[j]-k*m[i]
    a=[]
    for i in range(len(m)):
        a.append((m[i][len(m)]/m[i][i]))
    return a

for s in range(3):
    m=[]
    for i in range(s+2):
        m.append([])
        for j in range(s+2):
            m[i].append(c[j+i])
        m[i].append(d[i])
    a=slau(m)
    sm=a[0].copy()
    sm_f=f'y={a[0]}'
    for i in range(s+1):
        sm+=a[i+1]*(fx**(i+1))
        sm_f+=(f"+{a[i+1]}*x^{i+1}")
    print(f"Сглаживающий многочлен степени {s+1}")
    print(sm_f)
    plt.plot(fx, sm, linewidth=2)
    legend.append(f"sm^{s+1}" % sm)

print(m)
#отображение исходных точек
plt.scatter(x, y, color='orange', s=40)

#Полином Ньютона
n = len(x)
k = []
for i in range(n):
    k.append(y[i])
for j in range(1, n):
    for i in range(n-1, j-1, -1):
        k[i] = float(k[i]-k[i-1])/float(x[i]-x[i-j])
#print(k)
rez=0
form="y="
print("Полином Ньютона:")
for i in range(len(k)):
    l=k[i]
    form+=(f"+{k[i]}")
    for j in range(i):
       l*=(fx-x[j])
       form+=(f"*(X-{x[j]})")
    rez+=l
print(form)
plt.plot(fx, rez, linewidth=2)
legend.append(f"N" % rez)
#Полином Лагранжа
def lag(x,y,fx):
    rez=0
    form="y="
    print("Полином Лагранжа:")
    for i in range(len(x)):
        l=y[i]
        form+=(f"+{y[i]}")
        for j in range(len(x)):
            if (i!=j):
                l*=((fx-x[j])/(x[i]-x[j]))
                form+=(f"*(X-{x[j]})/({x[i]-x[j]})")
        rez+=l
    print(form)
    return rez

L=lag(x,y,fx)
plt.plot(fx, L,"--", linewidth=2)
legend.append("L" % L)

#Отображение графиков
plt.legend(legend)#, loc="upper left")
plt.show() 