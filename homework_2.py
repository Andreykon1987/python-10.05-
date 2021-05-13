list = list(range(1, 1001, 2))
for i in range(len(list)):
    list[i] **= 3

summ = 0
summ_17 = 0
y = 0

for numbers in list:
    sumnumber = 0
    while numbers > 0:
        number = numbers % 10
        sumnumber += number
        numbers = numbers // 10
    if sumnumber % 7 == 0:
        summ = summ + list[y]
    y += 1

for i in range(len(list)):
    list[i] += 17

summ_17 = 0
x = 0
for numbers_17 in list:
    sumnumber_17 = 0
    while numbers_17 > 0:
        number_17 = numbers_17 % 10
        sumnumber_17 += number_17
        numbers_17 = numbers_17 // 10
    if sumnumber_17 % 7 == 0:
        summ_17 = summ_17 + list[x]
    x += 1

print(summ)
print(summ_17)

