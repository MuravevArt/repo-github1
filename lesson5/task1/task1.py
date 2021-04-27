"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

file_name = input("Введите имя файла: ") + ".txt"
f_obj = open(file_name, 'w', encoding='utf-8')
lines = []
while True:
    line = input("Введите данные или нажмите Enter для завершения: ")
    if line != '':
        lines.append(line + "\n")
    else:
        break
f_obj.writelines(lines)
f_obj.close()
