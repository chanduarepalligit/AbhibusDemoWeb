lst = [21, 12, 32, 12, 89, 12]
key = 12
lst2 = []
flag = False
for i in range(len(lst)):
    if key == lst[i]:
        flag = True
        lst2.append(i)
if flag:
    print("Key values found at Index of : ")
    for i in lst2:
        print(i)
else:
    print("key value not found")


pos = -1
def search(lst, n):
    i = 0
    while i<len(lst):
        if lst[i] == n:
            globals()['pos'] = i
            return True
        i += 1
    return False

lst = [23, 11, 32, 56, 79, 10]
n = 11
if search(lst, n):
    print("Found at :",pos)
else:
    print("Not found")

