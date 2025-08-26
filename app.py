import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
df = pd.read_csv('vehicles_us.csv', sep=',', encoding='utf-8', header=0)

st.title("Análisis de vehículos usados")

# Mostrar una muestra de la tabla
st.subheader("Vista previa de los datos")
st.dataframe(df.head(10))

# Filtros por marca y modelo
st.subheader("Filtrar por marca y modelo")

# Extraer marcas (primera palabra del modelo)
df['marca'] = df['model'].str.split().str[0]
marcas = sorted(df['marca'].dropna().unique())
marca_seleccionada = st.selectbox("Selecciona una marca", marcas)

# Filtrar modelos según la marca seleccionada
modelos_filtrados = df[df['marca'] == marca_seleccionada]['model'].dropna().unique()
modelo_seleccionado = st.selectbox("Selecciona un modelo", sorted(modelos_filtrados))

# Filtrar el DataFrame según selección
df_filtrado = df[df['model'] == modelo_seleccionado]

# Mostrar tabla filtrada
st.subheader(f"Datos del modelo seleccionado: {modelo_seleccionado}")
st.dataframe(df_filtrado)

# Comparativa: precio vs odómetro
st.subheader("Comparativa: Precio vs Odómetro")
fig_comp = px.scatter(df_filtrado, x="odometer", y="price",
                      title=f"Precio vs Odómetro para {modelo_seleccionado}",
                      labels={"odometer": "Odómetro", "price": "Precio"})
st.plotly_chart(fig_comp, use_container_width=True)

# Histograma general
if st.checkbox('Mostrar histograma general'):
    st.write('Creación de un histograma para el odómetro de todos los vehículos')
    fig_hist = px.histogram(df, x="odometer", title="Histograma de Odómetro")
    st.plotly_chart(fig_hist, use_container_width=True)

# Gráfico de dispersión general
if st.checkbox('Mostrar gráfico de dispersión general'):
    st.write('Creación de un gráfico de dispersión (precio vs. odómetro) para todos los vehículos')
    fig_disp = px.scatter(df, x="odometer", y="price", title="Precio vs Odómetro (Todos)")
    st.plotly_chart(fig_disp, use_container_width=True)


     