def upper(text):
    minus_para_maius = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}

    texto_final = ''

    for caracter in text:
        if caracter in minus_para_maius:
            texto_final += minus_para_maius[caracter]
        else:
            texto_final += caracter

    return texto_final


print(upper('Hello World'))
print(upper('leonam'))
print(upper('tEsTe 123'))