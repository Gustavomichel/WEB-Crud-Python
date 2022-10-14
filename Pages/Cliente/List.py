import streamlit as st
import controllers.clientecontroller as Clientecontroller
import Pages.Cliente.Create as pageincluirCliente
import pandas as pd

def List():
    st.title("Clientes")
    costumerlist = []

    for item in Clientecontroller.selecionartodos():
        costumerlist.append([item.nome, item.idade, item.profissao])

    df = pd.DataFrame(
        costumerlist,
        columns=['Nome', 'Idade', 'Profissão']
    )

    st.table(df)