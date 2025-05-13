import streamlit as st
import models.sistema as sistema
from datetime import timedelta
import controllers.database as db
import psycopg2

def selecionarTreinos():
    conn = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            id,         
            nm_treino,   
            nm_grupo_membro,         
            observacao, 
            user_insert,                      
            TO_CHAR(dt_insert, 'DD/MM/YYYY HH24:MI') AS dt_insert                
        FROM 
            tb_treinos
        ORDER BY
            ID
        ASC
    """)
    customerList = []

    for row in cursor.fetchall():
        customerList.append(sistema.treinos(row[0], row[1], row[2], row[3], row[4], row[5]))

    return customerList


def listarTreinos():
    conn = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    cursor.execute("SELECT nm_treino FROM tb_treinos")
    customerList = []

    for row in cursor.fetchall():
        customerList.append(sistema.alunos(id=None, nm_treino=row[0], nm_grupo_membro=None, observacao=None, user=None, dt_insert=None))
    
    return customerList