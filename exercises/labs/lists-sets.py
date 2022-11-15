# 1
# n = int(input('Podaj dlugosc tablicy: '))
# tab = [0]*n
# i = 0

# while i < n:
#     tab[i] = float(input('Podaj kolejna liczbe: '))
#     i += 1

# print(max(tab))

# tab.remove(max(tab))

# print(max(tab))

# 2
# n = int(input('Podaj dlugosc tablicy: '))
# tab1 = [0]*n
# tab2 = [0]*2
# tab3 = []

# i = 0
# j = 0

# while i < n:
#     tab1[i] = float(input('Podaj kolejna liczbe: '))
#     i += 1

# while j < 2:
#     tab2[j] = float(input('Podaj {} liczbe przedzialu'.format(j+1)))
#     j += 1


# for el in tab1:
#     if (el >= tab2[0] and el <= tab2[1]) or (el <= tab2[0] and el >= tab2[1]):
#         tab3.append(el)

# print(tab3)


# 3
# tab1 = []
# n = 1
# i = 0

# while n != 0:
#     tab1.append(float(input('Podaj kolejna liczbe: ')))
#     n = tab1[i] 
#     i += 1

# print(tab1)

# tab1.pop()

# for index, el in enumerate(tab1):
#     if tab1[index] == tab1[-index-1]:
#         print('Tablica jest parzysta na indeksie: {}'.format(tab1[index]))
#     else:
#         print('Tablica jest nieparzysta na indeksie: {}'.format(tab1[index]))
#     # print(index, tab1[index])
#     # print(-index-1, tab1[-index-1])


# 4
# tab1 = []
# n = 1
# i = 0

# while n != 0:
#     tab1.append(float(input('Podaj kolejna liczbe: ')))
#     n = tab1[i] 
#     i += 1

# print(tab1)

# tab1.pop()

# for el in tab1:
#     print('Element {} powtarza się {} razy'.format(el, tab1.count(el)))


# 5
# jebać

# Zadania do samodzielnej realizacji [tekstowe]
# 1. Loteria
import random
all_numbers = list(range(1, 40))
winning_numbers = [0]*6
user_numbers = []*6
same_numbers = []*6
i = 0

while i < 6:
    winning_numbers[i] = random.choice(all_numbers)
    all_numbers.remove(winning_numbers[i])
    i += 1

for index, el in enumerate(winning_numbers):
    user_number = int(input('Podaj kolejna liczbe: '))
    user_numbers.append(user_number)

    if user_number in winning_numbers:
        same_numbers.append(user_number)

    


print(all_numbers)
print(winning_numbers)
print(user_numbers)
print(same_numbers)