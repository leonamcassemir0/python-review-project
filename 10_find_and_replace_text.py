def findAndReplace(text, oldText, newText):
    replacedText = ' '
    i = 0
    while i < len(text):
        if text[i:i + len(oldText)] == oldText:
            replacedText += newText
            i += len(oldText)
        else:
            replacedText += text[i]
            i += 1
    
    return replacedText


print(findAndReplace('The fox', 'fox', 'dog')) 
print(findAndReplace('fox', 'fox', 'dog'))
print(findAndReplace('Firefox', 'fox', 'dog')) 
print(findAndReplace('foxfox', 'fox', 'dog')) 
print(findAndReplace('The Fox and fox.', 'fox', 'dog')) 
