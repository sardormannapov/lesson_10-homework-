lst = [1, 2, 3, 4, 5, 1]
def minimal(msv):
    lst.remove(min(msv))
    print(msv)

minimal(msv=lst)