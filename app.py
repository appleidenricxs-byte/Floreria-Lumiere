import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# ----------------------
# DATA
# ----------------------
data = pd.DataFrame({
    "Mes": ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"],
    "Ventas": [500,700,1200,900,1500,1700,1400,1600,2000,1800,2100,2300],
    "Estado": ["Completado","Pendiente","Completado","Completado","Pendiente","Completado",
               "Cancelado","Completado","Pendiente","Completado","Completado","Completado"]
})

gastos = 3000
inversion = 2000

ventas_totales = data["Ventas"].sum()
ganancia = ventas_totales - gastos - inversion
pendientes = (data["Estado"] == "Pendiente").sum()
completados = (data["Estado"] == "Completado").sum()

# ----------------------
# SIDEBAR
# ----------------------
st.sidebar.title("Menú")
st.sidebar.markdown("Dashboard")
st.sidebar.markdown("Ventas")
st.sidebar.markdown("Inventario")
st.sidebar.markdown("Inversión")

# ----------------------
# HEADER
# ----------------------
st.title("Panel de Operaciones")

# ----------------------
# GRÁFICA PRINCIPAL
# ----------------------
fig_line = px.line(data, x="Mes", y="Ventas", title="Tendencia de Ventas")
st.plotly_chart(fig_line, use_container_width=True)

# ----------------------
# KPIs
# ----------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Ventas Totales", f"${ventas_totales}")
col2.metric("Pedidos Pendientes", pendientes)
col3.metric("Pedidos Completados", completados)
col4.metric("Ganancia", f"${ganancia}")

# ----------------------
# GRÁFICAS ABAJO
# ----------------------
colA, colB = st.columns(2)

fig_donut = px.pie(data, names="Estado", title="Estado de Pedidos", hole=0.5)
colA.plotly_chart(fig_donut, use_container_width=True)

fig_bar = px.bar(data, x="Mes", y="Ventas", title="Ventas por Mes")
colB.plotly_chart(fig_bar, use_container_width=True)
