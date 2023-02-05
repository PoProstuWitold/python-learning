# Fibonacci
def fib(n, cache={0: 0, 1: 1}):
    if n not in cache:
        cache[n] = fib(n - 1) + fib(n - 2)
    return cache[n]
n = 50
print("{} wyraz ciągu Fibonacciego wynosi: {}".format(n, fib(n)))

# Bubblesort optimized
def bubbleSort(t):
    n = len(t)
    zakres = n - 1
    przestaw = True
    while przestaw:
        przestaw = False
        for j in range(zakres):
            if t[j] > t[j+1]:
                print(t)
                przestaw = True
                t[j], t[j + 1] = t[j + 1], t[j] 
                zakres = zakres - 1
lista1 = [4, 6, 3, 7, 9, 2]
print('before: ', lista1)
bubbleSort(lista1)
print('after: ', lista1)


# Sort selection
def sortSelection(t):
    for i in range(len(t)-1):
        ind = i
        for j in range(i+1,len(t)):
            if t[j] < t[ind]:
                print(t)
                ind = j
            t[i], t[ind] = t[ind], t[i]
t = [4, 2, 5, 3, 6, 1]
print('before: ', t)
sortSelection(t)
print('after: ', t)