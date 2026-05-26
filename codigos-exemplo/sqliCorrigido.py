import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

user = input("Usuário: ")
password = input("Senha: ")

query = """
SELECT * FROM users
WHERE username = ?
AND password = ?
"""

cursor.execute(query, (user, password))

resultado = cursor.fetchone()

if resultado:
    print("Login realizado")
else:
    print("Usuário inválido")