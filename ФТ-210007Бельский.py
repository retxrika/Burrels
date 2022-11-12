import random
import logging
import os

'''
Ввод целого числа с проверкой на ошибки.

Параметры:
msg - Информационное сообщение пользователю (type str). (Обязательный)

Ошибки:
Invalid input - Неверный ввод.
Number must be greater than 1 - Число не входит в заданный диапазон.

Возврат:
Целое число введенное пользователем.
'''
def input_int(msg : str) -> int:
    invalid_input_err = 'Invalid input'
    out_range_err = 'Number must be greater than 1'

    # Возвращает форматированную строку ошибки.
    def get_error(text : str):
        return '\033[31m{}\033[0m'.format('ERROR: ' + text + '! Try again...')

    while True:
        try:
            logging.info(msg)
            num = int(input(msg + ': '))
            logging.info(f'Пользователь ввел: {num}')
        except:
            print(get_error(invalid_input_err))
            logging.error(invalid_input_err, exc_info=True)
            continue

        if num < 1:
            print(get_error(out_range_err))
            logging.error(out_range_err)
            continue

        logging.info(f'Корректно введенное значение: {num}')
        return num

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename="log_file.log", filemode="a",
                        format="%(asctime)s %(levelname)s %(message)s")
    
    os.system('cls')
    countBarrels = input_int('Введите количество бочонков')
    # Генерация списка чисел.
    barrels = list(range(1, countBarrels + 1))
    # Перемешивание.
    random.shuffle(barrels)
    logging.info(f'Полученная последовательность бочек: {barrels}')
    
    print()
    msg = 'Выпавший бочонок с номером: '
    for i in range(len(barrels)):
        # Каждый раз берем и удаляем число из списка.
        barrel = barrels.pop()
        print(msg + str(barrel))
        logging.info(msg + str(barrel))
        input('Нажмите enter для вытягивания следующего бочонка...')

    

    