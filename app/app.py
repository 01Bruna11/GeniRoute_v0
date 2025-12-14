import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from genai.advisor import genai_advisor


st.set_page_config(page_title="GeniRoute | iFood GenAI", layout="wide")

st.title("🍔 GeniRoute — Previsão Inteligente de Entregas")

st.markdown("""
Simulação de um sistema GenAI integrado ao app do iFood,  
oferecendo **previsão de atrasos, explicabilidade e recomendações operacionais**.
""")

# Layout em colunas
col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 Parâmetros Operacionais")

    hora = st.slider("Hora do dia", 0, 23, 12)
    volume = st.slider("Volume de pedidos", 10, 300, 120)
    chuva = st.selectbox("Está chovendo?", [0, 1])
    jogo = st.selectbox("É dia de jogo?", [0, 1])
    feriado = st.selectbox("É feriado?", [0, 1])
    transito = st.slider("Nível de trânsito (1 = baixo | 5 = alto)", 1, 5, 3)

    input_data = {
        "hora": hora,
        "volume_pedidos": volume,
        "chuva": chuva,
        "dia_jogo": jogo,
        "feriado": feriado,
        "transito_nivel": transito,
    }

    gerar = st.button("🔮 Gerar Previsão")

with col2:
    st.subheader("📊 Resultado")

    if gerar:
        with st.spinner("Analisando cenário..."):
            atraso, explicacao = genai_advisor(input_data)

        st.metric("⏱️ Atraso médio estimado", f"{atraso} minutos")

        st.markdown("### 🧠 Explicação & Recomendações")
        st.write(explicacao)
    else:
        st.info("Preencha os parâmetros e clique em **Gerar Previsão**.")
