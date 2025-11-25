import math

# -------- Параметрические функции --------
def addition(a: float, b: float) -> float:
    """Возвращает сумму двух чисел"""
    return a + b

def subtraction(a: float, b: float) -> float:
    """Возвращает разность двух чисел"""
    return a - b

def multiplication(a: float, b: float) -> float:
    """Возвращает произведение двух чисел"""
    return a * b

def division(a: float, b: float) -> float:
    """Возвращает частное двух чисел. Деление на ноль вызывает ValueError"""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b

def exponentiation(base: float, power: float) -> float:
    """Возводит число в степень"""
    return base ** power

def square_root(number: float) -> float:
    """Возвращает квадратный корень числа. Для отрицательного числа вызывает ValueError"""
    if number < 0:
        raise ValueError("Квадратный корень из отрицательного числа не определен")
    return math.sqrt(number)

# -------- Вспомогательная функция для ввода --------
def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка! Пожалуйста, введите число.")

# -------- Меню и основной цикл --------
def show_menu():
    print("\n" + "="*50)
    print("      КАЛЬКУЛЯТОР")
    print("="*50)
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Возведение в степень (^)")
    print("6. Квадратный корень (√)")
    print("7. Выход")
    print("="*50)

def main():
    print("Добро пожаловать в калькулятор!")
    while True:
        show_menu()
        choice = input("Выберите операцию (1-7): ")

        if choice == '1':
            a = get_number("Введите первое число: ")
            b = get_number("Введите второе число: ")
            print(f"Результат: {addition(a, b)}")
        elif choice == '2':
            a = get_number("Введите первое число: ")
            b = get_number("Введите второе число: ")
            print(f"Результат: {subtraction(a, b)}")
        elif choice == '3':
            a = get_number("Введите первое число: ")
            b = get_number("Введите второе число: ")
            print(f"Результат: {multiplication(a, b)}")
        elif choice == '4':
            a = get_number("Введите делимое: ")
            b = get_number("Введите делитель: ")
            try:
                print(f"Результат: {division(a, b)}")
            except ValueError as e:
                print(f"Ошибка: {e}")
        elif choice == '5':
            a = get_number("Введите основание: ")
            b = get_number("Введите степень: ")
            print(f"Результат: {exponentiation(a, b)}")
        elif choice == '6':
            a = get_number("Введите число: ")
            try:
                print(f"Результат: {square_root(a)}")
            except ValueError as e:
                print(f"Ошибка: {e}")
        elif choice == '7':
            print("Спасибо за использование калькулятора! До свидания!")
            break
        else:
            print("Неверный выбор! Пожалуйста, выберите операцию от 1 до 7.")

        input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()
