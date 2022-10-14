import pyodbc 
"""
DATABASE CONNECTION
"""
__dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-OT76IE1\SQLEXPRESS;"
    "Database=Crud_python;"
)

cnxn = pyodbc.connect(__dados_conexao)
cursor = cnxn.cursor()