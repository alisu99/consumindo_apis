from requests import get
from time import sleep

cotacoes = get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
moedas = cotacoes.json()

while True:
    print('---------- DOLAR ----------')
    for chave, valor in moedas['USDBRL'].items():
        print(f'{chave}: {valor}')

    print('---------- EURO ----------')
    for chave, valor in moedas['EURBRL'].items():
        print(f'{chave}: {valor}')

    print('---------- BITCOIN ----------')
    for chave, valor in moedas['BTCBRL'].items():
        print(f'{chave}: {valor}')
    sleep(300)  # atualiza a cada 5 minutos
