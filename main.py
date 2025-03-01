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
showMenu(options)