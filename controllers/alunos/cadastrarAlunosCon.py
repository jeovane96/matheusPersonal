import streamlit as st
import models.sistema as sistema
from datetime import timedelta
import controllers.database as db
import psycopg2


def insertAlunos(insert_alunos):
    conn   = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    try:
        cursor.execute(""" 
            INSERT INTO tb_alunos (
                nm_aluno,  
                telefone,        
                observacao,
                user_insert                      
            ) 
            VALUES(
                %s,
                %s,
                %s,
                %s
            )""",
            (
                insert_alunos.nm_aluno, 
                insert_alunos.telefone,
                insert_alunos.observacao,
                insert_alunos.user
            )
        )
        conn.commit()
    
    except psycopg2.OperationalError as e:
        st.error(f"Erro no banco de dados: {e}")
    
    finally:
        cursor.close()
        conn.close()