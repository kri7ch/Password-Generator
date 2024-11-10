from moduleKey import generate_key_for_platform, generate_password


def get_user_choice() -> str:
    """
    :return:
    """
    choice = input("Что вы хотите сгенерировать: key or password? ")
    return choice.lower()


def get_platform() -> str:
    """
    :return:
    """
    platform = input("Укажите платформу: ")
    return platform


def input_number(prompt: str) -> int:
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Введены неверные данные, введите число")


def get_password_options() -> None | tuple[bool, bool, bool, bool, int, bool]:
    """
    :return:
    """
    use_numbers = get_user_input("Использовать цифры? (да/нет) ")
    use_lowercase = get_user_input("Использовать строчные буквы? (да/нет) ")
    use_uppercase = get_user_input("Использовать заглавные буквы? (да/нет) ")
    use_special = get_user_input("Использовать специальные символы? (да/нет) ")
    if not (use_numbers or use_lowercase or use_uppercase or use_special):
        print("Пароль не может быть пустым")
        return None
    length = input_number("Укажите длину пароля: ")
    avoid_repetition = get_user_input("Избегать повторяющихся символов? (да/нет) ")

    return use_numbers, use_lowercase, use_uppercase, use_special, length, avoid_repetition


def get_user_input(prompt: str) -> bool:
    while True:
        user_input = input(prompt).lower()
        if user_input == "да":
            return True
        elif user_input == "нет":
            return False
        else:
            print("Введены неверные данные")


def display_key(key: str, platform: str) -> None:
    """
    :param key:
    :param platform:
    :return:
    """
    print(f"Сгенерированный ключ для платформы {platform}: {key}")


def display_password(password: str) -> None:
    """
    :param password:
    :return:
    """
    print(f"Сгенерированный пароль: {password}")


def main() -> None:
    """
    :return:
    """
    while True:
        user_choice = get_user_choice()
        if user_choice == "key":
            platform = get_platform()
            num_keys = input("Сколько ключей вы хотите сгенерировать? ")
            if not num_keys.isdigit():
                print('Введено некорреткное значение , введите число')
                continue
            for _ in range(int(num_keys)):
                key = generate_key_for_platform(platform)
                if key:
                    display_key(key, platform)
        elif user_choice == "password":
            num_passwords = input("Сколько паролей вы хотите сгенерировать? ")
            if not num_passwords.isdigit():
                print('Введено некорретное значение, введите число')
                continue
            password_options = get_password_options()
            if password_options is None:
                continue
            for _ in range(int(num_passwords)):
                password = generate_password(*password_options)
                if type(password) == tuple:
                    print('Попробуйте сгенерировать пароль заново.')
                    break
                display_password(password)
        else:
            print("Некорректный выбор. Пожалуйста, выберите 'ключ' или 'пароль'.")


if __name__ == '__main__':
    main()
