# Armstrong Number = Sum of cubes of all numbers i.e 153 = 1cube + 5cube + 3 cube == 153

for num in range(150, 373):
    k = len(str(num))
    i = num
    res = 0
    while i > 0:
        digit = i % 10
        res = res + digit ** k
        i = i // 10
    if res == num:
        print(num)

# Using Lambda function
for num in range(150, 2000):
    k = len(str(num))
    a = list(map(int, str(num)))
    b = list(map(lambda x: x ** k, a))
    if sum(b) == num:
        print("Armstrong : ", num)
