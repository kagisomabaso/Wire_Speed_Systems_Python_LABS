word = input("Word: ")

if word == '':
    print('Cannot be an empty string')
else:
    for i in range(len(word)):
        if word[i].upper() != word[len(word)-i-1].upper():
            print("Not palindrome")
            break
    else:
        print("Is palindrome")




