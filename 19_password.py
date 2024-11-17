import random

minusculas = 'abcdefghijklmnopqrstuvwxyz'
maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '1234567890'
especiais = '~!@#$%^&*()_+'

todos = minusculas + maiusculas + numeros + especiais

def generatePassword(length):
    if length < 12:
        length = 12

    password = []
    password.append(minusculas[random.randint(0, 25)])
    password.append(maiusculas[random.randint(0, 25)])
    password.append(numeros[random.randint(0, 9)])
    password.append(especiais[random.randint(0, 12)])

    while len(password) < length:
        password.append(todos[random.randint(0, 74)])

    random.shuffle(password)

    return ''.join(password)

print(len(generatePassword(8)))

pw = generatePassword(14)
print(len(pw))
print(pw)
print(generatePassword(15))
print(generatePassword(20))
