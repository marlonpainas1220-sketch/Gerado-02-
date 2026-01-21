# 🎬 Gerado-02 - Sistema Autônomo de Produção de Conteúdo Digital

Sistema completo de geração de conteúdo usando IA, com dois perfis independentes:
- **Influenciadora de IA**: Conteúdo elegante, provocativo e magnético
- **Página de Fofocas**: Conteúdo viral, sarcástico e impactante

## 🚀 Características

### ✨ Perfis Independentes
- Dois perfis totalmente separados com personalidades únicas
- Memória evolutiva individual para cada perfil
- Sem compartilhamento de contexto entre perfis

### 🧠 Motor de IA
- Geração de conteúdo usando OpenAI GPT-4
- Validação automática de qualidade
- Sistema A/B de personalidade (Soft Power / Agressiva Magnética)
- Escala de ousadia configurável (1-10)

### 📊 Memória Evolutiva
- Aprende com conteúdos anteriores
- Análise de padrões e tendências
- Identificação de melhores performances
- Evolução contínua da qualidade

### 📱 Entrega Automatizada
- Integração com WhatsApp Business API
- Webhook n8n para automação
- Conteúdo pronto para publicação

### 🎨 Visual DNA
- Consistência visual garantida
- Prompts otimizados para geração de imagens
- Manutenção de identidade facial

## 📦 Estrutura do Projeto

```
backend/
├── profiles/           # Perfis de conteúdo
│   ├── base_profile.py
│   ├── influencer_profile.py
│   └── gossip_profile.py
├── engine/            # Motor de geração
│   └── content_generator.py
├── memory/            # Sistema de memória
│   └── memory_manager.py
├── delivery/          # Entrega de conteúdo
│   └── whatsapp_client.py
├── generators/        # Geradores visuais
│   └── visual_dna.py
├── integrations/      # Integrações externas
│   └── instagram.py
└── orchestrator.py    # Orquestrador central
```

## 🛠️ Instalação

1. **Clone o repositório**
```bash
git clone <repo-url>
cd gerado-02
```

2. **Instale as dependências**
```bash
pip install -r requirements.txt
```

3. **Configure as variáveis de ambiente**
```bash
cp .env.example .env
# Edite o .env com suas credenciais
```

Variáveis obrigatórias:
- `OPENAI_API_KEY`: Chave da API OpenAI (obrigatório)

Variáveis opcionais:
- `WHATSAPP_PHONE_NUMBER_ID`: ID do número WhatsApp Business
- `WHATSAPP_ACCESS_TOKEN`: Token de acesso WhatsApp
- `N8N_WEBHOOK_URL`: URL do webhook n8n
- `INSTAGRAM_ACCESS_TOKEN`: Token Instagram
- `INSTAGRAM_ACCOUNT_ID`: ID da conta Instagram
- `REPLICATE_API_TOKEN`: Token Replicate (para imagens)

## 🎮 Como Usar

### 1. Dashboard Web (Recomendado)

```bash
streamlit run dashboard.py
```

Acesse `http://localhost:8501` e use a interface visual para:
- Gerar conteúdo para qualquer perfil
- Configurar personalidade e ousadia
- Ver analytics e memória
- Gerar prompts de Visual DNA

### 2. CLI (Linha de Comando)

```bash
# Influenciadora - Post com Soft Power
python cli.py influencer post "Reflexão sobre autenticidade" --ousadia 5

# Influenciadora - Story agressiva
python cli.py influencer story "Confiança feminina" --personality agressiva --ousadia 8

# Fofocas - Post viral
python cli.py gossip post "Celebridade em situação constrangedora"

# Pacote completo com entrega WhatsApp
python cli.py influencer pacote "Lançamento de coleção" --phone 5511999999999

# Com n8n webhook
python cli.py gossip story "Fofoca quente" --n8n
```

### 3. Programaticamente (Python)

```python
from backend.orchestrator import ContentOrchestrator
from backend.profiles.base_profile import ContentType
from backend.profiles.influencer_profile import PersonalityVersion

# Inicializar
orchestrator = ContentOrchestrator()

# Gerar conteúdo da influenciadora
result = orchestrator.generate_influencer_content(
    content_type=ContentType.POST,
    topic="Autenticidade e confiança",
    personality=PersonalityVersion.SOFT_POWER,
    ousadia=6,
    delivery_phone="5511999999999"  # Opcional
)

print(result["formatted_content"])

# Gerar conteúdo de fofocas
result = orchestrator.generate_gossip_content(
    content_type=ContentType.STORY,
    topic="Escândalo da semana"
)

# Ver analytics
analytics = orchestrator.get_profile_analytics("influencer")
```

