import streamlit as st
import models.sistema as sistema
import controllers.treinos.cadastrarTreinosCon as cadastrarTreinosCon
import time
import streamlit as st
from datetime import datetime

def createTreinos():

    # Verifica se o usuário está autenticado
    if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
        st.error("Você precisa estar autenticado.")
        return
    
    # Garante que o usuário autenticado está disponível no session_state
    user = st.session_state.get("user", "")
        
    col1, col2 = st.columns(2)

    with col1:
        input_nm_treino        = st.text_input("**Nome do treino**", key="text_input_treino")
        input_nm_grupo_membro  = st.selectbox("**Grupo de membro**", options=['Superior', 'Inferior'], key="input_membro")

    with col2:
        input_observacao  = st.text_input("**Observação**", key="text_input_observacap")
        input_user        = st.text_input("**Usuário**", value=user, disabled=True, key="usuario_autenticado_create")

    input_button_submit     = st.button("**Enviar**", key="button_create_treino")
        
    if input_button_submit:

        with st.spinner("Cadastrando treino..."):   
            sistema.nm_treino          = input_nm_treino.upper() 
            sistema.nm_grupo_membro    = input_nm_grupo_membro
            sistema.observacao         = input_observacao
            sistema.user               = input_user
            cadastrarTreinosCon.insertTreinos(sistema)
            time.sleep(2) 

        success_container = st.empty()
        st.success(f"Treino **{input_nm_treino.upper()}** cadastrado com sucesso!")  
        time.sleep(2)
        success_container.empty()