# import streamlit as st
# import pandas as pd
# import psycopg2
# from datetime import datetime, timedelta
# import controllers.database as db

# # --- Conexão ao PostgreSQL ---

# def agendamento():
#     conn   = psycopg2.connect(db.db_url)
#     cursor = conn.cursor()

#     df = pd.read_sql("SELECT nm_aluno, dia_semana_aula, horario_inicio, horario_fim FROM tb_agendamentos", conn)
#     conn.close()

#     # --- Converte colunas de tempo ---
#     df["horario_inicio"] = pd.to_datetime(df["horario_inicio"], format="%H:%M:%S").dt.time
#     df["horario_fim"] = pd.to_datetime(df["horario_fim"], format="%H:%M:%S").dt.time

#     # --- Gera grade da agenda ---
#     horarios = pd.date_range("07:00", "22:00", freq="30min").time
#     dias = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
#     agenda = pd.DataFrame("", index=[h.strftime("%H:%M") for h in horarios], columns=dias)

#     # --- Preenche grade com os nomes dos alunos ---
#     for _, row in df.iterrows():
#         dia = row["dia_semana_aula"].capitalize()
#         inicio = row["horario_inicio"]
#         fim = row["horario_fim"]

#         tempo = inicio
#         while tempo < fim:
#             hora_str = tempo.strftime("%H:%M")
#             if hora_str in agenda.index and dia in agenda.columns:
#                 if agenda.at[hora_str, dia]:
#                     agenda.at[hora_str, dia] += f", {row['nm_aluno']}"
#                 else:
#                     agenda.at[hora_str, dia] = row["nm_aluno"]
#             tempo = (datetime.combine(datetime.today(), tempo) + timedelta(minutes=30)).time()

#     # --- Converte agenda em HTML estilizado ---
#     agenda.reset_index(inplace=True)
#     agenda.rename(columns={"index": "Horário"}, inplace=True)
#     table_html = agenda.to_html(index=False, classes="table", border=1, escape=False)

#     # --- CSS e HTML para estilização ---
#     st.markdown("""
#         <style>
#             .table-container {
#                 max-height: 600px;
#                 overflow-y: auto;
#                 margin-top: 20px;
#             }
#             .table {
#                 width: 100%;
#                 text-align: center;
#                 border-collapse: collapse;
#             }
#             .table th {
#                 background-color: black;
#                 color: white;
#                 padding: 10px;
#                 text-align: center;
#                 position: sticky;
#                 top: 0;
#                 z-index: 1;
#                 font-size: 14px;
#             }
#             .table td {
#                 border: 1px solid gray;
#                 padding: 8px;
#                 text-align: center;
#                 font-size: 12px;
#                 background-color: #cce5ff;
#                 font-weight: bold;
#             }
#             .table td:empty {
#                 background-color: white;
#                 font-weight: normal;
#             }
#             .table tr:nth-child(even) {
#                 background-color: #f2f2f2;
#             }
#             .table tr:hover {
#                 background-color: #ddd;
#             }
#         </style>
#     """, unsafe_allow_html=True)

#     st.markdown(f"<div class='table-container'>{table_html}</div>", unsafe_allow_html=True)








import streamlit as st
import pandas as pd
import psycopg2
from datetime import datetime, timedelta
import controllers.database as db
from st_aggrid import AgGrid, GridOptionsBuilder

def agendamento():
    conn   = psycopg2.connect(db.db_url)
    cursor = conn.cursor()

    df = pd.read_sql("SELECT nm_aluno, dia_semana_aula, horario_inicio, horario_fim FROM tb_agendamentos", conn)
    conn.close()

    df["horario_inicio"] = pd.to_datetime(df["horario_inicio"], format="%H:%M:%S").dt.time
    df["horario_fim"] = pd.to_datetime(df["horario_fim"], format="%H:%M:%S").dt.time

    horarios = pd.date_range("07:00", "22:00", freq="30min").time
    dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
    agenda = pd.DataFrame("", index=[h.strftime("%H:%M") for h in horarios], columns=dias)

    for _, row in df.iterrows():
        dia = row["dia_semana_aula"].capitalize()
        inicio = row["horario_inicio"]
        fim = row["horario_fim"]

        tempo = inicio
        while tempo < fim:
            hora_str = tempo.strftime("%H:%M")
            if hora_str in agenda.index and dia in agenda.columns:
                if agenda.at[hora_str, dia]:
                    agenda.at[hora_str, dia] += f", {row['nm_aluno']}"
                else:
                    agenda.at[hora_str, dia] = row["nm_aluno"]
            tempo = (datetime.combine(datetime.today(), tempo) + timedelta(minutes=30)).time()

    agenda.reset_index(inplace=True)
    agenda.rename(columns={"index": "Horário"}, inplace=True)

    gb = GridOptionsBuilder.from_dataframe(agenda)
    gb.configure_default_column(resizable=True, wrapText=True, autoHeight=True)
    gb.configure_grid_options(domLayout='normal')
    grid_options = gb.build()

    AgGrid(
        agenda,
        gridOptions=grid_options,
        height=600,
        fit_columns_on_grid_load=True,
        theme='material',
    )
