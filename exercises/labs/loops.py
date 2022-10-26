
# 2
# import math

# def get_user_choice(player):
#     choice = None
#     while not(choice):
#         input_value = input("{}, enter number between 10 and 50: ".format(player))
#         if input_value.isnumeric() and int(input_value) >= 10 and int(input_value) <= 50: 
#             input_value = int(input_value)
#             choice = input_value
#             print("{} choice is {}".format(player, choice))
#             return choice
#         else:
#             print("Choose number between 10 and 50")

# def show_sqrt_sum(number):
#     sum = 0
#     for i in range(number, 51):
#         sum+=pow(number,2)
#         number+=1
#     print("Sum is: {}".format(sum))
#     return sum

# number = get_user_choice("Witold")
# show_sqrt_sum(number)

# 3
# def get_number_unless(player):
#     number = 0
#     sum = 0
#     dividion = 0
#     while not(sum >= 255) and not(dividion >= 50000):
#         input_value = input("{}, enter integer number: ".format(player))
#         if input_value.isnumeric(): 
#             input_value = int(input_value)
#             number = input_value
#             sum+=number
#             if dividion == 0:
#                 dividion = sum
#             else: 
#                 dividion = dividion * number
#             print("{} choice is {}".format(player, number))
#             print("Sum is {}".format(sum))
#             print("Dividion is {}".format(dividion))
#         else:
#             print("Choose number")
#     if sum >= 255:
#         print("Sum is greater than 255")
#     if dividion >= 50000:
#         print("Iloczyn is greater than 50000")

# get_number_unless("Witold")

# 4
def get_unless_odd(player):
    numbers = []
    odd = 0
    while int(odd) % 2 == 0:
        input_value = input("{}, enter number: ".format(player))
        if input_value.isnumeric(): 
            input_value = int(input_value)
            odd = input_value
            numbers.append(odd)
            print(numbers)
            if not(int(odd) % 2 == 0):
                print("{} choice is {} which is odd number".format(player, odd))
            else:
                print("{} choice is {} which is even number".format(player, odd))
        else:
            print("Choose correct number")

get_unless_odd("Witold")