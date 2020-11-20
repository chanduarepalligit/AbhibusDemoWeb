for num in range(10, 120):
    str_rev = int(str(num)[::-1])
    if num == str_rev:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print("Palindromic Prime : ", num)
