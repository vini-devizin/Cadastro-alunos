from datetime import date # Importing date from datetime to use in validate_date
import re # Importing re to verify names of tables

def readInt(txt: str) -> int:
    """
    -> Read a int
    :param txt: Text that be used to ask or require to user
    :return: The number that user typed
    """
    while True:
        try:
            num: int = int(input(txt))
        except (TypeError, ValueError):
            print('\033[0;31mERRO: Digite um número inteiro!\033[0m')
        else:
            return num

def read_name(txt: str) -> str:
    """
    -> Read a name
    :param txt: Text that will be used to ask or require to user
    :return: The name that user typed
    """
    while True:
        try:
            name: str = str(input(txt))
        except(ValueError, TypeError):
            print('\033[0;31mERRO: Digite apenas letras e espaços!\033[0m')
        else:
            if name.strip() == '':
                print(f'\033[0;31mERRO: "" apenas espaços em branco são inválidos!\033[0m')
            elif len(name) > 255:
                print('\033[0;31mErro: Nome grande demais! Abrevie ou faça outra coisa\033[0m')
            else:
                return name.title()

def read_sex(txt: str) -> str:
    """
    -> Read a sex
    :param txt: Text that will be used to ask or require to user
    :return: The sex that user typed
    """
    while True:
        try:
            sex: str = str(input(txt)).strip().upper()[0]
        except (TypeError, ValueError, IndexError):
            print('\033[0;31mERRO: Digite M ou F!\033[0m')
        else:
            if sex in 'MF':
                return sex
            else:
                print('\033[0;31mERRO: Digite M ou F!\033[0m')

def validate_date(year: int, month: int, day: int):
    """
    -> Validate a date
    :param year: Year
    :param month: Month
    :param day: Day
    :return: If the date is valid
    """
    try:
        data = date(year, month, day)
    except:
        print('\033[0;31mERRO: Data inválida!\033[0m')
        return False
    else:
        return data

def read_date(txt: str) -> str:
    """
    -> Read a date
    :param txt: Text that will be used to ask or require to user
    :return: Formatted date
    """
    while True:
        try:
            print(txt)
            day: int = int(input('dia: '))
            month: int = int(input('mês: '))
            year: int = int(input('ano: '))
        except(ValueError, TypeError):
            print('\033[0;31mERRO: Digite apenas números!\033[0m')
        else:
            if validate_date(year, month, day):
                return validate_date(year, month, day)

def read_cpf(txt: str) -> str:
    """
    -> Read and validate a CPF
    :param txt: Text that will be used to ask or require to user
    :return: The CPF
    """
    while True:
        try:
            cpf: int = int(input(txt))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO: Digite apenas números!\033[0m')
        else:
            if len(str(cpf)) != 11:
                print('\033[0;31mErro: O cpf digitado não tem 11 dígitos!\033[0m')
            else:
                return cpf 

def read_grade(txt: str) -> str:
    """
    -> Read and validate the school grade
    :txt: Text that will be used to ask or require to user
    :return: The valid grade
    """
    while True:
        try:
            grade = int(input(txt))
        except (ValueError, TypeError):
            print('\033[0;31mErro: Digite de 1 a 9 para fundamental 1 e 2, e de 1 a 3 para médio\033[0m')
        else:
            if grade < 0 or grade > 9:
                print('\033[0;31mErro: Digite de 1 a 9 para fundamental 1 e 2, e de 1 a 3 para médio\033[0m')
            else:
                return grade

def define_edu(grade: int) -> str:
    if grade <= 3:
        while True:
            try:
                edu = str(input('O aluno é do fundamental 1 ou médio: ')).strip().capitalize()
            except (ValueError, TypeError):
                print(f'\033[0;31mErro: digite "Fundamental 1" ou "Médio"')
            else:    
                if edu == 'Medio':
                    edu = 'Médio'
                if edu in ('Fundamental 1', 'Médio'):
                    break
                else:
                    print(f'\033[0;31mErro: digite "Fundamental 1" ou "Médio"\033[0m')
    elif grade > 3 and grade < 5:
        edu = 'Fundamental 1'
    else:
        edu = 'Fundamental 2'
    return edu

def read_email(txt: str) -> str:
    """
    -> Read and verify a email
    :param txt: Text that will be used to ask or require user
    :return: Verified email
    """
    while True:
        try:
            email = str(input(txt))
        except (TypeError, ValueError):
            print('\033[0;31mERRO: Digite o seu email!\033[0m')
        else:
            if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
                return email
            else:
                print('\033[0;31mERRO: Email inválido!\033[0m') 

def confirmation() -> str:
    """
    -> Ask if the user really wants to do that
    :param txt: Text that will be used to ask or require to user
    :return: If the user want or not
    """
    try:
        confirm = str(input('Você realmente quer fazer isso? [S/N] ')).strip().upper()[0]
    except (ValueError, TypeError):
        print(f'\033[0;31mERRO: Resposta inválida!\033[0m')
    else:
        if confirm == 'S':
            return True
        elif confirm == 'N':
            return False
        else:
            print('\033[0;31mERRO: Digite apenas S ou N!\033[0m')
