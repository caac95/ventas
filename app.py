import streamlit as st
import pandas as pd
import plotly.express as px

df=pd.read_csv("../vehicles_us.csv")

if st.checkbox('Mostrar histograma'):
    st.write('Creación de un histograma para el odómetro de los vehículos')
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para scatter plot
if st.checkbox('Mostrar gráfico de dispersión'):
    st.write('Creación de un gráfico de dispersión (precio vs. odómetro)')
    fig = px.scatter(df, x="odometer", y="price", title="Precio vs Odómetro")
    st.plotly_chart(fig, use_container_width=True)
     