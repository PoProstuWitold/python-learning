import os

source = "/home/witold/Workspace/python/python-learning/exercises/1-python-course-bro-code/text.txt"
destination = "/home/witold/Workspace/python/python-learning/exercises/destination.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")