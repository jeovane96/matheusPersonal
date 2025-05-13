import streamlit as st
import models.sistema as sistema
from datetime import timedelta
import controllers.database as db
import psycopg2


def insertTreinos(insert_treinos):
    conn   = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    try:
        cursor.execute(""" 
            INSERT INTO tb_treinos (
                nm_treino,  
                nm_grupo_membro,        
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
                insert_treinos.nm_treino, 
                insert_treinos.nm_grupo_membro,
                insert_treinos.observacao,
                insert_treinos.user
            )
        )
        conn.commit()
    
    except psycopg2.OperationalError as e:
        st.error(f"Erro no banco de dados: {e}")
    
    finally:
        cursor.close()
        conn.close()