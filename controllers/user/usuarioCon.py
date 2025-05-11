import streamlit as st
import models.sistema as sistema
from datetime import timedelta
import controllers.database as db
import psycopg2

def Incluir_usuario(insert_tb_usuario):
    conn   = psycopg2.connect(db.db_url)
    cursor = conn.cursor()

    try:
        cursor.execute(""" 
            INSERT INTO tb_usuario (email, senha) 
            VALUES(LOWER(%s), %s)""",
        (insert_tb_usuario.email, insert_tb_usuario.senha)
        )
        conn.commit() 

    except psycopg2.OperationalError as e:
        st.error(f"Erro no banco de dados: {e}")
    
    finally:
        cursor.close()
        conn.close() #Ed.fisica.vitorino@gmail.com

def ExcluirUsuario(excluir_email):
    conn = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    cursor.execute(""" 
        DELETE FROM tb_usuario WHERE email = %s""", 
        (excluir_email.email,)
    )
    conn.commit()

def selecionarEmailUsuario():
    conn = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    cursor.execute("SELECT email FROM tb_usuario")
    customerList = []

    for row in cursor.fetchall():
        customerList.append(sistema.usuario(id=None, email=row[0], senha=None))
    
    return customerList

def obter_usuarios_cadastrados(usuario):
    conn   = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    query  = """
        SELECT 
            email
        FROM 
            tb_usuario
        WHERE 
            email = %s
    """
    cursor.execute(query, (usuario,))
    usuario_ = cursor.fetchall()
    conn.commit()
    return usuario_

def selecionarTodosUsuarios():
    conn   = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tb_usuario")
    customerList = []

    for row in cursor.fetchall():
        customerList.append(sistema.usuario(row[0], row[1], row[2]))

    return customerList

