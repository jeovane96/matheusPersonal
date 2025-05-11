import streamlit as st
import models.sistema as sistema
from datetime import timedelta
import controllers.database as db
import psycopg2


def insertAgendamentos(insert_agendamento):
    conn   = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    try:
        cursor.execute(""" 
            INSERT INTO tb_agendamentos (
                nm_aluno,       
                dia_semana_aula,
                horario_inicio, 
                horario_fim, 
                observacao,   
                user_insert                      
            ) 
            VALUES(
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            )""",
            (
                insert_agendamento.nm_aluno,       
                insert_agendamento.dia_semana_aula,
                insert_agendamento.horario_inicio, 
                insert_agendamento.horario_fim, 
                insert_agendamento.observacao,   
                insert_agendamento.user 
            )
        )
        conn.commit()
    
    except psycopg2.OperationalError as e:
        st.error(f"Erro no banco de dados: {e}")
    
    finally:
        cursor.close()
        conn.close()