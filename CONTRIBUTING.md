# 🤝 Guia de Contribuição - OpenVibe

Obrigado por considerar contribuir com o OpenVibe! Este documento fornece diretrizes para contribuir com o projeto.

## 📋 Índice

- [Código de Conduta](#código-de-conduta)
- [Como Posso Contribuir?](#como-posso-contribuir)
- [Processo de Desenvolvimento](#processo-de-desenvolvimento)
- [Diretrizes de Código](#diretrizes-de-código)
- [Diretrizes de Commit](#diretrizes-de-commit)
- [Processo de Pull Request](#processo-de-pull-request)

## 📜 Código de Conduta

### Nosso Compromisso

Estamos comprometidos em fazer da participação neste projeto uma experiência livre de assédio para todos, independentemente de idade, tamanho corporal, deficiência, etnia, identidade e expressão de gênero, nível de experiência, nacionalidade, aparência pessoal, raça, religião ou identidade e orientação sexual.

### Padrões

**Comportamentos esperados:**
- ✅ Usar linguagem acolhedora e inclusiva
- ✅ Respeitar pontos de vista e experiências diferentes
- ✅ Aceitar críticas construtivas graciosamente
- ✅ Focar no que é melhor para a comunidade
- ✅ Mostrar empatia com outros membros

**Comportamentos inaceitáveis:**
- ❌ Linguagem ou imagens sexualizadas
- ❌ Trolling, insultos ou ataques pessoais
- ❌ Assédio público ou privado
- ❌ Publicar informações privadas de outros
- ❌ Conduta não profissional

## 🎯 Como Posso Contribuir?

### 1. 🐛 Reportar Bugs

Encontrou um bug? Ajude-nos a melhorar!

**Antes de reportar:**
- Verifique se o bug já não foi reportado
- Teste na versão mais recente
- Colete informações sobre o ambiente

**Como reportar:**
```markdown
## Descrição do Bug
[Descrição clara e concisa]

## Passos para Reproduzir
1. Vá para '...'
2. Clique em '...'
3. Role até '...'
4. Veja o erro

## Comportamento Esperado
[O que deveria acontecer]

## Comportamento Atual
[O que está acontecendo]

## Screenshots
[Se aplicável]

## Ambiente
- Browser: [Chrome 120]
- OS: [Windows 11]
- Versão OpenVibe: [2.0]

## Informações Adicionais
[Qualquer contexto adicional]
```

### 2. 💡 Sugerir Features

Tem uma ideia para melhorar o OpenVibe?

**Antes de sugerir:**
- Verifique se já não foi sugerido
- Confirme que é relevante para o projeto

**Como sugerir:**
```markdown
## Feature Proposta
[Nome da feature]

## Problema que Resolve
[Que problema esta feature resolve?]

## Solução Proposta
[Como você imagina que funcione?]

## Alternativas Consideradas
[Outras soluções que você pensou]

## Mockups/Exemplos
[Se aplicável]
```

### 3. 📖 Melhorar Documentação

Documentação é crucial! Ajude a melhorar:
- Corrigir typos
- Adicionar exemplos
- Clarificar instruções
- Traduzir para outros idiomas

### 4. 🔧 Contribuir com Código

Quer adicionar uma feature ou corrigir um bug?

## 🛠️ Processo de Desenvolvimento

### Setup do Ambiente

1. **Fork o repositório**
   ```bash
   # No GitHub, clique em "Fork"
   ```

2. **Clone seu fork**
   ```bash
   git clone https://github.com/SEU-USUARIO/openvibe.git
   cd openvibe
   ```

3. **Configure upstream**
   ```bash
   git remote add upstream https://github.com/openvibe/openvibe.git
   ```

4. **Teste localmente**
   - Abra `openvibe-pro.html` no navegador
   - Teste todas as funcionalidades

### Estrutura do Projeto

```
openvibe/
├── openvibe-app.html          # Versão básica
├── openvibe-pro.html          # Versão Pro com features extras
├── README.md                  # Documentação principal
├── QUICKSTART.md             # Guia rápido
├── EXAMPLES.md               # Exemplos de apps
├── COMPARISON.md             # Comparação com Vibecode
├── CONTRIBUTING.md           # Este arquivo
├── LICENSE                   # Licença MIT
└── docs/                     # Documentação adicional
    ├── api.md               # Documentação da API
    ├── architecture.md      # Arquitetura do sistema
    └── templates.md         # Guia de templates
```

## 📝 Diretrizes de Código

### JavaScript/React

**Boas Práticas:**
```javascript
// ✅ BOM: Nomes descritivos
const generateAppFromPrompt = async (prompt) => {
  // ...
};

// ❌ RUIM: Nomes genéricos
const func = async (p) => {
  // ...
};

// ✅ BOM: Comentários úteis
// Gera código React Native usando Claude API
const generateCode = async () => {
  // ...
};

// ❌ RUIM: Comentários óbvios
// Esta função gera código
const generateCode = async () => {
  // ...
};
```

**Formatação:**
```javascript
// Use 4 espaços para indentação
function example() {
    const value = 42;
    if (value > 0) {
        console.log('positive');
    }
}

// Use aspas simples para strings
const message = 'Hello World';

// Sempre use ponto e vírgula
const name = 'OpenVibe';
const version = '2.0';
```

**React Hooks:**
```javascript
// ✅ BOM: Hooks no topo
const Component = () => {
    const [state, setState] = useState(initial);
    const [other, setOther] = useState(0);
    
    useEffect(() => {
        // ...
    }, []);
    
    return <div>...</div>;
};

// ❌ RUIM: Hooks condicionais
const Component = () => {
    if (condition) {
        const [state, setState] = useState(0); // ❌
    }
};
```

### CSS/Tailwind

**Classes Organizadas:**
```jsx
// ✅ BOM: Agrupadas logicamente
<div className="
    flex items-center justify-between
    px-4 py-6
    bg-white rounded-lg shadow-lg
    hover:shadow-xl transition
">
```

### Performance

**Otimizações:**
```javascript
// ✅ BOM: Memoização quando necessário
const Component = () => {
    const expensiveValue = useMemo(() => {
        return computeExpensiveValue(data);
    }, [data]);
};

// ✅ BOM: Callbacks memoizados
const handleClick = useCallback(() => {
    // ...
}, [dependencies]);

// ✅ BOM: Evitar renderizações desnecessárias
const MemoizedComponent = React.memo(Component);
```

## 💬 Diretrizes de Commit

### Formato de Mensagem

```
<tipo>(<escopo>): <assunto>

<corpo>

<rodapé>
```

### Tipos

- `feat`: Nova feature
- `fix`: Correção de bug
- `docs`: Documentação
- `style`: Formatação, ponto e vírgula, etc
- `refactor`: Refatoração de código
- `test`: Adição de testes
- `chore`: Manutenção, configs, etc

### Exemplos

```bash
# Feature
feat(templates): adiciona template de calculadora IMC

Implementa novo template para calcular IMC com:
- Input de peso e altura
- Cálculo automático
- Classificação por cor
- Tabela de referência

Closes #123

# Bug fix
fix(preview): corrige erro ao renderizar images

O preview estava quebrando quando o código continha
componentes Image sem source definido.

Fixes #456

# Documentação
docs(readme): atualiza instruções de instalação

Adiciona passos para Windows e macOS
```

## 🔄 Processo de Pull Request

### 1. Crie uma Branch

```bash
git checkout -b feature/minha-feature
# ou
git checkout -b fix/meu-bugfix
```

### 2. Faça Suas Mudanças

- Escreva código limpo
- Adicione comentários quando necessário
- Teste tudo localmente
- Siga as diretrizes de código

### 3. Commit Suas Mudanças

```bash
git add .
git commit -m "feat(feature): descrição clara"
```

### 4. Mantenha Atualizado

```bash
git fetch upstream
git rebase upstream/main
```

### 5. Push para Seu Fork

```bash
git push origin feature/minha-feature
```

### 6. Crie o Pull Request

No GitHub:
1. Vá para seu fork
2. Clique em "Pull Request"
3. Preencha o template:

```markdown
## Descrição
[Descrição clara do que foi mudado]

## Tipo de Mudança
- [ ] Bug fix
- [ ] Nova feature
- [ ] Breaking change
- [ ] Documentação

## Como Foi Testado?
[Descreva os testes realizados]

## Checklist
- [ ] Meu código segue as diretrizes
- [ ] Realizei auto-review
- [ ] Comentei código complexo
- [ ] Atualizei documentação
- [ ] Minhas mudanças não geram warnings
- [ ] Testei localmente

## Screenshots
[Se aplicável]
```

### 7. Review Process

- Mantenedores revisarão seu PR
- Podem solicitar mudanças
- Discuta feedbacks educadamente
- Faça ajustes se necessário
- Aguarde aprovação

## 🎨 Features Prioritárias

Interessado em contribuir mas não sabe por onde começar? Aqui estão algumas features que precisamos:

### Alta Prioridade 🔴

- [ ] **Modo Offline**: Cache de código e projetos
- [ ] **Mais Templates**: Expandir de 12 para 50+
- [ ] **Testes Unitários**: Cobertura de 80%+
- [ ] **Integração GitHub**: Export direto para repo
- [ ] **Componentes Customizados**: Biblioteca expandida

### Média Prioridade 🟡

- [ ] **Colaboração em Tempo Real**: WebRTC
- [ ] **Versionamento**: Git-like para projetos
- [ ] **Preview em Dispositivo**: QR code para teste
- [ ] **Marketplace**: Compartilhar templates
- [ ] **Temas Customizados**: Além de dark/light

### Baixa Prioridade 🟢

- [ ] **Integração n8n**: Automações
- [ ] **Deploy Expo**: Um clique para publicar
- [ ] **Analytics**: Estatísticas de uso
- [ ] **Tradução i18n**: Múltiplos idiomas
- [ ] **Acessibilidade**: WCAG 2.1 AA

## 🏷️ Labels do GitHub

Usamos estas labels para organizar issues e PRs:

- `bug` - Algo não está funcionando
- `enhancement` - Nova feature ou melhoria
- `documentation` - Melhorias na documentação
- `good first issue` - Bom para iniciantes
- `help wanted` - Precisamos de ajuda extra
- `priority: high` - Alta prioridade
- `priority: medium` - Média prioridade
- `priority: low` - Baixa prioridade
- `wontfix` - Não será trabalhado

## 🎓 Recursos para Contribuidores

### Aprendendo React
- [Documentação Oficial React](https://react.dev)
- [React Hooks Tutorial](https://react.dev/learn)

### Aprendendo React Native
- [React Native Docs](https://reactnative.dev)
- [Expo Docs](https://docs.expo.dev)

### Claude API
- [Anthropic Docs](https://docs.anthropic.com)
- [Claude API Reference](https://docs.anthropic.com/api)

## 💪 Reconhecimento

Contribuidores são reconhecidos de várias formas:

### README Contributors Section
Seu nome/GitHub será adicionado ao README

### Release Notes
Contribuições significativas são mencionadas

### Hall of Fame
Top contribuidores no site

### Swag
Contribuidores ativos recebem swag!

## 📞 Canais de Comunicação

### GitHub Issues
Para bugs, features, e discussões técnicas

### Discord
Para chat em tempo real e ajuda
- `#general` - Discussões gerais
- `#development` - Desenvolvimento
- `#help` - Pedir ajuda
- `#showcase` - Mostre seus apps

### Email
Para questões privadas: contribute@openvibe.dev

## ❓ FAQ para Contribuidores

**P: Preciso saber React para contribuir?**
R: Não! Você pode contribuir com docs, exemplos, testes, design, etc.

**P: Quanto tempo leva para meu PR ser revisado?**
R: Geralmente 2-5 dias. PRs pequenos são mais rápidos.

**P: Posso trabalhar em features grandes?**
R: Sim! Mas abra uma issue primeiro para discutir.

**P: Encontrei uma vulnerabilidade de segurança.**
R: Não abra issue pública! Email: security@openvibe.dev

**P: Posso ser pago para contribuir?**
R: OpenVibe é open source voluntário. Mas aceitamos sponsorship!

**P: Minha contribuição foi rejeitada, e agora?**
R: Não desista! Peça feedback e tente novamente.

## 🎉 Primeiros Passos

Pronto para contribuir? Aqui está um checklist:

- [ ] Li o README
- [ ] Li o Código de Conduta
- [ ] Entendi as diretrizes
- [ ] Configurei ambiente local
- [ ] Encontrei um issue "good first issue"
- [ ] Discuti no issue/Discord
- [ ] Criei fork e branch
- [ ] Fiz as mudanças
- [ ] Testei localmente
- [ ] Criei Pull Request

## 🙏 Agradecimentos

Obrigado por dedicar seu tempo para contribuir com OpenVibe! Juntos tornamos o desenvolvimento de apps mais acessível para todos.

### Agradecimentos Especiais

- Todos os contribuidores
- Anthropic pelo Claude API
- React e React Native teams
- Comunidade open source

---

**Questions?** Abra uma issue ou entre no Discord!

**Ready to contribute?** Fork o repo e comece! 🚀

*Última atualização: Janeiro 2026*
