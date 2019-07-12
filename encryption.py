alpha = 'abcdefghijklmnopqrstuvwxyz'
final = ''
my_input = input('enter a message: ')
key = int(input('enter the key value: '))

my_input = my_input.lower()
for x in my_input:
    if x in alpha:
        pos = alpha.find(x)
        pos = (pos + key) % 26
        final += (alpha[pos])

    else:
        final += x

print('your final message is: ' + final)