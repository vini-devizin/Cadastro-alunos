from lib.interface import * # Importing the package interface from package lib
from lib.classes import * # Importing the package classes from package lib
from lib.database import * # Importing the package database from package lib
from os import system
from time import sleep
options: list[str] = [ # The options of user
    'Cadastrar novo aluno',
    'Modificar aluno',
    'Remover aluno',
    'Exibir alunos cadastrados',
    'Buscar aluno',
    'Sair do sistema'
]
sleep(1)
create_database()
sleep(1)
create_table('alunos')
sleep(1)
while True:
    system('clear')
    res = showMenu(options)
    sleep(1)
    if res == 1:
        system('clear')
        header(options[0])
        name = read_name('Nome: (máximo de 255 caracteres) ')
        sex = read_sex('Sexo: [M/F] ')
        born = read_date('Data de nascimento: ')
        cpf = read_cpf('CPF: (sem "." ou "-") ')
        email = read_email('Email: ')
        grade = read_grade('Série: ')
        edu = define_edu(grade)
        sleep(1)
        add_student(name, sex, born, cpf, email, edu, grade, 'alunos')
        sleep(1)
    elif res == 2:
        system('clear')
        header(options[1])
        columns = ('nome', 'sexo', 'nascimento', 'cpf', 'email', 'ensino', 'serie')
        while True:
            try:
                id = readInt('Qual o id do aluno que deseja modificar: ')
                column = str(input('Qual campo deseja alterar: '))
                value = str(input('qual o valor deseja colocar: '))
            except (ValueError, TypeError):
                print('\033[0;31mERRO: Você escreveu algo inválido!\033[0m')
            else:
                if id > greater_id('alunos'):
                    print('\033[0;31mERRO: Id digitado é maior que o maior id registrado!\033[0m')
                else:
                    confirm = confirmation()
                    if confirm:
                        sleep(1)
                        update_student(id, value, column, 'alunos')
                        sleep(1)
                        break
                    else:
                        break
    elif res == 3:
        system('clear')
        header(options[2])
        while True:
            id = readInt('Qual o id do aluno que deseja remover: ')
            if id > greater_id('alunos'):
                print('\033[0;31mERRO: Id digitado é maior que o maior id registrado!\033[0m')
            else:
                confirm = confirmation()
                if confirm:
                    sleep(1)
                    remove_student(id, 'alunos')
                    sleep(1)
                    break
                else:
                    break
    elif res == 4:
        system('clear')
        header(options[3])
        sleep(1)
        show_students('alunos')
        stop = str(input('Pressione Enter para continuar '))
    elif res == 5:
        system('clear')
        header(options[4])
        id = readInt('Qual o id do aluno que deseja buscar: ')
        if id > greater_id('alunos'):
            print('\033[0;31mERRO: Id digitado é maior que o maior id registrado!\033[0m')
        else:
            sleep(1)
            search_student(id, 'alunos')
            stop = str(input('Pressione Enter para continuar '))
    elif res == 6:
        system('clear')
        sleep(2)
        header('SAINDO DO SISTEMA...')
        sleep(1)
        break
    else:
        print('\033[0;31mERRO: Digite uma opção válida!\033[0m')