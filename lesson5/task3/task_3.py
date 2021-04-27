"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.

Пример файла:

Иванов 23543.12
Петров 13749.32
"""

import json

with open("task_3.json", encoding='utf-8') as read_f:
    data_dict = json.load(read_f)
    print(type(data_dict))
    print("Сотрудники, зарабатывающие менее 20000:")
    for keys, values in data_dict.items():
        if values < 20000:
            print(keys)
    print(f"Средняя заработная плата = {sum(data_dict.values())/len(data_dict)}")
