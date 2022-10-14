import streamlit as st
import models.cliente as Cliente
import controllers.clientecontroller as Clientecontroller


st.title("Incluir cliente")

with st.form(key="include_cliente", clear_on_submit=True):
    input_name = st.text_input(label="Insira seu nome")
    input_age = st.number_input(label="Insira sua idade", format='%d', value=0, min_value=0, max_value=125, step=1)
    input_occupation = st.selectbox("Selecione sua profissão", ["Desenvolvedor(a)", "Professor(a)", "Eletricista"])
    Input_button_submit = st.form_submit_button("Enviar")

if Input_button_submit:
    Cliente.nome = input_name
    Cliente.idade =  input_age
    Cliente.profissao = input_occupation

    Clientecontroller.Incluir(Cliente)
    st.success("Cliente incluido com sucesso")