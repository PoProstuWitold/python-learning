from enum import Enum

class InputType(Enum):
    POS_INT = 1
    OCENA_STUDENCKA = 2

def validated_input(msg, err_message, input_type):
    value = input(msg)
    local_input_type = None

    while True:
        if input_type == InputType.OCENA_STUDENCKA:
            local_input_type = InputType.OCENA_STUDENCKA
            if value.isnumeric() and int(value) >= 2 and int(value) <= 5:
                return int(value)
            else:
                value = input(err_message)
        elif input_type == InputType.POS_INT:
            local_input_type = InputType.POS_INT
            if value.isnumeric() and int(value) > 0:
                return int(value)
            else:
                value = input(err_message)
        else:
            value = input('Niepoprawny rodzaj inputa: ')
            break

def get_oceny(ile_ocen):
    oceny = []
    
    for i in range(0, ile_ocen):
        ocena = validated_input('Podaj {}. ocenę: '.format(i+1), 'Podaj poprawną wartość {}. oceny: '.format(i+1), InputType.OCENA_STUDENCKA)
        oceny.append(ocena)

    return oceny

def passed(oceny):
    for ocena in oceny:
        if ocena < 3:
            return False
    return True

def licz_srednia(oceny):
    sum = 0

    for ocena in oceny:
        sum += ocena
    return sum/len(oceny) 

def wieksze(srednia, oceny):
    tab = []

    for ocena in oceny:
        if ocena >= srednia:
            tab.append(ocena)
    return tab 


ile_ocen = validated_input('Podaj ile ocen chcesz wprowadzić: ', 'Podaj poprawną ilość: ', InputType.POS_INT)
oceny = get_oceny(ile_ocen)
srednia = licz_srednia(oceny)

print('Ile ocen: {}, oceny: {}'.format(ile_ocen, oceny))
print('Semestr zaliczony: {}'.format(passed(oceny)))
print('Średnia: {}'.format(srednia))
print('Większe od średniej: {}'.format(wieksze(srednia, oceny)))