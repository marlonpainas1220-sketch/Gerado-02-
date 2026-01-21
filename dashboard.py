import streamlit as st
from backend.generators.visual_dna import VisualDNA
from backend.orchestrator import ContentOrchestrator
from backend.profiles.base_profile import ContentType
from backend.profiles.influencer_profile import PersonalityVersion

st.set_page_config(page_title="Gerado-02 Control", layout="wide", page_icon="🎬")

# Inicializar orquestrador
if 'orchestrator' not in st.session_state:
    st.session_state.orchestrator = ContentOrchestrator()

orchestrator = st.session_state.orchestrator

st.title("🎬 Gerado-02: Torre de Comando de Conteúdo")
st.markdown("*Sistema Autônomo de Produção de Conteúdo Digital*")

# Tabs principais
tab1, tab2, tab3, tab4 = st.tabs([
    "🎨 Gerador de Conteúdo",
    "📊 Analytics & Memória",
    "🖼️ Visual DNA",
    "⚙️ Configurações"
])

# TAB 1: Gerador de Conteúdo
with tab1:
    st.header("Gerador de Conteúdo")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Seleção de perfil
        profile = st.selectbox(
            "Perfil",
            ["influencer", "gossip"],
            format_func=lambda x: "🌟 Influenciadora de IA" if x == "influencer" else "💬 Página de Fofocas"
        )
        
        # Tipo de conteúdo
        content_type_map = {
            "Post": ContentType.POST,
            "Story": ContentType.STORY,
            "Roteiro": ContentType.ROTEIRO,
            "Pacote Completo": ContentType.PACOTE_COMPLETO
        }
        
        content_type_str = st.selectbox(
            "Tipo de Conteúdo",
            list(content_type_map.keys())
        )
        content_type = content_type_map[content_type_str]
        
        # Tema
        topic = st.text_area(
            "Tema/Tópico do Conteúdo",
            placeholder="Ex: Reflexão sobre confiança e autenticidade",
            height=100
        )
        
        # Contexto adicional
        additional_context = st.text_area(
            "Contexto Adicional (opcional)",
            placeholder="Informações extras, referências, tom desejado...",
            height=80
        )
    
    with col2:
        st.subheader("Configurações")
        
        # Configurações específicas da influenciadora
        if profile == "influencer":
            st.markdown("**Personalidade**")
            personality_map = {
                "Soft Power (Elegante)": PersonalityVersion.SOFT_POWER,
                "Agressiva Magnética": PersonalityVersion.AGRESSIVA_MAGNETICA
            }
            personality_str = st.radio(
                "Versão",
                list(personality_map.keys()),
                label_visibility="collapsed"
            )
            personality = personality_map[personality_str]
            
            st.markdown("**Ousadia**")
            ousadia = st.slider(
                "Nível (1-10)",
                min_value=1,
                max_value=10,
                value=5,
                label_visibility="collapsed"
            )
            
            st.caption(f"Nível {ousadia}: " + {
                1: "Discreta",
                2: "Discreta",
                3: "Confiante",
                4: "Elegante",
                5: "Provocação sutil",
                6: "Provocação sutil",
                7: "Sensual e direta",
                8: "Marcante",
                9: "Ousada",
                10: "Máximo impacto"
            }.get(ousadia, ""))
        
        st.markdown("**Entrega**")
        delivery_phone = st.text_input(
            "WhatsApp (opcional)",
            placeholder="5511999999999"
        )
        
        use_n8n = st.checkbox("Enviar via n8n")
    
    # Botão de geração
    if st.button("🚀 Gerar Conteúdo", type="primary", use_container_width=True):
        if not topic:
            st.error("Por favor, insira um tema/tópico!")
        else:
            with st.spinner("Gerando conteúdo..."):
                try:
                    # Preparar configurações
                    config = {}
                    if profile == "influencer":
                        config["personality"] = personality
                        config["ousadia"] = ousadia
                    
                    # Gerar
                    result = orchestrator.generate_and_deliver(
                        profile_name=profile,
                        content_type=content_type,
                        topic=topic,
                        delivery_phone=delivery_phone if delivery_phone else None,
                        use_n8n=use_n8n,
                        additional_context=additional_context,
                        **config
                    )
                    
                    st.success("✅ Conteúdo gerado com sucesso!")
                    
                    # Exibir resultado
                    st.markdown("### 📄 Conteúdo Gerado")
                    st.text_area(
                        "Resultado",
                        value=result["formatted_content"],
                        height=400,
                        label_visibility="collapsed"
                    )
                    
                    # Informações de entrega
                    if delivery_phone:
                        st.info(f"📱 Enviado via WhatsApp para {delivery_phone}")
                    if use_n8n:
                        st.info("🔗 Enviado para n8n webhook")
                    
                except Exception as e:
                    st.error(f"❌ Erro ao gerar conteúdo: {str(e)}")

