# number1, number2, number3 = input("Enter 3 values separated by comma: ").split()
# print("Numbers: {}, {}, {}".format(number1, number2, number3))

def get_numbers(count):
    while True:
        input_values = input("Enter 3 values separated by space: ").split()
        if len(input_values) == count:
            print("Max number is {}".format(max(*input_values)))
            break
        else:
            print("Enter {} valid numbers".format(count))

get_numbers(3)