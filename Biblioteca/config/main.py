from database import Database
db = Database(host = '10.28.1.244',
    user = 'root',
    password = '',
    database = 'biblioteca')

db.conectar()  
print(vars(db.conectar()))
db.cursor.execute("SELECT * FROM LIVRO")
print(db.cursor.fetchall())

db.desconectar()
print(vars(db.desconectar()))

