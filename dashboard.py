import streamlit as st
from backend.generators.visual_dna import VisualDNA

st.set_page_config(page_title="Gerado-02 Control", layout="wide")

st.title("🎬 Gerado-02: Painel de Controle da Influenciadora")

col1, col2 = st.columns(2)

with col1:
    st.header("⚙️ Gerador Manual")
    scenario = st.text_input("Cenário", "sitting in a cafe")
    outfit = st.text_input("Roupa", "white dress")
    mood = st.selectbox("Iluminação", ["natural lighting", "neon lights", "golden hour", "studio lighting"])
    
    if st.button("Gerar Prompt de DNA"):
        dna = VisualDNA()
        prompt, negative = dna.construct_prompt(scenario, outfit, mood)
        st.code(prompt, language="text")
        st.info("Copie este prompt e use no Replicate/Stable Diffusion para testar.")

with col2:
    st.header("📲 Fila de Aprovação")
    st.write("Nenhum conteúdo pendente no momento.")
    # Aqui entraria a conexão com o Banco de Dados