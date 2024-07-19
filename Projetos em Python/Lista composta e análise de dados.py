from colorama import Fore, Style, init


init(autoreset=True)

lista_temporaria = []
lista_principal = []
maior = menor = 0

while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    lista_temporaria.append(nome)
    lista_temporaria.append(peso)
    
    if len(lista_principal) == 0:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    
    lista_principal.append(lista_temporaria[:])
    lista_temporaria.clear()
    
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(lista_principal)} pessoas. ')
print(f'O maior peso foi de {Fore.RED}{maior}Kg{Style.RESET_ALL}. Peso de ', end='')

for pessoa in lista_principal:
    if pessoa[1] == maior:
        print(f'{Fore.RED}{pessoa[0]}{Style.RESET_ALL}', end=' ')
print()

print(f'O menor peso foi de {Fore.BLUE}{menor}Kg{Style.RESET_ALL}. Peso de ', end='')

for pessoa in lista_principal:
    if pessoa[1] == menor:
        print(f'{Fore.BLUE}{pessoa[0]}{Style.RESET_ALL}', end=' ')
print()
print('-=' * 30)
