# Задаем начальный массив строк
initial_array = ["abc", "de", "fghi", "j", "klm", "n", "opq"]

# Создаем пустой массив для результата
result_array = []

# Проходим по всем строкам в initial_array
for string in initial_array:
  
  # Проверяем длину строки
  if len(string) <= 3:
    
    # Добавляем строку в result_array, если ее длина меньше или равна 3
    result_array.append(string)

# Выводим result_array
print(result_array)