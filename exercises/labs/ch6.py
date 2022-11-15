# Zestaw nr 1


# 2
# from math import pow

# n = int(input('Podaj dlugosc tablicy: '))
# tab = [0]*n
# sum = 0
# i = 0

# while i < n:
#     tab[i] = float(input('Podaj kolejna liczbe: '))
#     sum += pow(tab[i], 2)
#     i += 1

# print(sum)

# 3
# import math
# numbers = []
# num = 0
# while not(num % 10 == 0) or num == 0:
#     num = int(input('Podaj kolejną liczbę'))
#     if not(num % 10 == 0):
#         numbers.append(num)

# print('All numbers: {}'.format(numbers))
# print('Lowest: {}'.format(min(numbers)))
# print('Average: {}'.format(sum(numbers)/len(numbers)))


# 4
# n = int(input('Podaj dlugosc tablicy: '))
# tab = [0]*n
# i = 0

# while i < n:
#     tab[i] = float(input('Podaj kolejna liczbe: '))
#     i += 1

# print(tab)
# def find_biggest(tab, length):
#     if(len(tab) < length):
#         print('Nie ma tylu liczb w tablicy')
#         return None

#     result = []
#     starting_indexes = {}
#     for i in range(length):
#         result.append(max(tab))
#         starting_indexes.update({tab.index(max(tab)): max(tab)})
#         tab.remove(max(tab))
#     print('Wynik: {}'.format(result))
#     print('Początkowe indexy: {}'.format(starting_indexes))
#     print('Najmniejsza wartość: {}'.format(min(result)))
#     return (
#         result,
#         starting_indexes
#     )

# find_biggest(tab, 3)


# Zestaw nr 2
# 3
# import math
# n = int(input('Podaj dlugosc tablicy: '))
# condition = n > 2 and n % 2 == 0
# if not(condition):
#     print('Liczba musi być parzysta i większa od 2')

# tab = [0]*n
# i = 0

# while i < n and condition:
#     tab[i] = float(input('Podaj kolejna liczbe: '))
#     i += 1

# middle_index_f = math.floor((len(tab) - 1)/2)
# middle_index_c = math.ceil((len(tab) - 1)/2)
# print(tab)
# print(middle_index_f)
# print(middle_index_c)

# average = (tab[middle_index_f]+tab[middle_index_c])/2

# print('Średnia środkowych liczb: {}'.format(average))



# 4
n = int(input('Podaj dlugosc tablicy: '))
condition = n > 2 and n % 2 == 0
tab = [0]*n
i = 0

def get_number(index):
        input_value = input("Enter {} value between 1-100: ".format(index))
        if (input_value.isnumeric() and int(input_value) >= 0 and int(input_value) <= 100):
                print("Input value is: {}".format(input_value))
                input_value = int(input_value)
                return input_value
        else:
            print("Please, enter value between 1-100: ")

def check_if_duplicates(tab):
    if len(tab) == len(set(tab)):
        return False
    else:
        return True

while i < n:
    tab[i] = get_number(i+1)

    if tab[i] != None:
        i += 1
  
print('Duplikaty? {}'.format(check_if_duplicates(tab)))


# Zestaw nr 3
#