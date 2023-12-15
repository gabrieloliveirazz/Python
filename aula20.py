primeiro_valor = int(input("Digite o primeiro valor: "))
segundo_valor = int(input("Digite o segundo valor: "))

if primeiro_valor > segundo_valor:
    print('O', primeiro_valor, 'é maior que', segundo_valor)
elif primeiro_valor == segundo_valor:
    print(primeiro_valor, 'é igual ao', segundo_valor)
else:
    print('O', segundo_valor, 'é maior que', primeiro_valor)
