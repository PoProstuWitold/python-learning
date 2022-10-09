import os

try:
    with open('exercises/1-python-course-bro-code/text.txt') as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)
    print("That file was not found :(")
finally:
    print(os.getcwd())