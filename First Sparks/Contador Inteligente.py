from time import sleep

def contador(i, f, p): #inicio, fim e passo.(i: o valor de início da contagem. f: o valor de fim da contagem. p: o passo, ou seja, o incremento ou decremento a ser usado na contagem.)
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)
    # Se o passo p for negativo, ele é transformado em positivo. Isso é necessário para evitar problemas de lógica na contagem.
    # Se o passo p for igual a zero, ele é redefinido para 1. Isso é feito para evitar loops infinitos, já que um passo de 0 causaria um ciclo sem fim.

    if p < 0: 
        p *= -1
    if p == 0:
        p = 1 
    if i < f:
        cont = i
        while cont <= f:
           print(f'{cont} ', end=' ', flush=True)
           sleep(0.5)
           cont += p 
        print('FIM!')
    else: 
        cont = i 
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')
    

#Programa principal 
contador(1, 10, 1) #Essas linhas chamam a função contador duas vezes com valores predefinidos:

#A primeira contagem vai de 1 até 10, de 1 em 1.
#A segunda contagem vai de 10 até 0, de 2 em 2.
contador(10, 0, 2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
#Aqui, o programa permite ao usuário definir seus próprios valores de início, fim e passo. Ele solicita esses valores via input() e converte as entradas para inteiros com int(). Depois, o programa chama a função contador() com os valores fornecidos pelo usuário.