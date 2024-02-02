inp = input("Enter name: ")
lst = ["Sardor", "Mardon", "Firdavs"]
result = 0
while result < len(lst):
    a = lst[result]
    result += 1
    if a == inp:
        lst.remove(a)
        print(lst)