# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped version of a variable can be created
# LEGB rule
# L = Local
# E = Enclosing
# G = Global
# B = Builtin
name = "Bro" # global scope (available inside & outside functions)

def display_name():
    name = "Code"    # local scope (available only inside this function)
    print(name)


display_name()
print(name)