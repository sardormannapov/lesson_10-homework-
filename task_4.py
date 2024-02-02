lst = [3, 3, 3, 7, 3, 3]
sm = 0

while sm < len(lst):
    a = lst[sm]
    sm += 1
    if lst.count(a) == 1:
        print(a)
