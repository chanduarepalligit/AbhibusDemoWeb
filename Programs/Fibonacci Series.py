# Fibonacci = 0,1,1,2,3,5,8 = addition of preceding 2 values is equal to next value i.e 2,3,5 --> 2+3 = 5

num = 5
first = 1
second = 2
for i in range(num):
    print(first)
    temp = first
    first = second
    second = second + temp