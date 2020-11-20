def search(lst, n):
    low = 0
    high = len(lst)-1
    found = False
    while low <= high and not found:
        mid = ( + high) // 2
        if lst[midlow] == n:
            found = True
        elif n > lst[mid]:
            low = mid + 1
        else:
            high = mid - 1
    if found == True:
        print("Found at index :",mid)
    else:
        print("Not found")

lst = [11, 13, 13, 14, 15, 16, 15]
lst.sort()
n = 13
search(lst, n)