# Estou de volta!

Faz um tempo que eu não apareço aqui no GitHub, mas eu estava fazendo exercicios de Python lá no Google Colab.

Eu já comecei a aprender POO e decidi fazer esse projetinho para praticar coisas que já aprendi.

Qualquer problema(issue) ou sugestão de implementação(pull request) eu estarei dando uma olhada(talvez demore para eu ver, mas em algum momento eu vejo).

Eu pretendo implementar o uso de banco de dados nesse projeto, mas não tão cedo.

# 23/02/2025

Fiquei uns dias sem mexer no projeto porque eu estava estudando e vendo formas de implementar postgresql.

Implementar isso não foi tão difćil, mas aconteceu algumas coisas, como:

- Tive um problema com OS(Debian 12), pois aparentemente ele não teve compatibilidade com a biblioteca.(Se alguém mais experiente estiver lendo isso, poderia me ajudar a entender isso? Porque o que eu falei, foi o que eu entendi, mas não sei se isso está correto)
- Para resolver o problema anterior, eu criei um venv, e tentei, mas deu um erro. Então, eu perguntei pro ChatGpt(Eu tive que usar ele porque eu não consegui entender o traceback) e ele me disse que eu teria que instalar mais dois pacotes(libpq-dev e python3-dev).

Obs: Quando eu avançar mais o projeto, irei fazer um passo a passo de como roda-lo.

Depois de dar o push entre 12:00 e 13:00, eu continuei codando e fui implementar a conexão do banco de dados. Sendo bem sincero, quando eu estava criando um usuário para usar, não estava dando certo porque eu não coloquei ponto e vírgula, e passei muito tempo quebrando cabeça com isso.

No momento que estou escrevendo agora, o commit mais recente é `verification added`.

# 24/02/2025

Hoje não tive tanto tempo para o projeto, mas só hoje que eu percebi que o .env e o venv estavam disponiveis, ou seja, minhas credenciais do banco de dados ficaram expostas por um dia inteiro🤡, e o venv não é necessário ele no repositório remoto(minha opinião).

# 28/02/2025

Olá, fiquei 4 dias sem dar atualizações aqui no GitHub porque estava tentando retirar do histórico o .env, que tinha as credenciais do banco de dados, mas o jeito foi deletar o repositório original e criar outro, que no caso, é esse.

Se quiser atualizações do projeto com mais frequência, vai no meu perfil do [TabNews](https://www.tabnews.com.br/ViniciusDaniel404/).

# 01/03/2025

Hoje implementei a verificação do nome de tabelas, para caso alguém tente fazer um sql injection, e as features de adicionar, remover, atualizar e exibir alunos nessas tabelas.
