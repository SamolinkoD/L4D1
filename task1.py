# У даному випадку, весь код написано за Вас) Ваша ж задача прописати аннотації до функцій.


# виконує сумму 
def add(num1, num2):
    return num1 + num2

print(add(5, 3))
# додає нові елементи в лист (оновлює лист)
old_list = ["apple", "pear", "banana"]

def add_element_to_list(lst, element):
    lst.append(element)
    return lst

print(add_element_to_list(old_list, "grape"))
# множеня двух значень
def multiple(num1, num2):
    return num1 * num2

print(multiple(5.1, 3))
# створюе лист із рандомними 10 числами від 0 до 100
def create_list_of_random_numbers(length):
    import random
    lst = []
    for _ in range(length):
        lst.append(random.randint(0, 100))
    return lst

print(create_list_of_random_numbers(10))
# кінець коду