text1 = input("Enter the first: ")
text2 = input("Enter the second: ")

for i in range(len(text1)):
    if text1.upper().count(text1[i]) != text2.upper().count(text1[i]):
        print("Is not anagram")
        break
else:
    print("Is anagram")
