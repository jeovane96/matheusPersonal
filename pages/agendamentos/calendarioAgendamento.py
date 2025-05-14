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
    df["horario_fim"]    = pd.to_datetime(df["horario_fim"], format="%H:%M:%S").dt.time

    horarios = pd.date_range("05:00", "22:00", freq="30min").time
    dias     = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
    agenda   = pd.DataFrame("", index=[h.strftime("%H:%M") for h in horarios], columns=dias)

    for _, row in df.iterrows():
        dia    = row["dia_semana_aula"].capitalize()
        inicio = row["horario_inicio"]
        fim    = row["horario_fim"]

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