from datetime import datetime
from colorama import Fore, Style, init

# Inicializa a colorama
init(autoreset=True)

dados = dict()
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)

print(Fore.GREEN + '-=' * 30)
print(Fore.CYAN + f"Nome: {Fore.YELLOW}{dados['nome']}")
print(Fore.CYAN + f"Idade: {Fore.YELLOW}{dados['idade']} anos")
print(Fore.CYAN + f"Carteira de Trabalho: {Fore.YELLOW}{'Não possui' if dados['ctps'] == 0 else dados['ctps']}")
if dados['ctps'] != 0:
    print(Fore.CYAN + f"Ano de Contratação: {Fore.YELLOW}{dados['contratação']}")
    print(Fore.CYAN + f"Salário: {Fore.YELLOW}R${dados['salário']:.2f}")
    print(Fore.CYAN + f"Aposentadoria prevista para: {Fore.YELLOW}{dados['aposentadoria']} anos")
print(Fore.GREEN + '-=' * 30)
