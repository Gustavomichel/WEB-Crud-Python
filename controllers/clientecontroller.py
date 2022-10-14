import services.database as db

def Incluir(cliente):
    count = db.cursor.execute("""
    INSERT INTO Cliente (cliNome, cliIdade, cliProfissao) 
    VALUES (?,?,?)""",
    cliente.nome, cliente.idade, cliente.profissao).rowcount
    db.cnxn.commit()