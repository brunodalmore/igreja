import streamlit as st

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="EJE - Encontro de Jovens",
    page_icon="🎭",
    layout="centered"
)

# ===== CSS CUSTOMIZADO =====
st.markdown("""
<style>
body {
    background-color: #0e1117;
}

.main {
    background-color: #0e1117;
}

/* Título principal */
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 0;
}

/* Subtítulo */
.subtitle {
    text-align: center;
    font-size: 22px;
    color: #bbbbbb;
    margin-top: 0;
}

/* Card */
.card {
    background-color: #1c1f26;
    padding: 25px;
    border-radius: 15px;
    margin-top: 20px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
}

/* Texto */
.text {
    font-size: 18px;
    line-height: 1.6;
}

/* Centralizar imagem */
.img-center {
    display: flex;
    justify-content: center;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
st.markdown('<p class="title">🎭 Encontro de Jovens nas Escolas</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">EJE</p>', unsafe_allow_html=True)

# ===== IMAGEM =====
st.markdown('<div class="img-center">', unsafe_allow_html=True)
st.image("img/image - 2026-04-29T123204.035.png", width=250)
st.markdown('</div>', unsafe_allow_html=True)

# ===== SOBRE =====
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📌 Sobre o projeto")
st.markdown("""
<div class="text">
Somos um grupo de jovens que realiza peças de teatro nas escolas com o objetivo
de inspirar outros jovens a participarem do Encontro de Jovens nas Escolas (EJE),
um evento que acontece todos os anos e transforma vidas.
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ===== LOCALIZAÇÃO =====
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📍 Onde estamos?")
st.markdown("""
<div class="text">
Estamos localizados no Jardim Paquetá, em Planaltina - Goiás.
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ===== RODAPÉ =====
st.markdown("""
<br><br>
<div style='text-align: center; color: gray; font-size: 14px;'>
Feito com ❤️ usando Streamlit
</div>
""", unsafe_allow_html=True)
