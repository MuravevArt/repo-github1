# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.

def my_func(*user_nums):
    nums = set(user_nums)
    smallest = min(nums)
    nums.remove(smallest)
    return sum(nums)


result = my_func(int(input("Введите первое число: ")), int(input("Введите второе число: ")),
                 int(input("Введите третье число: ")))
print(result)
