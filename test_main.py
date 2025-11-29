import pytest
from main import csv_data_preparation, calculate_averages, generate_report


def test_calculate_averages():
    """Тест расчета средних значений"""
    test_data = [
        ['Mobile Developer', '8'],
        ['Backend Developer', '9'],
        ['Mobile Developer', '9']
    ]

    result = calculate_averages(test_data)

    assert 'Mobile Developer' in result
    assert 'Backend Developer' in result
    assert result['Mobile Developer'] == [17.0, 2]
    assert result['Backend Developer'] == [9.0, 1]


def test_calculate_averages_with_invalid_data():
    """Тест обработки некорректных данных"""
    test_data = [
        ['Data Engineer', '8'],
        ['QA Engineer', 'None'], # Должно пропустить
    ]

    result = calculate_averages(test_data)

    assert 'Data Engineer' in result
    assert 'QA Engineer' not in result


def test_generate_report():
    """Тест генерации отчета"""
    test_data = {
        'Разработчик': [18.0, 2],  # среднее: 9.0
        'Менеджер': [9.2, 1],
        'Аналитик': [7.8, 1]
    }

    result = generate_report(test_data)

    # Проверяем сортировку
    assert result[0][1] == 'Менеджер'  # 9.2 - первое место
    assert result[1][1] == 'Разработчик'  # 9 - второе место
    assert result[2][1] == 'Аналитик'  # 7.8 - третье место

    # Проверяем нумерацию
    assert result[0][0] == 1
    assert result[1][0] == 2
    assert result[2][0] == 3

    # Проверяем значения
    assert result[0][2] == 9.2
    assert result[1][2] == 9.0
    assert result[2][2] == 7.8



if __name__ == "__main__":
    pytest.main([__file__, "-v"])