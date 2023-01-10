import re
import requests
import os
import dotenv

dotenv.load_dotenv()

def zipcode_results():
    kod = input('Podaj kod pocztowy: ')

    # RegEx
    wynik = re.fullmatch('[0-9][0-9]-[0-9][0-9][0-9]', kod)
    wynik = re.fullmatch('[0-9]{2}-[0-9]{3}', kod)

    if wynik != None:
        print('Kod prawidłowy')
        print('Ładowanie wyników...')

        url = 'https://polish-zip-codes1.p.rapidapi.com/{}'.format(kod)

        headers = {
            "Accept": "application/json",
            "X-RapidAPI-Key": os.getenv('RAPID_API_KEY'),
            "X-RapidAPI-Host": "polish-zip-codes1.p.rapidapi.com"
        }

        response = requests.request('GET', url, headers=headers)

        print(response.text)
    else:
        print('Kod nieprawidłowy')

zipcode_results()



# # 1. first_name (required), middle_name (optional), last_name (required)
# fullname = input('Podaj imie (wymagane), drugie imie (opcjonalne) i nazwisko (wymagane): ')

# fullname_result = re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?( [A-Za-z]{2,25})', fullname)
# print('Poprawne dane: {}'.format(fullname_result.string)) if fullname_result and fullname_result.string else print('Niepoprawne dane')


# # # 2. email
# email = input('Podaj email: ').lower()

# email_result = re.fullmatch('(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)', email)
# print('Poprawny email: {}'.format(email_result.string)) if email_result and email_result.string else print('Niepoprawny email')


# # 3. correct
# # a) int
# # b) float
# correct_int = input('Podaj liczbe calkowita: ')
# correct_int_result = re.fullmatch('[+-]?([0-9])+', correct_int)
# print('Poprawna liczba calkowita: {}'.format(correct_int_result.string)) if correct_int_result and correct_int_result.string else print('Niepoprawna liczba calkowita')

# correct_float = input('Podaj liczbe rzeczywista: ')
# correct_float_result = re.fullmatch('[+-]?([0-9]*[.])?[0-9]+', correct_float)
# print('Poprawna liczba rzeczywista: {}'.format(correct_float_result.string)) if correct_float_result and correct_float_result.string else print('Niepoprawna liczba rzeczywista')

# # 4. adress - street/village (required), house number (required)/flat number (optional)
# # Grunwaldzka 4/6
# # Grunwald 6

# # 5. phone number in PL (starts with +48)
# phone_number = input('Podaj numer telefonu PL: ')
# correct_phone_number = re.fullmatch('[0-9]{3}[ ][0-9]{3}[ ][0-9]{3}', phone_number)
# print('Poprawny numer PL: {}'.format(correct_phone_number.string)) if correct_phone_number and correct_phone_number.string else print('Niepoprawny numer PL')