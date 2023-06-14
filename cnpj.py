from requests import get

# api que retorna informações de um cnpj

# entrada para digitar o cnpj
cnpj = input('Digite o cnpj: ')

# buscando o cnpj pela url
url = get(f'https://minhareceita.org/{cnpj}')

# convertendo os dados
resultado = url.json()

for chave, valor in resultado.items():
    print(f'{chave}: {valor}')
