# Sum of Digits = if num is 1234, then sum is 10
num = 1234
res = 0
while num > 0:
    digit = num % 10
    res = res + digit
    num = num // 10
print(res)

# Using While loop
def sumOf(num):
    sum = 0
    while num != 0:
        sum = sum + int(num % 10)
        num = int(num // 10)
    return sum
print(sumOf(12345))

# Using Recursion
def sumDigits(no):
    return 0 if no == 0 else int(no%10) + sumDigits(int(no//10))
print(sumDigits(123))