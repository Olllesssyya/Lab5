#Лабароторна 5 варіант 8 завдання2. Посилання на GitHub https://github.com/Olllesssyya/Lab5
import math
a1=16
a2=20
a3=36
N=int(input("Введіть ціле число:"))
if N%a1==0 and N%a2==0 and N%a3==0:
    print("Відповідь: N - спільне кратне для a1, a2, a3")
else:
    print("Відповідь: N - не є спільним кратним для a1, a2, a3")
