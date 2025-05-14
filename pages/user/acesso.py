import streamlit as st
import time
import psycopg2
import bcrypt
import controllers.database as db

# Função para verificar se a senha digitada corresponde ao hash armazenado
def verificar_senha(senha: str, senha_hash: str) -> bool:
    return bcrypt.checkpw(senha.encode(), senha_hash.encode())

# Função para verificar o usuário no banco de dados
def verificar_usuario(email, senha):
    conn = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    
    # Buscar o hash da senha do usuário pelo e-mail
    cursor.execute("SELECT senha FROM tb_usuario WHERE email = %s", (email,))
    resultado = cursor.fetchone()
    
    conn.close()

    if resultado:
        senha_hash_armazenada = resultado[0]
        return verificar_senha(senha, senha_hash_armazenada)  # Compara a senha digitada com o hash salvo
    
    return False  

# Função para autenticação no Streamlit
def authenticate_user():

    if st.session_state.get("authenticated", False):  
        return True

    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    login_placeholder   = st.empty()  
    success_placeholder = st.empty()  

    with login_placeholder.container():
        st.markdown(""" 
            <style>
            .title-container { display: flex; justify-content: center; text-align: center; height: 10vh; }
            .title-container h1 { font-size: 2em; }
            </style>
        """, unsafe_allow_html=True)
        st.markdown('<div class="title-container"><h1>''</h1></div>', unsafe_allow_html=True)

        col1, col2, col3 = st.columns([3, 4, 3])
        with col1:
            None

        with col2:
            email        = st.text_input("**E-mail**", key="login_email")
            password     = st.text_input("**Senha**", type="password", key="login_password")
            login_button = st.button("Entrar")

            if login_button:
                with st.spinner("Autenticando..."):
                    autenticado = verificar_usuario(email, password)
                    time.sleep(3)

                if autenticado:
                    st.session_state["authenticated"] = True
                    st.session_state["user"] = email

                    # success_placeholder.success(f"Bem-vindo, **{email.upper()}** !")
                    success_placeholder.markdown(
                        f"""
                        <div style="
                            padding: 10px;
                            border-radius: 5px;
                            background-color: #D9D9D9; /* Cor verde personalizada */
                            color: black; /* Texto branco */
                            text-align: center;
                            font-weight: bold;">
                            <span style="color: black;">Bem-vindo, {email} !</span>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    time.sleep(3)
                    success_placeholder.empty()  
                    login_placeholder.empty()  

                    return True  
                else:
                    st.error("E-mail ou senha inválidos.")

            return False
        
        with col3:
            None
