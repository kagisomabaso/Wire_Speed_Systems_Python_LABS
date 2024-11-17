def mysplit(string):
    mylist = []
    word = ''
    if string == " ":
        return mylist
    for char in string:
        if char == ' ':
            mylist.append(word)
            word = ''
        else:
            word += char
    mylist.append(word)
    return mylist

print(mysplit('i am the one they love to hate'))
