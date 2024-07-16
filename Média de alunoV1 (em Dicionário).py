import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

print(f'{bcolors.OKBLUE}\nComputando média...{bcolors.ENDC}')
time.sleep(1.2)

if aluno['média'] >= 7:
    aluno['situação'] = f'{bcolors.OKGREEN}Aprovado{bcolors.ENDC}'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = f'{bcolors.WARNING}Recuperação{bcolors.ENDC}'
else:
    aluno['situação'] = f'{bcolors.FAIL}Reprovado{bcolors.ENDC}'

print('\n' + '-=' * 30)
print(f"{bcolors.BOLD}{bcolors.HEADER}Relatório do Aluno:{bcolors.ENDC}")
print('-=' * 30)

for k, v in aluno.items():
    if k == 'nome':
        print(f'{bcolors.BOLD}{bcolors.OKCYAN}Nome:{bcolors.ENDC} {v}')
    elif k == 'média':
        print(f'{bcolors.BOLD}{bcolors.OKCYAN}Média:{bcolors.ENDC} {v}')
    elif k == 'situação':
        print(f'{bcolors.BOLD}{bcolors.OKCYAN}Situação:{bcolors.ENDC} {v}')

print('-=' * 30)
