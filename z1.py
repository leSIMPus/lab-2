with open("data.txt", "r") as file: # открываем наш файл только для чтения
    num = [int(line.strip()) for line in file.readlines()] # считываем числа из файла и делаем из них список
    s = sum(num)
    a = s / len(num)
    max = max(num)
    min = min(num)
with open("result.txt", "w", encoding = "utf-8") as file: # используем кодировку чтобы русские букавы были отображаемы и создаем файл результатов
    file.write(f"Сумма: {s}\n")
    file.write(f"Среднее: {a}\n")
    file.write(f"Максимум: {max}\n")
    file.write(f"Минимум: {min}\n")  
