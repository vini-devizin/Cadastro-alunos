from lib.interface import * # Importing the package interface from package lib
from lib.classes import * # Importing the package classes from package lib
options: list[str] = [ # The options of user
    'Cadastrar novo aluno',
    'Remover aluno',
    'Exibir alunos cadastrados',
    'Sair do sistema'
]
showMenu(options)