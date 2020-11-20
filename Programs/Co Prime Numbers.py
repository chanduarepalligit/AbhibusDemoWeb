# Co-Prime numbers = when GCD of 2 numbers is 1, then those 2 numbers are called co-prime numbers
import math


def coPrime(a, b):
    if b == 1:
        return "Co-Prime"
    else:
        return coPrime(b, a % b)


print(coPrime(11, 17))

num1 = 11
num2 = 17
if math.gcd(num1, num2) == 1:
    print("CoPrime numbers")
else:
    print("Not coprime")

# Print all co-prime numbers of specific number
num = 10
for i in range(num):
    if math.gcd(num, i) == 1:
        print(i)
