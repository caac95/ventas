import streamlit as st
import pandas as pd
import plotly.express as px

try:
    df = pd.read_csv('vehiculo.csv', sep=',', encoding='utf-8', header=0)
    print(df.head())
except FileNotFoundError:
    print("No se encontró el archivo 'vehiculo.csv'. Verifica que esté en la carpeta correcta.")
except pd.errors.ParserError as e:
    print("Error al analizar el archivo CSV:", e)
except Exception as e:
    print("Error inesperado:", e)


if st.checkbox('Mostrar histograma'):
    st.write('Creación de un histograma para el odómetro de los vehículos')
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para scatter plot
if st.checkbox('Mostrar gráfico de dispersión'):
    st.write('Creación de un gráfico de dispersión (precio vs. odómetro)')
    fig = px.scatter(df, x="odometer", y="price", title="Precio vs Odómetro")
    st.plotly_chart(fig, use_container_width=True)
     