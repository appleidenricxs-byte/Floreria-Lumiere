import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(layout="wide")
st.title("🌸 Sistema Florería Lumiere")

# ----------------------
# CARGAR DATOS
# ----------------------
if os.path.exists("data.csv"):
    data = pd.read_csv("data.csv")
else:
    data = pd.DataFrame(columns=["Mes","Ventas","Estado"])

# ----------------------
# FORMULARIO (AGREGAR VENTAS)
# ----------------------
st.sidebar.header("Nueva Venta")

mes = st.sidebar.selectbox("Mes", ["Ene","Feb","Mar","Abr","May","Jun"])
ventas = st.sidebar.number_input("Monto", min_value=0)
estado = st.sidebar.selectbox("Estado", ["Completado","Pendiente","Cancelado"])

if st.sidebar.button("Agregar venta"):
    nueva = pd.DataFrame([[mes, ventas, estado]], columns=["Mes","Ventas","Estado"])
    data = pd.concat([data, nueva], ignore_index=True)
    data.to_csv("data.csv", index=False)
    st.sidebar.success("Venta guardada")

# ----------------------
# CALCULOS
# ----------------------
ventas_totales = data["Ventas"].sum()
pendientes = (data["Estado"] == "Pendiente").sum()
completados = (data["Estado"] == "Completado").sum()

gastos = 3000
ganancia = ventas_totales - gastos

# ----------------------
# DASHBOARD
# ----------------------
st.subheader("📊 Dashboard")

fig_line = px.line(data, x="Mes", y="Ventas", title="Ventas")
st.plotly_chart(fig_line, use_container_width=True)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Ventas", ventas_totales)
col2.metric("Pendientes", pendientes)
col3.metric("Completados", completados)
col4.metric("Ganancia", ganancia)

# ----------------------
# TABLA
# ----------------------
st.subheader("📋 Registros")
st.dataframe(data)
