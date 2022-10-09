import os

path = "/home/witold/Workspace/python/python-learning/exercises/1-python-course-bro-code/text.txt"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesn't exist!")