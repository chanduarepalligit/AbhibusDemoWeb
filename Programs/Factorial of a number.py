# Factorial of a number = 5! = 5*4*3*2*1 = 120    fyi : 0!= 1

# Using Recursion - A function is called inside a function or a function called inside its own function
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
print(fact(5))

# Using While loop
num = 6
res = 1
while num > 0:
    res = res * num
    num -= 1
print(res)

# Using For loop
num = 4
res = 1
for i in range(num, 0, -1):
    res = res * i
print(res)
