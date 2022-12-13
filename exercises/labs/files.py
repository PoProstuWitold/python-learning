from enum import Enum


class InputType(Enum):
    YES = ['tak', 't', 'yes', 'y',  1]
    NO = ['nie', 'n', 'no', 0]


def validated_input(msg, err_message=None):
    value = input(msg)
    local_input_type = None

    while local_input_type == None:
        if value in InputType.YES.value:
            local_input_type = InputType.YES
            return value
        elif value in InputType.NO.value:
            local_input_type = InputType.NO
            return value
        elif value.isnumeric():
            local_input_type = 'number'
            return int(value)
        else:
            value = input(err_message or 'Niepoprawny rodzaj inputa: ')


def posortuj_dane(tab):
    return tab.sort()

def szukaj_binarnie(tab, low, high, value):
    if high >= low:
 
        mid = (high + low) // 2
 
        if tab[mid] == value:
            return mid
 
        elif tab[mid] > value:
            return szukaj_binarnie(tab, low, mid - 1, value)
 
        else:
            return szukaj_binarnie(tab, mid + 1, high, value)
 
    else:
        return -1

def szukaj_klasycznie(tab, value):
    try:
        result = bool(tab.index(value) in tab)
    except ValueError:
        result = False
        
    return result

separator = ","
tab = []


plik_we = open('exercises/labs/wejscie.txt', 'r')
# print('Otwieram plik "{}"...'.format(plik_we.name))


rozbita_tablica = plik_we.read().split(separator)
# print('Wczytuje dane z "{}"...'.format(plik_we.name))


for wartosc in rozbita_tablica:
    tab.append(int(wartosc))


plik_we.close()
# print('Zamykam plik "{}"...'.format(plik_we.name))


# miejsce na kod wykonujacy sortowanie
i = 0
plik_wy = open('exercises/labs/wynik.txt', 'w')
# print('Otwieram plik "{}"...'.format(plik_wy.name))

sortowac = validated_input('Czy chcesz sortować?: ', 'Wybierz poprawną opcje (tak/t/yes/y/1)/(nie/n/no/0): ')
x = validated_input('Podaj element do wyszukania: ')
print("x={}".format(x))

znaleziono = None
if sortowac in InputType.YES.value:
    print('SORTUJĘ...')
    posortuj_dane(tab)
    
    print('SZUKAM BINARNIE...')
    znaleziono = szukaj_binarnie(tab, 0, len(tab)-1, x)
else:
    print('SZUKAM KLASYCZNIE...')
    znaleziono = szukaj_klasycznie(tab, x)

if znaleziono:
    print('Podany element istnieje w tablicy')
else:
    print('Podany element nie istnieje w tablicy')

for wartosc in tab:
    if i == len(tab) -1:
        separator = ''

    plik_wy.write(str(wartosc) + separator)
    i += 1

# print('Zapisuje dane do pliku "{}"...'.format(plik_wy.name))

plik_wy.close()
# print('Zamykam plik "{}"...'.format(plik_wy.name))
