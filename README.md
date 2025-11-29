echo
Скрипт для обработки csv-файла
Скрипт читает файлы с данными о закрыты задачах и формирует отчеты
Программа анализирует CSV файлы с данными сотрудников и вычисляет средние показатели производительности по должностям


1. Клонируйте репозиторий:
   (Терминал)
git clone https://github.com/yourusername/csv-performance-analyzer.git
cd csv-performance-analyzer

2. Установка зависимостей:
   (Терминал)
pip install -r requirements.txt

3. Использование:
   (Терминал)
python perfomance_avg.py --files employees.csv --report performance

4. Тестирование:
   (Терминал)
pytest
