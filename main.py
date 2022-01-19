import string

dict_ru_low = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
dict_ru_up = dict_ru_low.upper()


def encrypt(code, msg):
    encoded_msg = real_code = str()
    while len(real_code) < len(msg):
        real_code += str(code)
    real_code = real_code[0:len(msg)]
    j = 0
    for i in range(len(msg)):
        if msg[i] in string.ascii_lowercase:
            encoded_msg += (string.ascii_lowercase * 2)[string.ascii_lowercase.find(msg[i]) + int(real_code[j])]
            j += 1
        elif msg[i] in string.ascii_uppercase:
            encoded_msg += (string.ascii_uppercase * 2)[string.ascii_uppercase.find(msg[i]) + int(real_code[j])]
            j += 1
        elif msg[i] in dict_ru_low:
            encoded_msg += (dict_ru_low * 2)[dict_ru_low.find(msg[i]) + int(real_code[j])]
            j += 1
        elif msg[i] in dict_ru_up:
            encoded_msg += (dict_ru_up * 2)[dict_ru_up.find(msg[i]) + int(real_code[j])]
            j += 1
        else:
            encoded_msg += msg[i]
    return encoded_msg


def decrypt(code, msg):
    decoded_msg = real_code = str()
    while len(real_code) < len(msg):
        real_code += str(code)
    real_code = real_code[0:len(msg)]
    j = 0
    for i in range(len(msg)):
        if msg[i] in string.ascii_lowercase:
            decoded_msg += (string.ascii_lowercase * 2)[string.ascii_lowercase.find(msg[i]) - int(real_code[j])]
            j += 1
        elif msg[i] in string.ascii_uppercase:
            decoded_msg += (string.ascii_uppercase * 2)[string.ascii_uppercase.find(msg[i]) - int(real_code[j])]
            j += 1
        elif msg[i] in dict_ru_low:
            decoded_msg += (dict_ru_low * 2)[dict_ru_low.find(msg[i]) - int(real_code[j])]
            j += 1
        elif msg[i] in dict_ru_up:
            decoded_msg += (dict_ru_up * 2)[dict_ru_up.find(msg[i]) - int(real_code[j])]
            j += 1
        else:
            decoded_msg += msg[i]
    return decoded_msg


def raise_error(code, msg):
    print(f"\033[31mОшибка №{code}!\n{msg}!\033[0m")
    raise SystemExit(code)


print(
        "Вас приветствует программа шифратор-дешифратор по алгоритму Гронсфельда."
        "\nАвтор: Студент РТУ МИРЭА группы БББО-05-20 Карабанов Евгений Геннадьевич"
)
choice = str()
while choice != "exit" or 0:
    print(
        "\n\nДля продолжения выберите способ предоставления сообщения для шифровки:"
        "\n1 или \"text\" для ввода текста вручную, 2 или \"file\" для извлечения его из файла."
        " Введите 0 или \"exit\" для выхода"
        "\nВыберите: ", end=''
    )
    choice = input()
    if choice == "0" or choice == "exit":
        raise SystemExit(0)
    elif choice == "1" or choice == "text":
        print("Введите секретный ключ: ", end='')
        try:
            code = int(input())
        except ValueError:
            raise_error(1, "Value error (must be integer)")
        print("Введите сообщение: ", end='')
        msg = input()
    elif choice == "2" or choice == "file":
        print("Введите секретный ключ: ", end='')
        try:
            code = int(input())
        except ValueError:
            raise_error(1, "Value error (must be integer)")
        print("Введите название файла (включая путь) с сообщением: ", end='')
        try:
            f = open(input(), 'r', encoding='utf-8')
            msg = f.read()
        except FileNotFoundError:
            raise_error(2, "File not found")
    else:
        raise_error(3, "Unexpected choice")
    print(f"Расшифрованное сообщение:"
          f"\033[33m\n"
          f"{decrypt(code, msg)}"
          f"\033[0m\n"
          f"Зашифрованное сообщение:"
          f"\033[33m\n"
          f"{encrypt(code, msg)}"
          f"\033[0m\n"
          )
