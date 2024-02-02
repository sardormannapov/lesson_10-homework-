lst = [1, 2, 3, 4, 5]
lst2 = [0, 1, 2, 3, 4]
result = 0
summa = 0
summa2 = 0
while summa < len(lst) and summa2 < len(lst2):
    a = lst[summa]
    b = lst2[summa2]
    summa += 1
    summa2 += 1
    result += a * b
print(result)