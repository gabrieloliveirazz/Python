"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
''' Meu código (não consegui informar se o número n é inteiro)
numero_inteiro = int(input('Digite um númeiro inteiro: '))

if numero_inteiro % 2:
    print('Seu número é ímpar.')
else :
    print('Seu número é par.')
'''
entrada = input('Digite um número')

try:
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro')
"""
Faça um programa que exige a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação correspondente. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = int(input('Digite a hora: '))

if hora >= 0 and hora <= 11:
    print('Bom dia!')
elif hora >= 12 and hora <= 17:
    print('Boa tarde')
else:
    print('Boa noite')

"""
Faça um programa que parte do primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
“Seu nome é normal”; maior que 6 escreva "Seu nome é muito grande".
"""
nome = (input('Digite seu nome: '))
tamanho_do_nome = len(nome)

if tamanho_do_nome < 5:
    print('Seu nome é curto')
elif tamanho_do_nome == 5 or tamanho_do_nome == 6:
    print('Seu nome é normal')
else:
    print('Seu nome é grande.')