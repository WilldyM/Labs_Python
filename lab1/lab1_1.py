num = float(input("Введите вещественное число: "))
num1 = int(num)
num2 = round((num - int(num)) * 100)
try: 
    if num<0:
        raise ValueError
except Exception:
    print("Некорректный формат!!!")
else:
    print(str(num1)+" руб. "+str(num2)+" коп.")

