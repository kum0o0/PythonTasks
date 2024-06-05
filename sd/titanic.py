import csv
import os
import random


class CSVProc:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.load_data()
        self.headers = self.data[0]
        self.rows = self.data[1:]

    def load_data(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            return list(reader)

    def Show(self, mode='top', count=5, separator=','):
        if count > len(self.rows):
            count = len(self.rows)
            print("Предупреждение: Недостаточно строк. Выведены все доступные строки.")

        if mode == 'top':
            selected_rows = self.rows[:count]
        elif mode == 'bottom':
            selected_rows = self.rows[-count:]
        elif mode == 'random':
            selected_rows = random.sample(self.rows, count)
        else:
            print("Неверный режим. Доступные режимы: top, bottom, random")
            return

        print(separator.join(self.headers))
        for row in selected_rows:
            print(separator.join(row))

    def Info(self):
        print(f"{len(self.rows)}x{len(self.headers)}")
        for i, header in enumerate(self.headers):
            column_data = [row[i] for row in self.rows]
            non_empty_count = len([cell for cell in column_data if cell != ''])
            data_type = type(column_data[0]).__name__ if non_empty_count > 0 else 'None'
            print(f"{header:<15} {non_empty_count:3}  {data_type}")

    def DelNaN(self):
        self.rows = [row for row in self.rows if all(cell != '' for cell in row)]
        print("Строки с пустыми значениями удалены.")

    def MakeDS(self, train_ratio=0.7):
        random.shuffle(self.rows)
        train_size = int(len(self.rows) * train_ratio)
        train_data = [self.headers] + self.rows[:train_size]
        test_data = [self.headers] + self.rows[train_size:]

        os.makedirs("workdata/Learning", exist_ok=True)
        os.makedirs("workdata/Testing", exist_ok=True)

        with open("workdata/Learning/train.csv", 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(train_data)

        with open("workdata/Testing/test.csv", 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(test_data)




if __name__ == "__main__":
    processor = CSVProc("titanic.csv")
    processor.Show()
    processor.Info()
    processor.DelNaN()
    processor.MakeDS()