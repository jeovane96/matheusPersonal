import streamlit as st
import controllers.alunos.listarAlunosCon as listarAlunosCon
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

def ListAlunos():
    customerList = []

    for item in listarAlunosCon.selecionarAlunos():
        customerList.append(
            [
                item.id,
                item.nm_aluno,
                item.telefone,
                item.observacao,
                item.user,
                item.dt_insert if item.dt_insert else ""
            ]
        )

    df = pd.DataFrame(
        customerList,
        columns=['ID', 'Aluno', 'Telefone', 'Observação', 'Usuário', 'Data']
    )

    # Configurações do AgGrid
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_default_column(
        resizable=True,
        wrapText=True,
        autoHeight=True,
        sortable=True,
        filter=False
    )

    # Ajustar colunas específicas automaticamente com base no conteúdo
    gb.configure_column('ID', maxWidth=80, autoWidth=True)
    gb.configure_column('Aluno', autoWidth=True)
    gb.configure_column('Telefone', autoWidth=True)
    gb.configure_column('Observação', autoWidth=True)
    gb.configure_column('Usuário', autoWidth=True)
    gb.configure_column('Data', autoWidth=True)

    gb.configure_grid_options(domLayout='normal')
    grid_options = gb.build()

    # Renderização
    AgGrid(
        df,
        gridOptions=grid_options,
        height=600,
        autoSizeColumns=True,  # Ativa o ajuste automático das colunas
        theme='material',
        enable_enterprise_modules=False
    )