import streamlit as st
import models.cliente as Cliente
import controllers.clientecontroller as Clientecontroller
import pandas as pd

st.sidebar.title("Menu")
page_cliente = st.sidebar.selectbox('Opções:', ['Incluir', 'Consultar', 'Excluir', 'Alterar'])

if 'Consultar' in page_cliente:

    st.title("Clientes")
    costumerlist = []

    for item in Clientecontroller.selecionartodos():
        costumerlist.append([item.nome, item.idade, item.profissao])

    df = pd.DataFrame(
        costumerlist,
        columns=['Nome', 'Idade', 'Profissão']
    )

    st.table(df)


if 'Incluir' in page_cliente:

    st.title("Incluir cliente")
    with st.form(key="include_cliente", clear_on_submit=True):
        input_name = st.text_input(label="Insira seu nome")
        input_age = st.number_input(label="Insira sua idade", format='%d', value=0, min_value=0, max_value=125, step=1)
        input_occupation = st.selectbox("Selecione sua profissão", ["Desenvolvedor(a)", "Professor(a)", "Eletricista"])
        Input_button_submit = st.form_submit_button("Enviar")

    if Input_button_submit:

        Clientecontroller.Incluir(Cliente.Cliente(0, input_name, input_age, input_occupation))
        st.success("Cliente incluido com sucesso")

