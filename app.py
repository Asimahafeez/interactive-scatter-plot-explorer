import streamlit as st
import pandas as pd
from scatter_utils import generate_scatter

st.title("Interactive Multi-Dataset Scatter Plot Explorer")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of Dataset:")
    st.dataframe(df.head())

    columns = df.columns.tolist()
    x_col = st.selectbox("Select X-axis:", columns)
    y_col = st.selectbox("Select Y-axis:", columns)
    color_col = st.selectbox("Select Color (optional):", [None]+columns)
    size_col = st.selectbox("Select Size (optional):", [None]+columns)

    fig = generate_scatter(df, x_col, y_col, color_col, size_col)
    st.plotly_chart(fig, use_container_width=True)
