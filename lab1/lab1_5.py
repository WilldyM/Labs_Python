text = input("Введите текст:\n")
text = text.split(' ')
for string in text:
    if string[0].isupper():
        string = string.upper()
    print(string, end=' ')
