# OpenVibe - AI App Builder Open Source

![OpenVibe](https://img.shields.io/badge/OpenVibe-Open%20Source-purple)
![License](https://img.shields.io/badge/license-MIT-green)
![React](https://img.shields.io/badge/React-18.2-blue)

**OpenVibe** é uma alternativa 100% open source ao Vibecode - um construtor de aplicativos mobile com IA que permite criar apps React Native através de prompts em linguagem natural.

## 🚀 Características

### ✨ Principais Funcionalidades

- **🤖 Geração com IA**: Use Claude AI para gerar código React Native completo
- **💾 Múltiplos Projetos**: Crie e gerencie quantos projetos quiser
- **📱 Preview em Tempo Real**: Visualize seu app instantaneamente
- **💻 Editor de Código**: Edite manualmente o código gerado
- **📊 Sistema de Logs**: Acompanhe todas as operações
- **📥 Exportação**: Baixe o código para usar no React Native
- **🔄 Histórico**: Veja todas as iterações do projeto
- **💰 100% Grátis**: Sem limites de prompts ou pagamentos

### 🆚 Comparação com Vibecode

| Recurso | OpenVibe | Vibecode |
|---------|----------|----------|
| Preço | Grátis | $50-199/mês |
| Prompts | Ilimitados | 300-ilimitados |
| Open Source | ✅ Sim | ❌ Não |
| Código Exportável | ✅ Sim | ✅ Sim |
| Preview Local | ✅ Sim | ✅ Sim |
| Projetos | Ilimitados | Ilimitados |

## 🎯 Como Usar

### Instalação

1. **Clone ou baixe o arquivo HTML**
   ```bash
   git clone https://github.com/seu-usuario/openvibe
   cd openvibe
   ```

2. **Abra o arquivo no navegador**
   - Simplesmente abra `openvibe-app.html` no seu navegador
   - Recomendado: Chrome, Firefox ou Edge

### Primeiros Passos

1. **Crie um Novo Projeto**
   - Clique em "Novo Projeto"
   - Dê um nome ao seu projeto
   - Clique em "Criar"

2. **Gere seu App com IA**
   - Digite um prompt descrevendo o app desejado
   - Exemplo: "Crie um app de lista de tarefas com opção de marcar como concluído"
   - Clique em "Gerar App com IA"
   - Aguarde a geração (15-30 segundos)

3. **Visualize e Edite**
   - Veja o preview em tempo real no painel direito
   - Edite o código manualmente se necessário
   - Faça novas iterações com prompts adicionais

4. **Export e Use**
   - Clique em "Exportar" para baixar o código
   - Use o código em um projeto React Native real

## 📝 Exemplos de Prompts

### Apps Simples
```
Crie um contador com botões de incrementar e decrementar
```

### Apps de Produtividade
```
Crie um app de lista de tarefas com:
- Input para adicionar tarefas
- Lista de tarefas com checkbox
- Botão para deletar tarefas
- Contador de tarefas pendentes
```

### Apps Interativos
```
Crie um app de quiz com:
- 5 perguntas sobre geografia
- Botões de resposta múltipla
- Pontuação no final
- Botão para reiniciar
```

### Apps de Utilidade
```
Crie uma calculadora de gorjeta com:
- Input para valor da conta
- Slider para escolher porcentagem
- Mostra valor da gorjeta e total
- Opção de dividir entre pessoas
```

## 🛠️ Tecnologias Utilizadas

- **React 18.2**: Framework principal
- **Tailwind CSS**: Estilização
- **Claude API (Sonnet 4)**: Geração de código com IA
- **Storage API**: Persistência local de projetos
- **React Native Components**: Biblioteca de componentes

## 🏗️ Arquitetura

```
OpenVibe
├── Interface React
│   ├── Gerenciador de Projetos
│   ├── Editor de Código
│   └── Preview em Tempo Real
├── Integração Claude AI
│   ├── Geração de Código
│   └── Iterações
└── Storage Local
    ├── Projetos
    └── Histórico
```

## 🎨 Componentes Suportados

O OpenVibe suporta os seguintes componentes React Native:

- `View` - Container principal
- `Text` - Texto
- `Button` - Botão
- `TextInput` - Campo de entrada
- `ScrollView` - Área rolável
- `Image` - Imagem
- `TouchableOpacity` - Elemento clicável

## 📦 Estrutura do Código Gerado

```javascript
import React, { useState } from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';

const App = () => {
  // Estado do componente
  const [state, setState] = useState(initialValue);
  
  // Handlers
  const handleAction = () => {
    // Lógica
  };
  
  return (
    <View style={styles.container}>
      {/* UI Components */}
    </View>
  );
};

const styles = StyleSheet.create({
  // Estilos
});

export default App;
```

## 🔧 Configuração Avançada

### Usando com Sua Própria API Key

O OpenVibe usa a API do Claude diretamente no navegador. Para uso em produção com sua própria key:

1. Modifique a seção da API:
```javascript
const response = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'x-api-key': 'SUA_API_KEY_AQUI', // Adicione sua key
    },
    // ...
});
```

### Customizando o System Prompt

Você pode ajustar o comportamento da IA editando o `systemPrompt`:

```javascript
const systemPrompt = `Você é um expert em React Native...`;
```

## 🚀 Deploy

### Hospedagem Gratuita

1. **Netlify Drop**
   - Acesse [Netlify Drop](https://app.netlify.com/drop)
   - Arraste o arquivo HTML
   - Pronto!

2. **GitHub Pages**
   ```bash
   git add openvibe-app.html
   git commit -m "Deploy OpenVibe"
   git push origin main
   ```
   - Ative GitHub Pages nas configurações

3. **Vercel**
   - Crie conta no [Vercel](https://vercel.com)
   - Import do GitHub
   - Deploy automático

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/NovaFeature`)
5. Abra um Pull Request

## 📋 Roadmap

- [ ] Suporte a mais componentes React Native
- [ ] Integração com Expo
- [ ] Templates pré-configurados
- [ ] Compartilhamento de projetos
- [ ] Temas dark/light
- [ ] Colaboração em tempo real
- [ ] Versionamento de código
- [ ] Testes automatizados
- [ ] Build para Android/iOS

## 🐛 Bugs Conhecidos

- Preview pode não funcionar para componentes muito complexos
- Alguns estilos avançados podem não renderizar corretamente
- Imagens externas podem não carregar no preview

## 📄 Licença

MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🙏 Agradecimentos

- Inspirado no [Vibecode](https://vibecodeapp.com)
- Powered by [Anthropic Claude](https://anthropic.com)
- UI inspirada em ferramentas modernas de desenvolvimento

## 📞 Suporte

- 📧 Email: support@openvibe.dev
- 💬 Discord: [OpenVibe Community](https://discord.gg/openvibe)
- 🐛 Issues: [GitHub Issues](https://github.com/seu-usuario/openvibe/issues)

## 🌟 Star History

Se você gostou do projeto, dê uma ⭐️ no GitHub!

---

**Feito com ❤️ pela comunidade open source**

OpenVibe - Construa apps incríveis sem limites!
