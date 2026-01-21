# 🚀 Gerado-02 - Guia Rápido de Início

## ⚡ Início Rápido (5 minutos)

### 1. Configure a API Key da OpenAI

```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Edite e adicione sua chave
nano .env
```

Adicione:
```
OPENAI_API_KEY=sk-sua-chave-aqui
```

### 2. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 3. Execute o Dashboard

```bash
streamlit run dashboard.py
```

Acesse: `http://localhost:8501`

---

## 🎯 Uso Básico

### Opção 1: Dashboard Web (Mais Fácil)

1. Abra o dashboard: `streamlit run dashboard.py`
2. Selecione o perfil (Influenciadora ou Fofocas)
3. Escolha o tipo de conteúdo (Post, Story, Roteiro, Pacote)
4. Digite o tema
5. Configure personalidade e ousadia (se Influenciadora)
6. Clique em "Gerar Conteúdo"

### Opção 2: CLI (Mais Rápido)

```bash
# Influenciadora - Post elegante
python3 cli.py influencer post "Reflexão sobre autenticidade" --ousadia 5

# Influenciadora - Story ousada
python3 cli.py influencer story "Confiança feminina" --personality agressiva --ousadia 8

# Fofocas - Post viral
python3 cli.py gossip post "Escândalo da semana"

# Pacote completo
python3 cli.py influencer pacote "Lançamento de coleção"
```

### Opção 3: Python (Mais Flexível)

```python
from backend.orchestrator import ContentOrchestrator
from backend.profiles.base_profile import ContentType
from backend.profiles.influencer_profile import PersonalityVersion

# Inicializar
orchestrator = ContentOrchestrator()

# Gerar conteúdo
result = orchestrator.generate_influencer_content(
    content_type=ContentType.POST,
    topic="Autenticidade e ser verdadeira",
    personality=PersonalityVersion.SOFT_POWER,
    ousadia=6
)

# Exibir
print(result["formatted_content"])
```

---

## 📱 Entrega Automática (Opcional)

### WhatsApp

1. Configure no `.env`:
```
WHATSAPP_PHONE_NUMBER_ID=seu-id
WHATSAPP_ACCESS_TOKEN=seu-token
```

2. Use no CLI:
```bash
python3 cli.py influencer post "tema" --phone 5511999999999
```

### n8n Webhook

1. Configure no `.env`:
```
N8N_WEBHOOK_URL=https://seu-webhook.com
```

2. Use no CLI:
```bash
python3 cli.py influencer post "tema" --n8n
```

---

## 🎨 Tipos de Conteúdo

| Tipo | Descrição | Uso |
|------|-----------|-----|
| **post** | Post completo para feed | Instagram, Facebook |
| **story** | Story curto e impactante | Stories, Status |
| **roteiro** | Roteiro para vídeo/reels | Reels, TikTok, YouTube |
| **pacote** | Todos os formatos acima | Campanha completa |

---

## 🌟 Perfil: Influenciadora

### Personalidades

**--personality soft** (padrão)
- Elegante e minimalista
- Confiante e calma
- Provocação sutil

**--personality agressiva**
- Direta e impactante
- Provocativa e marcante
- Frases fortes

### Ousadia (--ousadia 1-10)

- **1-2**: Discreta, clean
- **3-4**: Confiante e elegante
- **5-6**: Provocação sutil ⭐ (padrão)
- **7-8**: Sensual e direta
- **9-10**: Máximo impacto

---

## 💬 Perfil: Fofocas

- Sarcasmo e ironia
- Texto curto e viral
- Gancho imediato
- Fácil de compartilhar

---

## 🧪 Testar o Sistema

```bash
# Executar testes
python3 test_system.py

# Ver exemplos
python3 example_usage.py
```

---

## 📊 Ver Analytics

No dashboard:
1. Vá para aba "Analytics & Memória"
2. Selecione o perfil
3. Clique em "Analisar Perfil"

Ou via Python:
```python
orchestrator = ContentOrchestrator()
analytics = orchestrator.get_profile_analytics("influencer")
print(analytics)
```

---

## 🎨 Gerar Prompts de Imagem (Visual DNA)

No dashboard:
1. Vá para aba "Visual DNA"
2. Configure cenário, roupa e iluminação
3. Clique em "Gerar Prompt de DNA"
4. Copie e use em Stable Diffusion/Midjourney

---

## ❓ Problemas Comuns

**"OpenAI API key not found"**
→ Configure `OPENAI_API_KEY` no `.env`

**"No module named 'openai'"**
→ Execute: `pip install -r requirements.txt`

**"WhatsApp credentials not configured"**
→ Normal! Sistema funciona em modo simulação
→ Configure credenciais para uso real

**Dashboard não abre**
→ Verifique se Streamlit está instalado
→ Execute: `pip install streamlit`

---

## 📚 Documentação Completa

- `README.md` - Documentação completa
- `IMPLEMENTATION.md` - Detalhes técnicos
- `example_usage.py` - Exemplos de código

---

## 🎉 Pronto!

Você está pronto para gerar conteúdo profissional com IA!

**Dica:** Comece com o dashboard para se familiarizar, depois use o CLI para automação.

---

**Precisa de ajuda?** Consulte o README.md completo.
