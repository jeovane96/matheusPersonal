import streamlit as st
import models.sistema as sistema
from datetime import timedelta
import controllers.database as db
import psycopg2


def insertTreinosAlunos(insert_treinos_alunos):
    conn   = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    try:
        cursor.execute(""" 
            INSERT INTO tb_treinos_alunos (
                nm_aluno,         
                nm_treino,        
                nr_repeticao,     
                peso,               
                nr_tempo_descanso,
                observacao                           
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
                insert_treinos_alunos.nm_aluno,         
                insert_treinos_alunos.nm_treino,        
                insert_treinos_alunos.nr_repeticao,     
                insert_treinos_alunos.peso,               
                insert_treinos_alunos.nr_tempo_descanso,
                insert_treinos_alunos.observacao  
            )
        )
        conn.commit()
    
    except psycopg2.OperationalError as e:
        st.error(f"Erro no banco de dados: {e}")
    
    finally:
        cursor.close()
        conn.close()