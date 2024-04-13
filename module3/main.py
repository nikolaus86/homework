def test():
    a = 10
    b = 20
    print("Inside test function:")
    print("a =", a)
    print("b =", b)


# Вызов функции test
test()


def test2(param1, param2, param3):
    print("\nInside test2 function:")
    print("param1 =", param1)
    print("param2 =", param2)
    print("param3 =", param3)


# Вызов функции test2 с передачей трех параметров
test2(100, "Hello", [1, 2, 3])