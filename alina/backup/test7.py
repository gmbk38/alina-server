import random

letters = 'alina'

# for i in range (0,8):
#     command += random.choice(letters)

command = '/' + ''.join([random.choice(letters) for i in range (8)])

print (command)