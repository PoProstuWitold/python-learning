# Ciag fibonacciego
def fib(n, cache={0: 0, 1: 1}):
    if n not in cache:
        cache[n] = fib(n - 1) + fib(n - 2)
    return cache[n]

print(fib(50))

# bubblesort
# def bubbleSort(t):
#     n = len(t)
#     zakres = n - 1
#     przestaw = True
#     while przestaw:
#         przestaw = False
#         for j in range(zakres):
#             if t[j] > t[j+1]:
#                 print(t)
#                 przestaw = True
#                 t[j], t[j + 1] = t[j + 1], t[j] 
#                 zakres = zakres - 1
# lista1 = [4, 6, 3, 7, 9, 2]

# bubbleSort(lista1)
# print(lista1)


def sortSelection(t):
    for i in range(len(t)-1):
        ind = i
        for j in range(i+1,len(t)):
            if t[j] < t[ind]:
                ind = j
            t[i], t[ind] = t[ind], t[i]
def main():
    t = [4, 2, 5, 3, 6, 1]
    print(t)
    sortSelection(t)
    print(t) 

if __name__ == "__main__":
    main()
