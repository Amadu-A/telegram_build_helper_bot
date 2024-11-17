import pandas as pd

def compare_excel_files(file1, file2):
    try:
        # Загружаем данные из файлов
        df1 = pd.read_excel(file1, sheet_name=None)
        df2 = pd.read_excel(file2, sheet_name=None)

        # Проверяем, совпадают ли листы
        if df1.keys() != df2.keys():
            return "Файлы имеют разные листы и не могут быть сравнимы."

        differences = []

        # Проводим посрочное сравнение данных по каждому листу
        for sheet_name in df1.keys():
            sheet1 = df1[sheet_name]
            sheet2 = df2[sheet_name]

            # Проверяем, совпадает ли размер таблиц
            if sheet1.shape != sheet2.shape:
                differences.append(f"На листе '{sheet_name}' размеры таблиц отличаются.")
                continue

            # Сравниваем значения ячеек
            for row in range(sheet1.shape[0]):
                for col in range(sheet1.shape[1]):
                    value1 = sheet1.iat[row, col]
                    value2 = sheet2.iat[row, col]

                    # Если значения не равны, добавляем информацию о расхождении
                    if pd.notna(value1) and pd.notna(value2) and value1 != value2:
                        differences.append(f"Лист '{sheet_name}', ячейка ({row + 1}, {col + 1}): "
                                           f"значение в первом файле '{value1}', во втором файле '{value2}'.")

        if differences:
            return "\n".join(differences)
        else:
            return "Файлы прошли сверку, расхождений не найдено."
    except Exception as e:
        return f"Ошибка при обработке файлов: {e}"
