# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor
# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Digite sua Senha: ')

senha_permitida = '1234'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Você entrou')
else:
    print('Voce saiu')

# Avaliação de curto circuitoE