# TAB 2: Analytics
with tab2:
    st.header("Analytics & Memória Evolutiva")
    
    profile_analytics = st.selectbox(
        "Selecione o Perfil",
        ["influencer", "gossip"],
        format_func=lambda x: "🌟 Influenciadora" if x == "influencer" else "💬 Fofocas",
        key="analytics_profile"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Análise de Padrões")
        
        if st.button("Analisar Perfil"):
            with st.spinner("Analisando..."):
                analysis = orchestrator.get_profile_analytics(profile_analytics)
                
                if "error" in analysis:
                    st.warning(analysis["error"])
                else:
                    st.json(analysis)
    
    with col2:
        st.subheader("🏆 Melhores Conteúdos")
        
        metric = st.selectbox(
            "Métrica",
            ["engagement", "likes", "shares", "comments"]
        )
        
        if st.button("Ver Melhores"):
            with st.spinner("Carregando..."):
                best = orchestrator.get_profile_best_content(
                    profile_name=profile_analytics,
                    metric=metric,
                    limit=5
                )
                
                if not best:
                    st.info("Nenhum conteúdo com métricas registradas ainda.")
                else:
                    for idx, item in enumerate(best, 1):
                        with st.expander(f"#{idx} - {item['content'].get('titulo', 'Sem título')}"):
                            st.write(item['content'].get('texto', ''))
                            st.caption(f"Métricas: {item.get('metrics', {})}")

# TAB 3: Visual DNA
with tab3:
    st.header("🖼️ Visual DNA Generator")
    st.caption("Gerador de prompts para manter consistência visual da influenciadora")
    
    col1, col2 = st.columns(2)
    
    with col1:
        scenario = st.text_input("Cenário", "sitting in a cafe")
        outfit = st.text_input("Roupa", "white dress")
        mood = st.selectbox("Iluminação", ["natural lighting", "neon lights", "golden hour", "studio lighting"])
        
        if st.button("Gerar Prompt de DNA"):
            dna = VisualDNA()
            prompt, negative = dna.construct_prompt(scenario, outfit, mood)
            
            st.markdown("**Prompt Positivo:**")
            st.code(prompt, language="text")
            
            st.markdown("**Prompt Negativo:**")
            st.code(negative, language="text")
            
            st.info("💡 Copie estes prompts e use no Replicate/Stable Diffusion/Midjourney")
    
    with col2:
        st.markdown("### ℹ️ Sobre o Visual DNA")
        st.markdown("""
        O Visual DNA garante que todas as imagens geradas mantenham:
        
        - ✅ Mesma identidade facial
        - ✅ Características físicas consistentes
        - ✅ Estilo visual coerente
        - ✅ Qualidade profissional
        
        **Como usar:**
        1. Configure o cenário e roupa
        2. Gere o prompt
        3. Use em ferramentas de IA de imagem
        4. A identidade visual será mantida
        """)

# TAB 4: Configurações
with tab4:
    st.header("⚙️ Configurações do Sistema")
    
    st.subheader("🔑 Credenciais")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**OpenAI**")
        st.text_input("API Key", type="password", placeholder="sk-...")
        
        st.markdown("**WhatsApp Business**")
        st.text_input("Phone Number ID", placeholder="123456789")
        st.text_input("Access Token", type="password", placeholder="EAA...")
    
    with col2:
        st.markdown("**n8n**")
        st.text_input("Webhook URL", placeholder="https://...")
        
        st.markdown("**Instagram**")
        st.text_input("Account ID", placeholder="123456789")
        st.text_input("Access Token (IG)", type="password", placeholder="EAA...")
    
    st.info("💡 Configure as credenciais no arquivo .env para uso em produção")
    
    st.subheader("📊 Status do Sistema")
    
    status_col1, status_col2, status_col3 = st.columns(3)
    
    with status_col1:
        st.metric("Perfis Ativos", "2")
    
    with status_col2:
        st.metric("Conteúdos Gerados", "0")
    
    with status_col3:
        st.metric("Taxa de Sucesso", "100%")

# Footer
st.markdown("---")
st.caption("🎬 Gerado-02 - Sistema Autônomo de Produção de Conteúdo Digital | Powered by OpenAI GPT-4")