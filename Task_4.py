# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

rows = int(input("Enter the number of rows "))
columns = int(input("Enter the number of columns "))
parts = int(input("Enter the number of parts "))
if parts <= (rows*columns) and (parts % rows == 0 or parts % columns == 0):
    print("Yes")
else:
    print("No")