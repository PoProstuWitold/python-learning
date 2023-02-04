# 1. Po wykonaniu poniższych instrukcji:
for a in range(1,40,2):
    pass
# print(a)
x = a // 5
x = x - 5 % 3 /2
print(x)
# 6.0


# 2. Dana jest funkcja
def f(n):
    if n >= 0:
        print(chr(ord("a")+n), end="")
        f(n-1)
        print(chr(ord("a")+n), end="")
# Jej wykonanie dla n = 2 spowoduje wyświetlenie:
# Uwaga: wpisać ciąg znaków bez spacji
n = 2
f(n)
print("\n")
# cbaabc


# 3. Dany jest ciąg instrukcji
a, b = 0, 1
m = 4
while b < m:
    print(b)
    a, b = b, a + b
# 1 1 2 3

# 4. wartość dziesiętna liczby 5B (zapisanej heksadecymalnie) wynosi:
# Convert hexadecimal 5B to decimal
# 91


# 5. Co należy wpisać w miejsce ###, by na skutek wykonywania kodu:
def f1(n):
    for j in range(n):
        print()
        for i in range(n-j): # xxx
            print(i+1, end="")
f1(4)


# 6. ZA TRUDNE
# 7. ZA TRUDNE


# 8. Najmniejsza liczba ujemna zapisana binarnie w systemie uzupełnieniowym do dwóch na 4 bitach przyjmuje wartość
# -8


# 9. ZA TRUDNE


# 10. Dana jest funkcja
def bin(m):
    if m == 1:
        print(1, end="")
    else:
        print(m % 2, end="")
        bin(m//2)
bin(11)
# 11101


# 11. Która linia kodu poprawnie wywołuje zdefiniowaną funkcję
def fun(a, b = 1, c = 0):
    pass

# fun(a=1, b=0, c=0)
# fun(1, c=1, b=0)
# fun(a=0, b=0)


# 12. Wykonanie poniższego kodu nie zgłosi błędu
# from math import sin, pi

# def sin(x):
#     if 2 * x == pi:
#         return 1.0
#     else:
#         return None

# print(sin(math.pi/2))
# Fałsz

# 13. Dla danych liczby rzeczywistej dodatniej x i liczby całkowitej n rozważmy algorytm obliczania wartości w = x^n
w = 1
k = n
while k != 0:
    w = w * x
    k = k - 1
# algorytm ten jest algorytem całkowicie poprawnym
# Prawda

# 14. Wynikiem działania kodu będzie:
# def fun1(n):
#     if n % 2 == 0:
#         return 1

# def fun2(n):
#     if n % 3 == 0:
#         return 1

# print(fun1(2)* fun2(1))
# Informacja o błędzie


# 15. Zaznacz poprawne stwierdzenia 
# Przeszukiwanie liniowe jest przykładem algorytmu siłowego, natomiast wyszukiwanie binarne to algorytm "dziel i zwyciężaj"
# Średnia złożoność czasowa algorytmu szybszego sortowania QuickSort jest logarytmczna
# W przypadku posortowanego ciągu liczb wyszukiwanie danego elementu 
# można wykonać za pomocą algorytmu wyszukiwania binarnego o złożoności czasowej logarytmicznej


# 16. Dany jest fragment programu
print('\n')
k = 1
s = 5
for k in range(3,1,-1):
    s -= k
if s:
    print(k)
else:
    print(s)
# 0


# 17. Dopasuj części zdań
# Technika Top-down i Bottom-up:
# to odpowiednio podejście zstępujące, analityczne oraz wstępujące, syntetyczne

# Stosowanie fundamentalnej zasady konstukcyjnej:
# w przypadku języka wysokiego poziomu oznacza w praktyce rezygnację z tzw. instrukcji skoku "goto"a

# Prawo Murphy'ego:
# jeśli udoskonalasz coś dostatecznie długo - na pewno to zepsujesz

# Fundamentalna zasada konstrukcyjna:
# przy budowaniu programu należy ograniczyć się do stosowania instrukcji: pętli dopóki, selekcji dwu...


# 18. 
tab = [7, 6, 2, 4, 8, 1, 2]
def sortowanie_babelkowe(lista):
    n = len(lista)
    
    while n > 1:
        zamien = False
        for l in range(0, n-1):
            if lista[l] > lista[l+1]:
                lista[l], lista[l+1] = lista[l+1], lista[l]
                zamien = True
                
        n -= 1
        print("Iteracja {}, tablica: {}".format(l +1, lista))
        if zamien == False: break
        
    return lista
        
sortowanie_babelkowe(tab)
# 6, 2, 4, 7, 1, 2, 8


# 19. Dany jest wielomian:
# w(x) = 3x^3 + 5x^2 + 8x + 2
# Łączna liczba mnożeń i dodawań potrzebna do obliczenia wartości tego wielomanu za pomocą 
# schematu Hornera wynosi:
def horner_complexity(n):
    multiplications = 0
    additions = 0
    for i in range(n - 1, 0, -1):
        multiplications += 1
        additions += 1
    return multiplications, additions

n = 4
multiplications, additions = horner_complexity(n)
print("Liczba mnożeń:", multiplications)
print("Liczba dodawań:", additions)
print("Łączna liczba mnożeń i dodawań:", multiplications + additions)
# 6


# 20. Instrukcja 
wart = -4
assert wart <= 0
# powoduje zatrzymanie programu w przypadku, gdy wart jest dodatnie
# powoduje zgłoszenie wyjątku, gdy wart jest dodatnie