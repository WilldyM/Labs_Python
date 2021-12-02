debNum = input("Введите номер дебетовой карты: ")
#ind = 0
while len(debNum) != 16 or debNum.isdigit() == False:
    print("Ошибка! Повторите ещё раз!")
    debNum = input("Введите номер дебетовой карты: ")

debNum = debNum[:4] + '*'*12 + debNum[12:]
print(debNum)


#ind = 0
#for i in debNum:
    #if (ind > 3) and (ind < 12):
        #print('*', end='')
    #else:
        #print(i, end='')

    #if ind == 3 or ind == 7 or ind == 11:
        #print(end=' ')

    #ind += 1
