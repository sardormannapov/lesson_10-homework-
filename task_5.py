lst = ["Google", "Apple", "Microsoft"]
summa = 0
while summa < len(lst):
    a = summa + 1
    while a < len(lst):
        if len(lst[summa]) > len(lst[a]):
            lst[summa], lst[a] = lst[a], lst[summa]
        a += 1
    summa += 1
print(lst)