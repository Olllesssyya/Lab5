#Лабароторна 5 варіант 8 завдання2. Посилання на GitHub https://github.com/Olllesssyya/Lab5
import math
a1=16
a2=20
a3=36
N=int(input("Введіть ціле число:"))
if a1/N%1==0 and a2/N%1==0 and a3/N%1==0:
    print("Відповідь: N - спільне кратне для a1,a 2, a3")
else:
    print("Відповідь: N - не є спільним кратним для a1, a2, a3")
