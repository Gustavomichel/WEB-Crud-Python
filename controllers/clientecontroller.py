import Database.database as db
import models.cliente as cliente

def Incluir(cliente):
    count = db.cursor.execute("""
    INSERT INTO Cliente (cliNome, cliIdade, cliProfissao) 
    VALUES (?,?,?)""",
    cliente.nome, cliente.idade, cliente.profissao).rowcount
    db.cnxn.commit()

def Excluir(id):
    count = db.cursor.execute("""
    DELETE FROM Cliente WHERE id = ?""",
    id).rowcount
    db.cnxn.commit()

def selecionartodos():
    db.cursor.execute("SELECT * FROM Cliente")
    costumerlist = []

    for row in db.cursor.fetchall():
        costumerlist.append(cliente.Cliente(row[0], row[1], row[2], row[3]))
    
    return costumerlist