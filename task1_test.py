import typing
from task1 import add, add_element_to_list, multiple, create_list_of_random_numbers

def test_add_function_annotations():
    annotations = typing.get_type_hints(add)
    expected_annotations = {'num1': int, 'num2': int, 'return': int}
    assert annotations == expected_annotations, f"Type annotations are incorrect. Expected: {expected_annotations}, Actual: {annotations}"
    return "Type annotations for 'add' function are correct."

def test_add_element_to_list_function_annotations():
    annotations = typing.get_type_hints(add_element_to_list)
    expected_annotations = {'lst': list, 'element': str, 'return': list}
    assert annotations == expected_annotations, f"Type annotations are incorrect. Expected: {expected_annotations}, Actual: {annotations}"
    return "Type annotations for 'add_element_to_list' function are correct."

def test_multiple_function_annotations():
    annotations = typing.get_type_hints(multiple)
    expected_annotations = {'num1': float, 'num2': int, 'return': float}
    assert annotations == expected_annotations, f"Type annotations are incorrect. Expected: {expected_annotations}, Actual: {annotations}"
    return "Type annotations for 'multiple' function are correct."

def test_create_list_of_random_numbers_function_annotations():
    annotations = typing.get_type_hints(create_list_of_random_numbers)
    expected_annotations = {'length': int, 'return': list}
    assert annotations == expected_annotations, f"Type annotations are incorrect. Expected: {expected_annotations}, Actual: {annotations}"
    return "Type annotations for 'create_list_of_random_numbers' function are correct."

print(test_add_function_annotations())
print(test_add_element_to_list_function_annotations())
print(test_multiple_function_annotations())
print(test_create_list_of_random_numbers_function_annotations())
