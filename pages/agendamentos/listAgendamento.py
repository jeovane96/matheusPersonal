# import streamlit as st
# import controllers.agendamentos.listarAgendamentosCon as listarAgendamentosCon
# import pandas as pd

# def ListAgendamentos():
#     customerList = []

#     for item in listarAgendamentosCon.selecionarAgendamentos():
#         customerList.append([
#             item.id,
#             item.nm_aluno,       
#             item.dia_semana_aula,
#             item.horario_inicio, 
#             item.horario_fim,    
#             item.observacao,     
#             item.user,    
#             item.dt_insert     
#         ])

#     df = pd.DataFrame(
#         customerList,
#         columns=['ID', 'Aluno', 'Dia da Semana', 'Início', 'Fim', 'Observação', 'Usuário', 'Data de Cadastro']
#     )

#     table_html = df.to_html(index=False, classes="table", border=1)

#     st.markdown("""
#         <style>
#             .table-container {
#                 max-height: 600px;  /* Ajuste a altura conforme necessário */
#                 overflow-y: auto;  /* Habilita a rolagem vertical */
#                 margin-top: 20px;
#             }
#             .table {
#                 width: 100%;
#                 text-align: center;
#                 border-collapse: collapse;
#             }
#             .table th {
#                 background-color: black;
#                 color: white;
#                 padding: 10px;
#                 text-align: center;  /* CENTRALIZA OS CABEÇALHOS */
#                 position: sticky;
#                 top: 0;
#                 z-index: 1;  /* Garante que o cabeçalho ficará acima do conteúdo */
#                 font-size: 14px; /* Ajuste conforme necessário */
#             }
#             .table td {
#                 border: 1px solid grow;
#                 padding: 8px;
#                 text-align: center; /* CENTRALIZA O CONTEÚDO */
#                 font-size: 12px; /* Ajuste conforme necessário */
#             }
#             .table tr:nth-child(even) {
#                 background-color: #f2f2f2;
#             }
#             .table tr:nth-child(odd) {
#                 background-color: #ffffff;
#             }
#             .table tr:hover {
#                 background-color: #ddd;
#             }
#         </style>
#     """, unsafe_allow_html=True)

#     # Envolver a tabela com a div para permitir a rolagem
#     st.markdown(f"<div class='table-container'>{table_html}</div>", unsafe_allow_html=True)


import streamlit as st
import controllers.agendamentos.listarAgendamentosCon as listarAgendamentosCon
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

def ListAgendamentos():
    customerList = []

    for item in listarAgendamentosCon.selecionarAgendamentos():
        customerList.append([
            item.id,
            item.nm_aluno,
            item.dia_semana_aula,
            item.horario_inicio.strftime("%H:%M") if item.horario_inicio else "",
            item.horario_fim.strftime("%H:%M") if item.horario_fim else "",
            item.observacao,
            item.user,
            item.dt_insert.strftime("%d/%m/%Y %H:%M") if item.dt_insert else ""
        ])

    df = pd.DataFrame(
        customerList,
        columns=[
            'ID',
            'Aluno',
            'Dia da Semana',
            'Início',
            'Fim',
            'Observação',
            'Usuário',
            'Data de Cadastro'
        ]
    )

    st.markdown("### 📅 Lista de Agendamentos")

    # Criação de opções para o grid
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_default_column(
        resizable=True,
        wrapText=True,
        autoHeight=True,
        sortable=True,
        filter=True
    )
    gb.configure_pagination(paginationAutoPageSize=False, paginationPageSize=15)
    gb.configure_grid_options(domLayout='normal')
    grid_options = gb.build()

    # Renderização da tabela com AgGrid
    AgGrid(
        df,
        gridOptions=grid_options,
        height=600,
        fit_columns_on_grid_load=True,
        theme='material',  # 'streamlit', 'alpine', 'balham' também são válidos
        enable_enterprise_modules=False
    )
