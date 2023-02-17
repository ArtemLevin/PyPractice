# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = input("Enter the number ")
s = 0
for i in number:
    s += int(i)
print(s)