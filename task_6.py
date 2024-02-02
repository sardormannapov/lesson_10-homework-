inp = input("Enter alphabet: ")
list = [
    ["D", "E", "Y", "H", "A", "D"],
    ["C", "B", "Z", "Y", "J", "K"],
    ["D", "B", "C", "A", "M", "N"],
    ["F", "G", "G", "R", "S", "R"],
    ["V", "X", "H", "A", "S", "S"]
]
lst2 = []

summa = 0
while summa < len(list):
    summa2 = 0
    while summa2 < len(list[summa]):
        if inp == list[summa][summa2]:
            lst2.append(list[summa][summa2])
        summa2 += 1
    summa += 1

print(len(lst2))
