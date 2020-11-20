# Perfect Number - Sum of divisors of numbers --> 6 can be divisible by 1,2,3 i.e sum of all of it's divisors should be
#                    equal to the number

for num in range(3, 30):
    res = 0
    for i in range(1, num):
        if num % i == 0:
            res = res + i
    if num == res:
        print("Perfect Number : ", res)
