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
        wrapText=False,
        autoHeight=True,
        sortable=False,
        filter=False
    )

    # Ajustar colunas específicas automaticamente com base no conteúdo
    gb.configure_column('ID', maxWidth=80, autoWidth=True)
    gb.configure_column('Treino', autoWidth=True)
    gb.configure_column('Grupo de membro', autoWidth=True)
    gb.configure_column('Observação', autoWidth=True)
    gb.configure_column('Usuário', autoWidth=True)
    gb.configure_column('Data', autoWidth=True)

    gb.configure_grid_options(domLayout='normal')
    grid_options = gb.build()

    # # Renderização
    # AgGrid(
    #     df,
    #     gridOptions=grid_options,
    #     height=600,
    #     autoSizeColumns=False,  # Ativa o ajuste automático das colunas
    #     theme='material',
    #     enable_enterprise_modules=False
    # )
    # Renderização da tabela com AgGrid
    AgGrid(
        df,
        gridOptions=grid_options,
        height=600,
        fit_columns_on_grid_load=False,
        theme='material',  # 'streamlit', 'alpine', 'balham' também são válidos
        enable_enterprise_modules=False
    )