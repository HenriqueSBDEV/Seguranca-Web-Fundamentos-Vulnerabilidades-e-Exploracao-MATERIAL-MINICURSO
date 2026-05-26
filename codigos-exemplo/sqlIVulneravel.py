import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

user = input("Usuário: ")
password = input("Senha: ")

query = f"""
SELECT * FROM users
WHERE username = '{user}'
AND password = '{password}'
"""

cursor.execute(query)

resultado = cursor.fetchone()

if resultado:
    print("Login realizado")
else:
    print("Usuário inválido")