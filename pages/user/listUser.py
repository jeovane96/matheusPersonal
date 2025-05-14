import streamlit as st
import controllers.user.usuarioCon as ControllerSistema
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

def ListUsuarios():
    customerList = []

    for item in ControllerSistema.selecionarTodosUsuarios():
        customerList.append([
            item.id, 
            item.email
        ])

    df = pd.DataFrame(
        customerList,
        columns=['ID', 'E-mail']
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
    gb.configure_column('E-mail', autoWidth=True)

    gb.configure_grid_options(domLayout='normal')
    grid_options = gb.build()

    # # Renderização
    # AgGrid(
    #     df,
    #     gridOptions=grid_options,
    #     height=600,
    #     autoSizeColumns=True,  # Ativa o ajuste automático das colunas
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