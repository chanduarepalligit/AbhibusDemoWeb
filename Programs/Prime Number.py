# Prime Number - The number which is divisible by 1 and itself
import math
for num in range(10, 20):
    if num > 1:
        for j in range(2, num):
            if num % j == 0:
                break
        else:
            print(num)

num = 11
while num % 2 == 0:
    print("not a prime")
    break
else:
    print("Prime")

num = 20
for i in range(num):
    if math.gcd(num, i) == 1:
        print(i)