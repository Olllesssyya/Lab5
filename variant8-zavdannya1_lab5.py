#Лабароторна 5 варіант 8 завдання1. Посилання на GitHub https://github.com/Olllesssyya/Lab5
import math
x=float(input("Введіть x:"))
if (x>=7.2):
    f=math.log((math.fabs(x+1)),4)
elif (x>5.11) and (x<7.2):
    f=math.sqrt(math.log10(math.fabs(math.cos(x))))
elif (x<=-5.11):
    f=x**2+4*math.fabs(x-4)+math.pow(math.e,x)
print("Значення функції дорівнює:",f)