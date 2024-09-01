# Напишите функцию группового переименования файлов. Она должна:
#   принимать параметр желаемое конечное имя файлов.
#   При переименовании в конце имени добавляется порядковый номер.
#   принимать параметр количество цифр в порядковом номере.
#   принимать параметр расширение исходного файла.
#   Переименование должно работать только для этих файлов внутри каталога.
#   принимать параметр расширение конечного файла.
#   принимать диапазон сохраняемого оригинального имени.
#   Например для диапазона [3, 6] берутся буквы с 3 по 6
#   из исходного имени файла. К ним прибавляется желаемое
#   конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os
from typing import List


def bulk_rename(
        directory: str,
        new_name: str,
        digits: int,
        original_extension: str,
        new_extension: str,
        name_slice: List[int]
) -> None:
    """
    Функция для группового переименования файлов в указанной директории.

    :param directory: Директория, содержащая файлы для переименования.
    :param new_name: Новое имя файла. В конце имени добавляется порядковый номер.
    :param digits: Количество цифр в порядковом номере.
    :param original_extension: Расширение исходных файлов, которые нужно переименовать.
    :param new_extension: Расширение конечных файлов после переименования.
    :param name_slice: Диапазон сохраняемого оригинального имени [начало, конец].
    """
    # Получение списка файлов в директории с указанным расширением
    files = [f for f in os.listdir(directory) if f.endswith(original_extension)]

    # Проверка диапазона сохраняемого оригинального имени
    start, end = name_slice
    if start < 0 or end < 0 or start > end:
        raise ValueError("Invalid name_slice range. Ensure start <= end and both are non-negative.")

    # Счётчик для добавления порядкового номера
    counter = 1

    for filename in files:
        # Сохранение оригинального имени в заданном диапазоне
        original_part = filename[start:end]

        # Формирование нового имени файла
        counter_str = str(counter).zfill(digits)  # Добавляем ведущие нули
        new_filename = f"{original_part}{new_name}{counter_str}.{new_extension}"

        # Переименование файла
        old_filepath = os.path.join(directory, filename)
        new_filepath = os.path.join(directory, new_filename)
        os.rename(old_filepath, new_filepath)

        counter += 1

    print("Файлы успешно переименованы.")


