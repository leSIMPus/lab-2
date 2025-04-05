import re

with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read()

dates = re.findall(r"\b(\d{2})\.(\d{2})\.(\d{4})\b", text) # ищет даты в изначальном формете

converted_dates = [f"{year}-{month}-{day}" for day, month, year in dates] # преобразует в нужный формат

with open("dates.txt", "w", encoding="utf-8") as f: # записывает их и потом еще и сортирует
    f.write("\n".join(converted_dates))
sorted_dates = sorted(converted_dates, key=lambda date: date)
print("Отсортированные даты:")
for date in sorted_dates:
    print(date)
