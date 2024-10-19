def introspection_info(obj):
    info = {}

    # Определение типа объекта
    info['type'] = type(obj).__name__

    # Определение атрибутов объекта
    attributes = [attr for attr in dir(obj) if not attr.startswith("__")]
    info['attributes'] = attributes

    # Определение методов объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    info['methods'] = methods

    # Определение модуля, к которому принадлежит объект
    info['module'] = getattr(obj, '__module__', 'builtins' if info['type'] in ['int', 'str', 'list', 'dict'] else None)

    # Дополнительные интересные свойства
    if isinstance(obj, type):
        info['bases'] = [base.__name__ for base in obj.__bases__]

    return info

# Пример использования
number_info = introspection_info(42)
print(number_info)
