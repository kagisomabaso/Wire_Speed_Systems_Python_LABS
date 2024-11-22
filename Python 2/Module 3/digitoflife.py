dob = input("Enter your date of birth: ")

def calc(string):
    total = 0
    for digit in string:
        total += int(digit)

    if len(str(total)) > 1:
        return calc(str(total))

    return total

print(calc(dob))
