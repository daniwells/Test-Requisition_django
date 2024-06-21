import requests

# URL do seu servidor Django para obter o CSRF token
csrf_url = 'http://127.0.0.1:8000/get_csrf_token/'  # Endpoint fictício para obter o token

# Fazendo uma requisição GET para obter o token CSRF
csrf_response = requests.get(csrf_url)

# Verificando se a requisição foi bem-sucedida
if csrf_response.status_code == 200:
    csrf_token = csrf_response.json()['csrf_token']
else:
    print('Falha ao obter CSRF token, status code:', csrf_response.status_code)
    csrf_token = ''

# URL para fazer a requisição POST
post_url = 'http://127.0.0.1:8000/'  # Sua URL para fazer a requisição POST

# Dados que você quer enviar (pode ser um dicionário)
data = {
    'chave': 'valor',
    'outro_dado': 'outro_valor'
}

# Headers com o CSRF token
headers = {
    'X-CSRFToken': csrf_token  # Adicione o token CSRF aqui
}

# Fazendo uma requisição POST com o CSRF token no cabeçalho
response = requests.post(post_url, json=data, headers=headers)

# Verificando a resposta do servidor
if response.status_code == 200:
    print('Requisição bem-sucedida!')
    print('Resposta do servidor:', response.json())
else:
    print('Falha na requisição, status code:', response.status_code)