Veja mais exemplos em `example_usage.py`.

## 📋 Tipos de Conteúdo

- **POST**: Post completo para feed/Instagram
- **STORY**: Story curto e impactante
- **ROTEIRO**: Roteiro detalhado para vídeo/reels
- **PACOTE_COMPLETO**: Todos os formatos acima

## 🎭 Perfil: Influenciadora de IA

### Personalidades

**SOFT POWER** (Versão A)
- Elegante e minimalista
- Confiante e calma
- Provoca sem confrontar
- Sutileza é poder

**AGRESSIVA MAGNÉTICA** (Versão B)
- Direta e impactante
- Provocativa e marcante
- Frases fortes
- Impacto imediato

### Escala de Ousadia

- **1-2**: Discreta, clean, quase neutra
- **3-4**: Confiante e elegante
- **5-6**: Provocação sutil e consciente (padrão)
- **7-8**: Sensual, direta e marcante
- **9**: Forte, ousada e dominante
- **10**: Máximo impacto estratégico (nunca vulgar)

### Frases-Marca

O sistema usa estrategicamente uma das frases-marca:
- "Nem tudo precisa ser dito."
- "Quem entende, sente."
- "Silêncio também comunica."
- "Presença não se explica."
- "Confiança é linguagem."
- "Não é sobre mostrar. É sobre ser."
- "Algumas coisas se percebem."

## 💬 Perfil: Página de Fofocas

- Sarcasmo e ironia inteligente
- Texto curto e viral
- Gancho imediato
- Fácil de compartilhar
- Emojis estratégicos

## 🔄 Sistema de Memória

O sistema aprende automaticamente:
- Analisa conteúdos anteriores
- Identifica padrões de sucesso
- Elimina repetições fracas
- Evolui com naturalidade
- Mantém consistência de personalidade

## ✅ Validação Automática

Cada conteúdo passa por checklist:
- Coerência com o perfil
- Linguagem natural e humana
- Impacto no início
- Sem repetições desnecessárias
- Tom adequado ao nicho
- Pronto para postar
- CTA sutil e não forçado

## 🎨 Visual DNA

Gera prompts consistentes para:
- Stable Diffusion
- Midjourney
- Replicate
- Outras ferramentas de IA

Garante:
- Mesma identidade facial
- Características físicas consistentes
- Estilo visual coerente
- Qualidade profissional

## 📊 Analytics

Acompanhe:
- Total de conteúdos gerados
- Métricas médias
- Melhores performances
- Tendências de crescimento
- Padrões de sucesso

## 🔧 Modo Automático

Configure agendamentos em `main.py`:

```python
# Rotina da manhã (Stories)
schedule.every().day.at("09:00").do(job_morning_routine)

# Rotina da noite (Feed)
schedule.every().day.at("18:00").do(job_evening_routine)
```

## 🤝 Integrações

### WhatsApp Business API
- Entrega automática de conteúdo
- Formatação otimizada
- Suporte a texto e imagens

### n8n
- Automação de workflows
- Webhooks personalizados
- Integração com outras ferramentas

### Instagram Graph API
- Publicação automática
- Agendamento de posts
- Métricas de performance

## 📝 Formato de Saída

Todo conteúdo segue o formato:

```
PERFIL: [Nome do Perfil]
PERSONALIDADE: [Versão]
OUSADIA: [Nível]

TÍTULO:
[Título chamativo]

TEXTO:
[Texto principal]

STORY:
[Texto para story]

ROTEIRO:
[Roteiro se aplicável]

LEGENDA:
[Legenda para imagem]

CTA:
[Call-to-action]

OBSERVAÇÕES:
[Observações técnicas]
```

## 🐛 Troubleshooting

**Erro: "OpenAI API key not found"**
- Configure `OPENAI_API_KEY` no arquivo `.env`

**Erro: "WhatsApp credentials not configured"**
- Sistema funciona em modo simulação sem credenciais
- Configure `WHATSAPP_PHONE_NUMBER_ID` e `WHATSAPP_ACCESS_TOKEN` para uso real

**Conteúdo não está sendo salvo na memória**
- Verifique permissões da pasta `data/memory`
- Pasta é criada automaticamente na primeira execução

## 📄 Licença

MIT License

## 🙏 Créditos

Desenvolvido com:
- OpenAI GPT-4
- Streamlit
- Python 3.8+

---

**🎬 Gerado-02** - Sistema Autônomo de Produção de Conteúdo Digital