from ..inputs import * # Importing the package inputs from package lib

def line(length: int=40) -> str:
    """
    -> Create a line
    :param length: Length of line
    :return: The line
    """
    return '-' * length

def header(txt: str) -> None:
    """
    -> Create a header with function line()
    :param txt: Text that will be used
    :return: None
    """
    print(line())
    print(f'{txt.center(40)}')
    print(line())

def showMenu(opts: list[str]):
    """
    -> Show the menu
    :param opts: A list of options that the user will chose one
    :return: The option that the user chose
    """
    header('MENU PRINCIṔAL')
    for i, v in enumerate(opts):
        print(f'\033[0;34m{i+1} \033[0;33m- {v}\033[0m')
    ask: int = readInt('Qual opção escolhe: ')
    return ask