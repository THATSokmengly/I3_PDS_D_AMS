# Problem 10: Prime Numbers and Goldbach's Conjecture
# (a) Create a function to check prime numbers
def is_prime(n):
    # Numbers smaller than 2 are not prime
    if n < 2:
        return False
    # Check divisors from 2 to square root of n
    d = 2

    while d * d <= n:

        if n % d == 0:
            return False
        d = d + 1
    return True

# (b) Print all prime numbers below 50
print("Prime numbers below 50:")
for n in range(2, 50):
    if is_prime(n):
        print(n, end=" ")
print()
# Count prime numbers below 100
count = 0
for n in range(2, 100):
    if is_prime(n):
        count = count + 1
print("Number of primes below 100:", count)

# (c) Goldbach's conjecture
def goldbach(n):
    # Check possible first prime numbers
    for p in range(2, n):
        q = n - p
        # Check whether both numbers are prime
        if is_prime(p) and is_prime(q):
            return (p, q)
    # No pair found
    return None
# Print Goldbach pairs from 4 to 30
print("\nGoldbach pairs:")
for n in range(4, 31, 2):
    pair = goldbach(n)
    if pair is not None:
        p, q = pair
        print(f"{n} = {p} + {q}")
        
# (d) Check Goldbach's conjecture from 4 to 10,000
holds = True
for n in range(4, 10001, 2):
    pair = goldbach(n)
    if pair is None:
        holds = False
        print("Goldbach fails at:", n)
        break
print("\nGoldbach holds for every even number from 4 to 10000:", holds)
