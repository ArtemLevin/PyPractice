# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

cranes = int(input("Enter the total number of cranes "))
peter = 0
sergio = 0
kate = 0
Flag = True
while peter <= cranes//6:
    peter +=1
    sergio = peter
    kate = 2*(peter + sergio)
    if (peter + sergio + kate) == cranes:
        print ("Cranes = ", cranes, "Peter = ", peter, "Sergio = ", sergio, "Kate =", kate)
        Flag = False
if Flag:
    print("There is no correct way to divide the number of cranes")