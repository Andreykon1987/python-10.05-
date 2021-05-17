list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i in range(len(list)):
    if list[i].isdigit():
        list[i] = f'"{int(list[i]):02}"'
    elif list[i].replace('+', '').isdigit():
        list[i] = f'"+{int(list[i]):02}"'

print(' '.join(list))
