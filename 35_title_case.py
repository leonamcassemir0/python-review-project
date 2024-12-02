def title(text):
    texto_final = ''

    for i in range(len(text)):
        if i == 0:
            texto_final += text[i].upper()
        elif text[i].isalpha() and not text[i - 1].isalpha():
            texto_final += text[i].upper()
        else:
            texto_final += text[i].lower()

    return texto_final


print(title("leonam cassemiro"))
print(title('Teste teste'))
print(title('teste2python'))