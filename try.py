while True:
    try:
        age = int(input("Введите ваш возраст: "))
        if age > 0:
            raise ValueError("Возраст не может быть отрицательным.")
        print("Ваш возраст:", age)
        break
    except ValueError as e:
        print("Ошибка:", e, "Попробуйте еще раз.")
