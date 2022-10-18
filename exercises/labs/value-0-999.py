# number1, number2, number3 = input("Enter 3 values separated by comma: ").split()
# print("Numbers: {}, {}, {}".format(number1, number2, number3))

def get_sum(n):
    
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum

def get_number():
    while True:
        input_value = input("Enter value between 0-999: ")
        if (input_value.isnumeric() and int(input_value) >= 0 and int(input_value) <= 999):
                print("Input value is: {}".format(input_value))
                num = int(input_value)
                hundreds = (num % 1000) // 100
                tens = (num % 100) // 10
                units = (num % 10)
                print("sum of digits: {}, hundreds: {}, tens: {}, units: {}".format(get_sum(num), hundreds, tens, units))
                break
        else:
            print("Please, enter value between 0-999: ")

get_number()