import csv
import argparse
from operator import index
from tabulate import tabulate

def csv_data_preparation(files, report, position_column):
        all_data = []
        for filename in files:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for line_number, row in enumerate(reader):
                    if line_number == 0:
                        required_row = row.index(report)
                        index_position = row.index(position_column)
                    elif line_number != 0:
                        required_data = [row[index_position], row[required_row]]
                        all_data.append(required_data)
        return all_data

def calculate_averages(data):
    final_data = {}
    for row in data:
        try:
            key = row[0]
            value = float(row[1])
            if key not in final_data:
                final_data[key] = [value, 1]
            else:
                final_data[key][0] += value
                final_data[key][1] += 1
        except ValueError:
            continue
    return final_data

def generate_report(averages_data):
        table_data = []
        for key, (total, count) in averages_data.items():
            average = total / count
            table_data.append([index, key, round(average, 2)])

        table_data.sort(key=lambda x: x[2], reverse=True)

        for i in range(len(table_data)):
            table_data[i][0] = i + 1

        return table_data


def process_csv(files, report, position_column='position'):
    all_data = csv_data_preparation(files, report, position_column)
    averages_data = calculate_averages(all_data)
    report_table = generate_report(averages_data)

    headers = [position_column, report]
    print(tabulate(report_table, headers=headers))

    return report_table


def main():
    parser = argparse.ArgumentParser(description='Обработка CSV файла')
    parser.add_argument('--files', nargs='+', required=True, help='Входные CSV')
    parser.add_argument('--report', type=str, required=True, help='Колонка для анализа')

    args = parser.parse_args()
    process_csv(args.files, args.report)


if __name__ == "__main__":
    main()




