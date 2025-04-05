import re
with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read()
emails = re.findall(r"[\w.-]+@[\w.-]+", text)
phones = re.findall(r"\+7-\d{3}-\d{3}-\d{2}-\d{2}", text)
capital_words = re.findall(r"\b[A-ZА-Я][a-zа-я]+", text)

with open("emails.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(emails))

with open("phones.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(phones))

with open("capital_words.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(capital_words))