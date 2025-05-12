import streamlit as st
import models.sistema as sistema
from datetime import timedelta
import controllers.database as db
import psycopg2

def selecionarAgendamentos():
    conn = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            id,         
            nm_aluno,       
            dia_semana_aula,
            horario_inicio, 
            horario_fim,            
            observacao, 
            user_insert,                      
            TO_CHAR(dt_insert, 'DD/MM/YYYY HH24:MI') AS dt_insert                
        FROM 
            tb_agendamentos
        ORDER BY
            ID
        ASC
    """)
    customerList = []

    for row in cursor.fetchall():
        customerList.append(sistema.agendamentos(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

    return customerList