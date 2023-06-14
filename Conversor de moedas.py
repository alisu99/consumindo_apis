# conversor de moedas
from time import sleep
from requests import get

cotacoes = get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
moedas = cotacoes.json()
dolar = moedas['USDBRL']
euro = moedas['EURBRL']
bitcoin = moedas['BTCBRL']


# funções responsáveis pela converção
def conv_dolar(valor):
    print('-' * 25)
    print('      $ Dolar $       ')
    print(f'Cotação Atual: R$ {float(dolar["high"]):.2f}')
    print(f'R$ {valor:.2f} => $ {valor / float(dolar["high"]):.2f}')
    print(f'{dolar["create_date"]}')
    print('-' * 25)


def conv_euro(valor):
    print('-' * 25)
    print('      € Euro €       ')
    print(f'Cotação Atual: R$ {float(euro["high"]):.2f}')
    print(f'R$ {valor:.2f} => € {valor / float(euro["high"]):.2f}')
    print(f'{euro["create_date"]}')
    print('-' * 25)


def conv_bitcoin(valor):
    print('-' * 25)
    print(' ₿ Bitcoin ₿ ')
    print(f'Cotação atual: R$ {float(bitcoin["high"]):.2f}')
    print(f'R$ {valor:.2f} => ₿ {valor / float(bitcoin["high"]):.2f}')
    print(f'{bitcoin["create_date"]}')
    print('-' * 25)


valor = float(input('Saldo R$: '))
opcao = 0
print(
f'''----- Saldo R$ {valor:.2f} -----
[1] Dolar
[2] Euro
[3] Bitcoin
[4] Alterar Saldo''')


while opcao != 5:
    opcao = int(input('Opção desejada ([5] para sair): '))
    if opcao == 1:
        conv_dolar(valor)
        sleep(1)

    elif opcao == 2:
        conv_euro(valor)
        sleep(1)

    elif opcao == 3:
        conv_bitcoin(valor)
        sleep(1)

    elif opcao == 4:
        print('-' * 25)
        valor = float(input('Saldo: '))
        print(
f'''----- Saldo R$ {valor:.2f} -----
[1] Dolar
[2] Euro
[3] Libra esterlina
[4] Alterar Saldo
____________________________________''')
        sleep(1)

    elif opcao == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('\033[0:31mOpção inválida, tente novamente!\033[0:0m')

