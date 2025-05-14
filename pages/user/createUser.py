import streamlit as st
import models.sistema as sistema
import pages.user.acesso as acesso
import controllers.user.usuarioCon as UsuarioCon
import pandas as pd
import random
import string
import time
import bcrypt

def hash_senha(senha: str) -> str:
    """Gera um hash seguro para a senha usando bcrypt."""
    salt = bcrypt.gensalt()
    senha_hash = bcrypt.hashpw(senha.encode(), salt)
    return senha_hash.decode()

def Incluir_usuario():  

    st.markdown(
        """
        <style>
        input[type="text"], input[type="number"] {
            background-color: white !important;
            color: white !important;
        }
        div[data-baseweb="select"] > div {
            background-color: white !important;
        }
        .stButton button:focus,
        .stButton button:active {
            background-color: black !important;
            color: white !important;
            border-color: white !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    def gerar_senha():
        """Gera uma senha aleatória de 8 caracteres."""
        tamanho_senha = 8
        caracteres = string.ascii_letters + string.digits  # Letras e números
        senha = ''.join(random.choice(caracteres) for i in range(tamanho_senha))
        return senha

    senha_gerada = gerar_senha()  # Senha temporária visível ao usuário

    col1, col2 = st.columns([2, 4])

    with col1:
        input_usuario       = st.text_input("**Usuário (E-mail)**", value="")  # Alterado para garantir um valor padrão
        # input_senha         = st.text_input("**Senha Gerada**", value=senha_gerada, disabled=True)
        
        input_button_submit = st.button("**Enviar**")

    if input_button_submit:
        if not input_usuario.strip():
            st.error("O E-mail está em branco.")
            return
        
        # Verifica se o usuário já existe no banco
        usuarios_existentes = UsuarioCon.obter_usuarios_cadastrados(input_usuario)
        if usuarios_existentes:
            return st.error("Usuário já cadastrado")
            
        with st.spinner("Cadastrando usuário..."):
            sistema.email  = input_usuario
            sistema.senha  = hash_senha(senha_gerada)  # Senha será armazenada como hash
            UsuarioCon.Incluir_usuario(sistema)  # Envia os dados para salvar no banco
            time.sleep(3)

        st.success(f"Usuário: **{input_usuario}** cadastrado com sucesso! A senha foi gerada automaticamente." )
        st.info(f"🔑 **Anote a senha:** `{senha_gerada}` (não será exibida novamente)")
        time.sleep(3)
   

def ExcluirUsuario():

    def ListEmailFiltro():
        customerList = []

        for item in UsuarioCon.selecionarEmailUsuario():
            customerList.append(item.email)

        return customerList

    email = ListEmailFiltro() 

    col1, col2 = st.columns([2, 4])

    with col1:   
        input_email  = st.selectbox("**E-mail cadastrado**", email, key="list_email")
        input_button = st.button("**Enviar**", key="button_enviar")

    with col2:
        None

    if input_button:
        with st.spinner("Atualizando..."):
            sistema.email = input_email
            UsuarioCon.ExcluirUsuario(sistema)
            time.sleep(3)

        st.success(f"Usuário {input_email} excluído!" )
        time.sleep(3)