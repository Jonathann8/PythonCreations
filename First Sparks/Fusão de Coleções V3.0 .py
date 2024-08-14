import time
from termcolor import colored

def obter_dado(texto, tipo=str, validacao=None):
    while True:
        try:
            dado = tipo(input(texto))
            if validacao and not validacao(dado):
                raise ValueError
            return dado
        except ValueError:
            print(colored('Entrada inválida. Tente novamente.', 'red'))

def registrar_pessoa():
    pessoa = {}
    pessoa['nome'] = obter_dado('Nome: ')
    pessoa['sexo'] = obter_dado('Sexo: [M/F] ', str, lambda x: x.upper() in 'MF').upper()
    pessoa['idade'] = obter_dado('Idade: ', int, lambda x: x >= 0)
    return pessoa

def exibir_resultados(galera, soma):
    print('-=' * 30)
    print('Por favor, aguarde enquanto calculamos os dados...')
    time.sleep(2)  # Simula o tempo de computação

    print('-=' * 30)
    total_pessoas = len(galera)
    média = soma / total_pessoas
    print(colored(f'Ao todo temos {total_pessoas} pessoas cadastradas.', 'green'))
    print(colored(f'A média de idade é de {média:5.2f} anos.', 'yellow'))

    mulheres = [p["nome"] for p in galera if p['sexo'] == 'F']
    homens = [p["nome"] for p in galera if p['sexo'] == 'M']

    print('As mulheres cadastradas foram: ', end='')
    print(colored(', '.join(mulheres), 'magenta'))

    print('Os homens cadastrados foram: ', end='')
    print(colored(', '.join(homens), 'cyan'))

    print('Lista das pessoas que estão acima da média de idade:')
    for p in galera:
        if p['idade'] >= média:
            print('   ', end='')
            for k, v in p.items():
                print(colored(f'{k} = {v}; ', 'blue'), end='')
            print()
    print(colored('<< ENCERRADO >>', 'green'))
    print(f'Obrigado e volte sempre!!!')

def main():
    galera = []
    soma = 0

    while True:
        pessoa = registrar_pessoa()
        galera.append(pessoa)
        soma += pessoa['idade']
        
        continuar = obter_dado('Quer continuar? [S/N] ', str, lambda x: x.upper() in 'SN').upper()
        if continuar == 'N':
            break

    exibir_resultados(galera, soma)

if __name__ == "__main__":
    main()
