import random 
import pyperclip

lowercase = 'qwertyuiopasdfghjklzxcvbnm'
uppercase = 'QWERTYUIOPASDFGHJKLZXCVBNM'
numbers = '1234567890'
symbols = '!@#$%^&*()"><?/.,'

passLen = int(input('Enter pass lengt: '))

password = None
separator = ""

password_symbols = []


vocabulary = lowercase + uppercase + numbers + symbols



for i in range (1, passLen):
    symbol = random.choice(vocabulary)
    password_symbols.append(symbol)

password = "".join(password_symbols)

print(password)

pyperclip.copy(password)

print('Text copied to clipboard!')