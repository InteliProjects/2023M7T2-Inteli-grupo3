import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Criar dados fictícios para os gráficos de barras com cores
data1 = pd.DataFrame({
    'Tempo até a falha': ['7 Dias', '14 Dias', '1 Mes'],
    'Porcentagem de certeza': [75, 46, 15],
    'Time': ['7 Dias', '14 Dias', '1 Mes']
})

data2 = pd.DataFrame({
    'Modelos': ['Modelo 1', 'Modelo 2', 'Modelo 3'],
    'Porcentagem de certeza': [75, 80, 93],
    'Name': ['Logistic regression', 'XGBOOST', 'Random forest']
})

# Layout de duas colunas
col1, col2 = st.columns(2)

# Gráfico de barras na primeira coluna
with col1:
    st.write('Falha em 7 dias, 14 dias e 1 mês')
    chart1 = alt.Chart(data1).mark_bar().encode(
        x='Tempo até a falha',
        y='Porcentagem de certeza',
        color='Time'
    ).properties(width=300)
    st.altair_chart(chart1)

# Gráfico de barras na segunda coluna
with col2:
    st.write('Modelos')
    chart2 = alt.Chart(data2).mark_bar().encode(
        x='Modelos',
        y='Porcentagem de certeza',
        color='Name'
    ).properties(width=300)
    st.altair_chart(chart2)
