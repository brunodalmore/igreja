import streamlit as st

# Ler o HTML
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Ler o CSS
with open("index.css", "r", encoding="utf-8") as f:
    css = f.read()

# Aplicar CSS + HTML
st.markdown(f"<style>{css}</style>{html}", unsafe_allow_html=True)
