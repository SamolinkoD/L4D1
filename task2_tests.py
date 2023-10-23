from task2 import sum_lower_than

def test_positive_case():
    ls1 = [1, 2, 3, 4, 5]
    ls2 = [4, 5, 6, 7, 8]
    not_more = 5
    result = sum_lower_than(ls1, ls2, not_more)
    expected_result = [1, 2, 3, 4, 5]
    assert result == expected_result, f"Позитивний тест не пройдено. Отримано: {result}, Очікувано: {expected_result}"
    return "Позитивний тест пройдено."

def test_negative_case():
    ls1 = [6, 7, 8]
    ls2 = [9, 10, 11]
    not_more = 5
    result = sum_lower_than(ls1, ls2, not_more)
    expected_result = []
    assert result == expected_result, f"Негативний тест не пройдено. Отримано: {result}, Очікувано: {expected_result}"
    return "Негативний тест пройдено."

def test_inclusion_case():
    ls1 = [1, 2, 3, 4]
    ls2 = [3, 4, 5]
    not_more = 5
    result = sum_lower_than(ls1, ls2, not_more)
    expected_result = [1, 2, 3, 4, 5]
    assert result == expected_result, f"Тест на включення не пройдено. Отримано: {result}, Очікувано: {expected_result}"
    return "Тест на включення пройдено."

def test_empty_lists_case():
    ls1 = []
    ls2 = []
    not_more = 10
    result = sum_lower_than(ls1, ls2, not_more)
    expected_result = []
    assert result == expected_result, f"Тест на порожні списки не пройдено. Отримано: {result}, Очікувано: {expected_result}"
    return "Тест на порожні списки пройдено."

def test_large_data_case():
    ls1 = list(range(1, 1000001))
    ls2 = list(range(1000001, 2000001))
    not_more = 1500000
    result = sum_lower_than(ls1, ls2, not_more)
    expected_length = 1500000
    assert len(result) == expected_length, f"Тест на велику кількість даних не пройдено. Отримано довжину: {len(result)}, Очікувано: {expected_length}"
    return "Тест на велику кількість даних пройдено."


print(test_positive_case())
print(test_negative_case())
print(test_inclusion_case())
print(test_empty_lists_case())
print(test_large_data_case())