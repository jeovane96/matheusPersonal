import streamlit as st
import psycopg2
import controllers.database as db

def criar_tabelas_db():
    conn = psycopg2.connect(db.db_url)
    cursor = conn.cursor()

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tb_usuario (
                id        SERIAL PRIMARY KEY,
                email     TEXT NOT NULL,
                senha     TEXT NOT NULL,
                dt_insert TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP - INTERVAL '3 hours'
            )''')
        print("Tabela 'tb_usuario' criada com sucesso.")

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tb_alunos (
                id          SERIAL PRIMARY KEY,
                nm_aluno    TEXT NOT NULL,
                kg          NUMERIC(5,2) NOT NULL,
                observacao  TEXT NOT NULL,
                user_insert TEXT NOT NULL,
                dt_insert   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP - INTERVAL '3 hours'
            )''')
        print("Tabela 'tb_alunos' criada com sucesso.")

    except psycopg2.Error as e:
        print(f"Erro ao criar tabelas: {e}")

    conn.commit()
    conn.close()