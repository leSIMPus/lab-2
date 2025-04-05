try: # используем try чтобы создать такую структуру как исключения в принципе
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    result = a / b
except ZeroDivisionError:
    print("Ошибка: деление на ноль")  # собственно первое исключение
except ValueError:
    print("Ошибка: введите числовое значение")
else:
    print("Результат деления:", result)