lst = [1, 2, 3, 4]
summa = 0
while summa < len(lst):
    a = lst[summa]
    summa += 1
    if a // 4:
        print(a * 10)

    else:
        print("to'rga bo'linmidi")