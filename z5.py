num = list(range(1, 21))

h = list(filter(lambda x: x % 2 == 0, num)) # оставляет только четные
u = list(map(lambda x: x + 10, h)) # прибавляет к каждому 10
i = sorted(u, reverse=True) # сортировка по убыванию

print("Изначальный список:", num)
print("Чётные числа:", h)
print("Увеличенные на 10:", u)
print("Отсортированные по убыванию:", i)