# Selection sort Ascending using min and index built-in methods
lst = [1, 41, 3, 11, 2, 10, 10]
for i in range(len(lst) - 1):
    min_val = min(lst[i:])
    min_val_index = lst.index(min_val, i)
    if lst[i] != lst[min_val_index]:
        lst[i], lst[min_val_index] = lst[min_val_index], lst[i]
print(lst)

# Selection sort with out using built-in methods
lst = [23, 11, 12, 19, 8, 2]
for i in range(len(lst)-1):
    val = i
    for j in range(i+1, len(lst)):
        if lst[j] < lst[val]:
            val = j
    if lst[i] != val:
        lst[i], lst[val] = lst[val], lst[i]
print(lst)

# User input list
num = int(input("Enter how many numbers : "))
lst = [int(input("Enter numbers : ")) for x in range(num)]
for i in range(len(lst)-1):
    val = i
    for j in range(i+1, len(lst)):
        if lst[j] > lst[val]:
            val = j
            lst[i], lst[j] = lst[j], lst[i]
print(lst)




