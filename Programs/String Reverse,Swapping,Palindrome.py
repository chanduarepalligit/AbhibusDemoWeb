# Swapping numbers
a = 10
b = 20
a, b = b, a
print(a)
print(b)

# Swapping numbers
a = 20
b = 10
a = a + b
b = a - b
a = a - b
print(a)
print(b)

# String Reverse
data = "chandu"
str_rev = ""
for i in data:
    str_rev = i + str_rev
print(str_rev)

# Palindrome = string reverse should be equal to string --> madam = madam ( reverse )

data = "madam"
str_rev = data[::-1]
if data == str_rev:
    print("Palindrome")
else:
    print("Not a palindrome")