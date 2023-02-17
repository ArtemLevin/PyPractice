# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

number = input("Enter the number ")
sum1 = 0
sum2 = 0
for i in number[:3]:
    sum1 += int(i)
for i in number[3:]:
    sum2 += int(i)
if sum1 == sum2:
    print("Yes")
else:
    print("No")
