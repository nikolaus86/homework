
calls=0
def count_calls():
    global calls
    calls+=1
def string_info(s):
    count_calls()
    length=len(s)
    upper=s.upper()
    lower=s.lower()
    return length,upper,lower
def is_contains(s, list_to_search):
    count_calls()  # Увеличиваем счётчик вызовов
    # Приводим строку и элементы списка к нижнему регистру для сравнения
    s = s.lower()
    list_to_search = [item.lower() for item in list_to_search]
    return s in list_to_search


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)