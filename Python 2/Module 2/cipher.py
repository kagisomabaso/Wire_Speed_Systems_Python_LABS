text = input("Enter a string to cipher:")
n = int(input("Enter num:"))
cipher = ''

for char in text:
    if not char.isalpha():
        cipher += char

    elif char.islower():
        code = ord(char) + n
        if code > ord('z'):
            code = code - 26
        cipher += chr(code)
    else:
        code = ord(char) + n
        if code > ord('Z'):
            code = code - 26
        cipher += chr(code)
print(cipher)


