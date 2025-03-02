from lib.interface import * # Importing the package interface from package lib
from lib.classes import * # Importing the package classes from package lib
from lib.database import * # Importing the package database from package lib
options: list[str] = [ # The options of user
    'Cadastrar novo aluno',
    'Remover aluno',
    'Exibir alunos cadastrados',
    'Buscar aluno',
    'Sair do sistema'
]
create_database()
create_table('alunos')
while True:
    req = showMenu(options)
    if req == 1:
        name = read_name('Nome: (máximo de 255 caracteres) ')
        sex = read_sex('Sexo: [M/F] ')
        born = read_date('Data de nascimento: ')
        cpf = read_cpf('CPF: (sem "." ou "-") ')
        grade = read_grade('Série: ')
        edu = define_edu(grade)
        add_student(name, sex, born, cpf, edu, grade, 'alunos')
    elif req == 5:
        header('SAINDO DO SISTEMA...')
        break