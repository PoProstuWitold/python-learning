# 1. Zaznacz poprawne deklaracje (język Python) DONE
# a
_101 = 0o11
# b
a 1 = 10e1
# c
_a_ = 0x101
# d
1str = 1E0
# _101, _a_


# 2. Wydruk uzyskany po wynokaniu podanych ciągów instrukcji będzie taki sam DONE
# 1
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)
# 2
for j in range(5):
    print(j)
else:
    print("else:", j)
# Fałsz


# 3. Dany jest automat skończony funkcji przejścia DONE
# Alfa      a      b
# -> 0      1      0
# 1 ->      0      1
# Tekst babaa nie zostanie zaakceptowany przez ten automat
# Fałsz


# 4. Znaczenie argumentu pozycyjnego funkcji określane jest przez: DONE
# (c.) pozycję na liście argumentów zajmowaną przez ten argument


# 5. Ciąg instrukcji wyświetli: DONE
def fun(a, b):
    return a ** b
print(fun(a = 2, 3))
# (b.) komunikat o błędzie


# 6. Na skutek wykonania kodu wyświetlone zostanie DONE
def fun(m):
    return '+' * m
print(fun(1) + fun(2))
# (c.) +++


# 7. Po wykonaniu ciągu instrukcji na ekranie zostanie wyświetlone: DONE
def fun(a, b):
    return a ** b ** a
print(fun(b = 3, a = 2))
# 512


# 8. Dana jest funkcja rekurencyjna postaci: DONE
# Funckja ta jest efektywną implementacją 
# wyznaczania kolejnego wyrazu ciągu Fibonacciego
def fib(n):
    if n in (0, 1):
        return n
    return fib(n-1) + fib(n-2)
# Fałsz


# 9. Wprowadzenie bloku try: oznacze, że DONE
# (d.) niektóre instrukcje z tego bloku mogą nie zostać wykonane


# 10. Liczba binarna 01100010 może być zapisana jako DONE
#  (a.) 62 heksadecymalnie (hex)
#  (b.) 98 w systemie dziesiętnym (decimal)


# 12. Na skutek wykonania polecenia DONE
import random
print(dir(random))
# (c.) wyświetlona zostanie lista wszystkich bytów/funkcji modułu random


# 15. Co zostanie wyświetlone po wykonaniu ciągu instrukcji: DONE
x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z
print(x, y, z)
# 1 1 2

# 16. Dopasuj części zdań DONE
# Schemat Homera - służy do obliczania wartości wielomianu
# Wartość wyrażenia równa 0 traktowana jest jako - False
# Struktura algorytmu jest zdeterminowana przez struktury danych, które ten algorytm przetwarza - II zasada Jacksona
# struktura danych opisująca system rzeczywisty powinna odzwiercedlać strukturę tego systemu - I zasada Jacksona


# 17. Liczby całkowite zapisane binarnie w systemie uzupełnień do dwóch na 8 bitach przyjmują wartości z zakresu DONE
# [-128, 127]


# 18. W tablicy zapisano ciąg liczb całkowitych: DONE
# W wyniku sortowania bąbelkowego metodą omówioną na wykładzie w celu posortowania 
# elementów ciągu (rosnąco) wykonano następującą liczbę porównań tych elementów:
def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print('arr', arr)
         
        if not swapped:
            return arr
    return arr

arr = [7, 1, 2, 4, 5]
print(bubbleSort(arr))
# 4


# 19. Dana jest funkcja DONE
def bin(n):
    if n <= 0:
        return None
    if n < 8:
        print(n, end="")
    else:
        print(n % 8, end="")
        bin(n//8)
        print(n % 8, end="")
n = 142
bin(n)
# 61216


# 20. Funkcja o nazwie fun() zaimportowana z modułu "mod": import mod DONE
# wywołanie: mod.fun()