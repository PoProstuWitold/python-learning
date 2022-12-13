# limit ← 1000000000        // arbitrary search limit

# // set of wheel "hit" positions for a 2/3/5 wheel rolled twice as per the Atkin algorithm
# s ← {1,7,11,13,17,19,23,29,31,37,41,43,47,49,53,59}

# // Initialize the sieve with enough wheels to include limit:
# for n ← 60 × w + x where w ∈ {0,1,...,limit ÷ 60}, x ∈ s:
#     is_prime(n) ← false

# // Put in candidate primes:
# //   integers which have an odd number of
# //   representations by certain quadratic forms.
# // Algorithm step 3.1:
# for n ≤ limit, n ← 4x²+y² where x ∈ {1,2,...} and y ∈ {1,3,...} // all x's odd y's
#     if n mod 60 ∈ {1,13,17,29,37,41,49,53}:
#         is_prime(n) ← ¬is_prime(n)   // toggle state
# // Algorithm step 3.2:
# for n ≤ limit, n ← 3x²+y² where x ∈ {1,3,...} and y ∈ {2,4,...} // only odd x's
#     if n mod 60 ∈ {7,19,31,43}:                                 // and even y's
#         is_prime(n) ← ¬is_prime(n)   // toggle state
# // Algorithm step 3.3:
# for n ≤ limit, n ← 3x²-y² where x ∈ {2,3,...} and y ∈ {x-1,x-3,...,1} //all even/odd
#     if n mod 60 ∈ {11,23,47,59}:                                   // odd/even combos
#         is_prime(n) ← ¬is_prime(n)   // toggle state

# // Eliminate composites by sieving, only for those occurrences on the wheel:
# for n² ≤ limit, n ← 60 × w + x where w ∈ {0,1,...}, x ∈ s, n ≥ 7:
#     if is_prime(n):
#         // n is prime, omit multiples of its square; this is sufficient 
#         // because square-free composites can't get on this list
#         for c ≤ limit, c ← n² × (60 × w + x) where w ∈ {0,1,...}, x ∈ s:
#             is_prime(c) ← false

# // one sweep to produce a sequential list of primes up to limit:
# output 2, 3, 5
# for 7 ≤ n ≤ limit, n ← 60 × w + x where w ∈ {0,1,...}, x ∈ s:
#     if is_prime(n): output n

def sieveOfAtkin(limit):
    print('Limit wynosi: {}'.format(limit))

    if limit > 10000:
        answer = pickYorN('Whoa, whoa, whoa! Jesteś pewny...? (Y/n) ', 'Musisz wybrać "y" lub "n" ')
        if answer != 'y':
            return
        

    # 2 and 3 are prime numbers
    
    print('Liczby pierwsze z przedziału: [2, {}]\n'.format(limit))
    if limit > 2:
        print(2, end=" ")
    if limit > 3:
        print(3, end=" ")

    # Initialise the sieve
    # array with False values
    sieve = [False] * (limit + 1)
    for i in range(0, limit + 1):
        sieve[i] = False
 
    '''Mark sieve[n] is True if
    one of the following is True:
    a) n = (4*x*x)+(y*y) has odd
    number of solutions, i.e.,
    there exist odd number of
    distinct pairs (x, y) that
    satisfy the equation and
    n % 12 = 1 or n % 12 = 5.
    b) n = (3*x*x)+(y*y) has
    odd number of solutions
    and n % 12 = 7
    c) n = (3*x*x)-(y*y) has
    odd number of solutions,
    x > y and n % 12 = 11 '''

    x = 1
    while x * x <= limit:
        y = 1
        while y * y <= limit:
 
            # Main part of Sieve of Atkin
            n = (4 * x * x) + (y * y)
            if (n <= limit and (n % 12 == 1 or
                                n % 12 == 5)):
                sieve[n] ^= True
 
            n = (3 * x * x) + (y * y)
            if n <= limit and n % 12 == 7:
                sieve[n] ^= True
 
            n = (3 * x * x) - (y * y)
            if (x > y and n <= limit and
                    n % 12 == 11):
                sieve[n] ^= True
            y += 1
        x += 1
 
    # Mark all multiples of squares as non-prime
    r = 5
    while r * r <= limit:
        if sieve[r]:
            for i in range(r * r, limit+1, r * r):
                sieve[i] = False
 
        r += 1
 
    # Print primes using sieve[]
    for a in range(5, limit+1):
        if sieve[a]:
            print(a, end=" ")


def possitiveInt(msg, successMsg, errMsg):
    goodinput = False
    while not goodinput:
        try:
            number = int(input(msg))
            if number > 0:
                goodinput = True
                print(successMsg)
                return number
            else:
                print(errMsg)
        except ValueError:
            print(errMsg)

def pickYorN(msg, errMsg):
    goodinput = False
    while not goodinput:
        try:
            answer = input(msg)
            if answer.lower() == 'y' or answer.lower() == 'n':
                goodinput = True
                return answer
            else:
                print(errMsg)
        except ValueError:
            print(errMsg)

limit = possitiveInt(
    "Podaj całkowity dodatni limit: ", 
    "Podałeś prawidłowy numer", 
    "Podany numer jest nieprawidłowy. Spróbuj ponownie: "
)

sieveOfAtkin(limit)