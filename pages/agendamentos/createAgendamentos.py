import streamlit as st
import models.sistema as sistema
import pages.user.acesso as acesso
import controllers.agendamentos.cadastrarAgendamentoCon as cadastrarAgendamentoCon
import controllers.alunos.listarAlunosCon as listarAlunosCon
import time
import streamlit as st
from datetime import datetime, timedelta


def createAgendamentos():

    def ListarAlunosFiltro():
        customerList = []

        for item in listarAlunosCon.listarAlunos():
            customerList.append(item.nm_aluno)

        return customerList

    nm_aluno_ = ListarAlunosFiltro() 

    # Verifica se o usuário está autenticado
    if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
        st.error("Você precisa estar autenticado.")
        return
    
    # Garante que o usuário autenticado está disponível no session_state
    user = st.session_state.get("user", "")
        
    col1, col2 = st.columns(2)

    with col1:
        input_nm_aluno        = st.selectbox("**Aluno**", options=nm_aluno_, key="text_input_aluno")
        input_dia_semana_aula = st.multiselect("**Dia da Semana**", ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'], placeholder="Escolha os dias de aula", key="input_dia_semana_aula")
        input_observacao      = st.text_input("**Observação**", key="input_obervacao_agendamento")

    with col2:
        input_horario_inicio  = st.time_input("**Horário Inicio**", step=timedelta(minutes=30), key="input_horario_inicio")
        input_horario_fim     = st.time_input("**Horário Fim**", step=timedelta(minutes=30), key="input_horario_fim")
        input_user            = st.text_input("**Usuário**", value=user, disabled=True, key="usuario_autenticado_create")

    input_button_submit     = st.button("**Enviar**", key="button_create_agendamento")
        
    if input_button_submit:

        with st.spinner("Cadastrando agendamento..."):
            for dia in input_dia_semana_aula:
                sistema.nm_aluno        = input_nm_aluno 
                sistema.dia_semana_aula = dia  # Um dia por vez
                sistema.horario_inicio  = input_horario_inicio
                sistema.horario_fim     = input_horario_fim
                sistema.observacao      = input_observacao
                sistema.user            = input_user
                cadastrarAgendamentoCon.insertAgendamentos(sistema)
                time.sleep(0.3)  # opcional: pequeno delay visual

        success_container = st.empty()
        st.success(f"Agendamentos do aluno **{input_nm_aluno}** cadastrados com sucesso!")  
        time.sleep(2)
        success_container.empty()
