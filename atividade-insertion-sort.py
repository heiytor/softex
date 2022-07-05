import random


def insertionSort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = key
    return list


lista = []
for _ in range(30):
    lista.append(random.randint(1, 999))

print(lista)
print(insertionSort(lista))

