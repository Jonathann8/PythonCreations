from time import sleep

def maior(* núm):
    cont = maior = 0 
    print('-=' * 30)
    print('\nAnalisando os valores passados...')
    for valor in núm:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


#Programa principal
maior(8, 5, 3, 9, 1)
maior(4, 7, 9)
maior(1, 5)
maior(7)
maior()