# Anagram = Two strings must contains same characters but in different places --> earth & heart
name1 = "chandu"
name2 = "handcua"
if len(name1) == len(name2):
    if sorted(name1) == sorted(name2):
        print("Anagram")
else:
    print("Not an Anagram")

print("anagram" if len(name1) == len(name2) and sorted(name1) == sorted(name2) else "Not anagram")