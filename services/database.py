import pyodbc 

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-OT76IE1\SQLEXPRESS;"
    "Database=Crud_python;"
)

cnxn = pyodbc.connect(dados_conexao)
cursor = cnxn.cursor()