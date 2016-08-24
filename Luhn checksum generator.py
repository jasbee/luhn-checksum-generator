def double_item(x):
    x = x * 2
    y = 0

    if x >= 10:
        x = str(x)
        for each in x:
            y = y + int(each)
        return y
    else:
        return x

code = input('Please enter a string of numbers and I will return the check digit and the total before adding the check digit: ')

code = str(code)

code = code[::-1]
code_even = code[1::2]
code_odd = code[::2]

total = 0

for x in code_odd:
    y = int(x)
    total = total + double_item(y)
    
for z in code_even:
    z = int(z)
    total = total + z

check = abs((total % 10) - 10)

print 'Checksum is equal to ' + str(check)
print 'The Luhn total before adding the checksum is equal to ' + str(total)

raw_input('')