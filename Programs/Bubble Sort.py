lst = []
num = int(input("Enter how many numbers : "))
print("Enter values")
for k in range(num):
    lst.append(int(input()))
for j in range(len(lst)-1):
    for i in range(len(lst)-1-j):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            print(lst)
        else:
            print(lst)
    print()
print(lst)