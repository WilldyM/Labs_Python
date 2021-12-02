pw = input('Введите пароль:')
un = 0
if len(pw) >= 10:
    un += 1
for i in pw:
    if 'A' <= i <= 'Z':
        un += 1
        break
for i in pw:
    if i.isdigit():
        un += 1
        break
for i in pw:
    if 'a' <= i <= 'z':
        un += 1
        break
for i in pw:
    if 'а' <= i <= 'я' or 'А' <= i <= 'Я':
        un += 1
        break

print('Уровень надежности: '+str(un)+'/5')













