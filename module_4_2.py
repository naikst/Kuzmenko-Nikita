def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()
    # Вызов inner_function из test_function


test_function()
# Вывод от inner_function

# inner_function()  # Ошибка! Эта функция не существует вне test_function. NameError: name 'inner_function' is not
# defined. Did you mean: 'test_function'?
