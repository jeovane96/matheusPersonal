import streamlit as st
import models.sistema as sistema
import controllers.treinosAlunos.cadastrarTreinosAlunos as cadastrarTreinosAlunos
import time
import streamlit as st
from datetime import datetime

def createTreinosAlunos():

    # Verifica se o usuário está autenticado
    if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
        st.error("Você precisa estar autenticado.")
        return
    
    # Garante que o usuário autenticado está disponível no session_state
    user = st.session_state.get("user", "")
        
    col1, col2 = st.columns(2)

    with col1:
        input_nm_aluno    = st.selectbox("**Aluno**", options=['a', 'b'], key="input_aluno")
        input_nm_treino   = st.selectbox("**Treino**", options=["a", "b"], key="text_input_treino_aluno")
        input_observacao  = st.text_input("**Observação**", key="text_input_observacao")

    with col2:
        input_peso               = st.number_input("**Peso**")
        input_nr_repeticao       = st.number_input("**Nº de repetição**")
        input_nr_tempo_descanso  = st.number_input("**Tempo de Descanço**")

    input_button_submit     = st.button("**Enviar**", key="button_create_treino")
        
    if input_button_submit:

        with st.spinner("Cadastrando treino..."):
            sistema.nm_aluno          = input_nm_aluno.upper()    
            sistema.nm_treino         = input_nm_treino.upper() 
            sistema.peso              = input_peso
            sistema.nr_repeticao      = input_nr_repeticao
            sistema.nr_tempo_descanso = input_nr_tempo_descanso
            sistema.observacao        = input_observacao
            sistema.user              = user
            cadastrarTreinosAlunos.insertTreinosAlunos(sistema)
            time.sleep(2) 

        success_container = st.empty()
        st.success(f"Treino **{input_nm_treino.upper()}** cadastrado com sucesso!")  
        time.sleep(2)
        success_container.empty()