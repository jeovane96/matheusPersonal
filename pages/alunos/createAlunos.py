import streamlit as st
import models.sistema as sistema
import pages.user.acesso as acesso
import controllers.alunos.cadastrarAlunosCon as cadastrarAlunosCon
import time
import streamlit as st
from datetime import datetime

def createAlunos():

    # Verifica se o usuário está autenticado
    if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
        st.error("Você precisa estar autenticado.")
        return
    
    # Garante que o usuário autenticado está disponível no session_state
    user = st.session_state.get("user", "")
        
    col1, col2 = st.columns(2)

    with col1:
        input_nm_aluno  = st.text_input("**Aluno**", key="text_input_aluno")
        input_kg        = st.number_input("**KG**", key="input_kg")

    with col2:
        input_observacao  = st.text_input("**Observação**", key="text_input_observacap")
        input_user        = st.text_input("**Usuário**", value=user, disabled=True, key="usuario_autenticado_create")

    input_button_submit     = st.button("**Enviar**", key="button_create")
        
    if input_button_submit:

        with st.spinner("Cadastrando aluno..."):   
            sistema.nm_aluno    = input_nm_aluno 
            sistema.kg          = input_kg
            sistema.observacao  = input_observacao
            sistema.user        = input_user
            cadastrarAlunosCon.insertAlunos(sistema)
            time.sleep(2) 

        success_container = st.empty()
        st.success(f"Aluno **{input_nm_aluno}** cadastrado com sucesso!")  
        time.sleep(2)
        success_container.empty()