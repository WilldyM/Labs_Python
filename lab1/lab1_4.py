str1 = input("Введите текст:\n")
str1 = str1.split()

for y in str1:
    if len(y) >= 7:
        print(y)
    else:
        continue

for y in str1:
    if len(y) >= 4 and len(y) <= 7:
        print(y)
    else:
        continue

for y in str1:
    if len(y) < 4:
        print(y)
    else:
        continue


