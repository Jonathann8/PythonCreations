pessoa = dict()
galera = list()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! POR FAVOR, DIGITE M OU F!.' )
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! RESPONDA APENAS COM S OU N!.')
    if resp == 'N':
        break
    #foi adicionado o número de pessoas cadastradas e a média de suas idades.
print('-=' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'A média de idade é de {média:5.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print('Listas das pessoas que estão acima da média')
for p in galera:
    if p['idade'] >= média:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
        

