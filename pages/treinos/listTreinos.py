import streamlit as st
import controllers.treinos.listarTreinosCon as listarTreinosCon
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

def ListTreinos():
    customerList = []

    for item in listarTreinosCon.selecionarTreinos():
        customerList.append(
            [
                item.id,
                item.nm_treino,
                item.nm_grupo_membro,
                item.observacao,
                item.user,
                item.dt_insert if item.dt_insert else ""
            ]
        )

    df = pd.DataFrame(
        customerList,
        columns=['ID', 'Treino', 'Grupo de membro', 'Observação', 'Usuário', 'Data']
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
    # gb.configure_pagination(paginationAutoPageSize=False, paginationPageSize=15)
    gb.configure_grid_options(domLayout='normal')
    grid_options = gb.build()

    # Renderização
    AgGrid(
        df,
        gridOptions=grid_options,
        height=600,
        fit_columns_on_grid_load=True,
        theme='material',  # Alternativas: 'streamlit', 'alpine', 'balham'
        enable_enterprise_modules=False
    )
