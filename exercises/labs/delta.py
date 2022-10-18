a = float(input("a: "))
b = float(input("b:  "))
c = float(input("c: "))

delta = (b**2) - (4*a*c)

x1 = (-b - delta ** 0.5) / (2 * a)
x2 = (-b + delta ** 0.5) / (2 * a)

print("Formula - a*x**2 + b*x + c == 0")

if delta > 0:
    print(f'''The primes of the quadratic equation/square root of the quadratic equation:
x_1 = {x1}, x_2 = {x2}''')
elif delta == 0:
    print(f'''The primes of the quadratic equation/square root of the quadratic equation:
x1 = x2 = {x2} ''')
else:
    print("No results")