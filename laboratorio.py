i = 10
alunos=0
vagas=20

while i!=5:
    print('====LABORATÓRIO DE INFORMÁTICA====')

    print('1 - Registrar entrada de aluno')
    print('2 - Registrar saída de aluno')
    print('3 - Consultar alunos presentes')
    print('4 - Consultar vagas disponíveis')
    print('5 - Encerrar programa \n')

    i = int(input('Escolha sua opcao: '))

    if i == 1:
        if alunos == 20:
            print('Não é possível registrar um aluno, o laboratório está cheio')
        else:
            alunos += 1
            vagas -= 1

    elif i == 2:
        if alunos == 0:
            print('Não é possível registrar a saída de um aluno, não há nenhum aluno')
        else:
            alunos -= 1
            vagas += 1

    elif i == 3:
        if alunos == 0:
            print('Não há nenhum aluno presente')
        elif alunos >=1:
            print(f'{alunos} Estão presentes')

    elif i == 4:
        print(f'Há {vagas} vagas disponíveis')

# fazendo o segundo commit requerido pela atividade