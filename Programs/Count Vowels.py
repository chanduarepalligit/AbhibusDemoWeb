name = "chandU"
name = name.lower()
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
for i in name:
    if i in vowels:
        count = count+1
print(count)