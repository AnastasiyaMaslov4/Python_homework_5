# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_str = input("Введите слова через пробел: ")

string_list = my_str.split(" ")

result = []

for word in string_list:
  if "абв" not in word:
    result.append(word)

print(" ".join(result))