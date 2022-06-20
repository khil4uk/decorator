from datetime import datetime


def logger(old_function):
    def new_foo(*args, **qwargs):
        result = old_function(*args, **qwargs)
        with open('log_file.txt', 'w', encoding='utf-8') as file:
            file.write(
                f'Дата и время вызова: {datetime.now()}\n'
                f'Имя функции: {old_function.__name__}\n'
                f'Aргументы: {args, qwargs}\n'
                f'Возвращаемое значение: {result}'
            )
        return result

    return new_foo
