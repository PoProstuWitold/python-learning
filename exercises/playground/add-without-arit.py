def add(first_number, second_number):
    for i in range(1, second_number + 1):
        first_number = first_number + 1
    return first_number

print(add(5, 7))