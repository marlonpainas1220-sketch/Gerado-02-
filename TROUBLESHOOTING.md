# 🔧 Troubleshooting & FAQ - OpenVibe

## 📋 Índice

- [Problemas Comuns](#problemas-comuns)
- [FAQ - Perguntas Frequentes](#faq---perguntas-frequentes)
- [Otimização de Performance](#otimização-de-performance)
- [Dicas e Truques](#dicas-e-truques)
- [Suporte](#suporte)

---

## 🐛 Problemas Comuns

### 1. "Erro ao gerar código" / "Failed to fetch"

**Sintoma:** Mensagem de erro ao clicar em "Gerar App com IA"

**Causas Possíveis:**
- ❌ Sem conexão com internet
- ❌ API do Claude indisponível
- ❌ Bloqueio de firewall/antivírus
- ❌ Navegador bloqueando requisições

**Soluções:**

```
✅ Solução 1: Verificar Conexão
- Teste sua internet
- Recarregue a página
- Tente novamente

✅ Solução 2: Verificar Console
1. Abra DevTools (F12)
2. Vá para aba "Console"
3. Procure mensagens de erro
4. Compartilhe no Discord/GitHub

✅ Solução 3: Limpar Cache
1. Ctrl+Shift+Delete
2. Limpe cache e cookies
3. Recarregue OpenVibe

✅ Solução 4: Trocar Navegador
- Chrome (recomendado)
- Firefox
- Edge
```

---

### 2. "Preview não aparece" / Tela em branco

**Sintoma:** Área de preview fica vazia ou com erro

**Causas Possíveis:**
- ❌ Erro no código gerado
- ❌ Componente não suportado
- ❌ Sintaxe JavaScript incorreta

**Soluções:**

```
✅ Solução 1: Verificar Logs
- Olhe a seção "Logs" no app
- Procure mensagens de erro em vermelho

✅ Solução 2: Verificar Código
- Vá para aba "Código"
- Procure por erros óbvios
- Verifique se o código está completo

✅ Solução 3: Regenerar
- Use um prompt mais simples
- Ex: "Crie um botão que mostra um alerta"
- Teste se funciona
- Depois faça prompts mais complexos

✅ Solução 4: Usar Template
- Clique em "Templates"
- Escolha "App em Branco" (Studio)
- Modifique a partir daí
```

---

### 3. "Projetos não salvam" / "Dados perdidos"

**Sintoma:** Projetos desaparecem após fechar navegador

**Causas Possíveis:**
- ❌ Modo anônimo/privado ativado
- ❌ Configuração de navegador
- ❌ Storage bloqueado

**Soluções:**

```
✅ Solução 1: Sair do Modo Anônimo
- Não use janela anônima/privada
- Use janela normal do navegador

✅ Solução 2: Permitir Storage
1. Configurações do navegador
2. Privacidade e Segurança
3. Permitir armazenamento local

✅ Solução 3: Exportar Regularmente
- Use botão "Exportar"
- Salve .JSON do projeto
- Faça backup manual

✅ Solução 4: Verificar Espaço
- Storage pode estar cheio
- Delete projetos antigos
- Ou use export/import
```

---

### 4. "Editor de código não funciona" (Studio)

**Sintoma:** Editor CodeMirror não carrega ou não edita

**Causas Possíveis:**
- ❌ CDN do CodeMirror bloqueado
- ❌ JavaScript desabilitado
- ❌ Conflito de extensões

**Soluções:**

```
✅ Solução 1: Verificar CDN
- Verifique se cdnjs.cloudflare.com está acessível
- Tente outro navegador

✅ Solução 2: Desabilitar Extensões
- Desative bloqueadores de script
- Desative extensões uma por uma
- Teste qual está causando problema

✅ Solução 3: Usar Versão Pro
- Se Studio não funcionar
- Use OpenVibe Pro
- Tem 95% dos recursos
```

---

### 5. "Dark mode não funciona"

**Sintoma:** Tema escuro não ativa ou não salva

**Causas Possíveis:**
- ❌ Storage bloqueado
- ❌ Bug temporário

**Soluções:**

```
✅ Solução 1: Recarregar
- Clique no ícone 🌙/☀️ novamente
- Recarregue a página
- Deve persistir

✅ Solução 2: Limpar e Recriar
1. Limpe storage do site
2. Recarregue OpenVibe
3. Ative dark mode novamente

✅ Solução 3: Usar CSS Manual
- Abra DevTools (F12)
- Console: document.documentElement.classList.add('dark')
```

---

## ❓ FAQ - Perguntas Frequentes

### Geral

**Q: OpenVibe é realmente grátis?**
**A:** Sim! 100% grátis, sem assinaturas, sem taxas ocultas, para sempre.

**Q: Preciso de uma API key do Claude?**
**A:** Não! A API é chamada diretamente do navegador sem necessidade de key própria.

**Q: Funciona offline?**
**A:** Não. OpenVibe precisa de internet para gerar código com IA. Mas você pode editar código offline.

**Q: Posso usar comercialmente?**
**A:** Sim! Licença MIT permite uso comercial livre.

**Q: Qual navegador é melhor?**
**A:** Chrome é recomendado. Firefox e Edge também funcionam bem.

---

### Funcionalidades

**Q: Quantos projetos posso criar?**
**A:** Ilimitados! Sem restrições.

**Q: Quantos prompts posso usar?**
**A:** Ilimitados! Use quanto quiser.

**Q: O código gerado é bom?**
**A:** Sim! Usa Claude Sonnet 4, um dos melhores modelos de IA. Mas sempre revise o código.

**Q: Posso editar o código manualmente?**
**A:** Sim! Todas as versões permitem edição manual. Studio tem editor profissional.

**Q: Consigo fazer apps complexos?**
**A:** Sim! Mas apps muito complexos podem precisar de várias iterações e edição manual.

---

### Comparações

**Q: Qual versão devo usar?**
**A:** 
- **Iniciante?** → Basic
- **Uso regular?** → Pro (recomendado)
- **Profissional?** → Studio

**Q: OpenVibe é melhor que Vibecode?**
**A:** 
- ✅ Grátis vs $50-199/mês
- ✅ Prompts ilimitados vs 300
- ✅ Open source vs fechado
- ✅ Mais recursos (Pro/Studio)

**Q: Posso migrar do Vibecode?**
**A:** Sim! Exporte seus apps do Vibecode e recrie no OpenVibe.

**Q: Qual a diferença entre Pro e Studio?**
**A:**
- Pro: 12 templates, dark mode, multi-export
- Studio: +editor profissional, +componentes, +versionamento

---

### Técnicas

**Q: Como fazer bons prompts?**
**A:** Seja específico!
- ❌ "Faça um app"
- ✅ "Crie um contador com botões verdes + e -, número grande roxo no centro, e botão reset cinza"

**Q: Posso usar o código em produção?**
**A:** Sim, mas:
1. Revise o código
2. Teste extensivamente
3. Adicione tratamento de erros
4. Otimize performance

**Q: Como adicionar mais funcionalidades?**
**A:** 
1. Use novo prompt: "Adicione um botão de compartilhar"
2. Ou edite código manualmente
3. Ou use biblioteca de componentes (Studio)

**Q: Posso integrar com APIs?**
**A:** Sim! O código gerado pode fazer fetch de APIs. Peça no prompt:
"Crie um app que busca clima de uma cidade usando API OpenWeather"

---

### Storage e Dados

**Q: Onde meus projetos ficam salvos?**
**A:** No localStorage do navegador. Só você tem acesso.

**Q: Posso acessar de outro computador?**
**A:** Não automaticamente. Use export/import:
1. Exporte projeto como .JSON
2. Salve na nuvem (Drive, Dropbox)
3. Baixe no outro computador
4. Importe manualmente

**Q: Como fazer backup?**
**A:** 
1. Exporte cada projeto (.JSON)
2. Salve em pasta local ou nuvem
3. Ou use botão "Duplicar" regularmente

**Q: Quanto espaço tenho?**
**A:** Geralmente 5-10MB de localStorage. Suficiente para centenas de projetos.

---

### Versões e Updates

**Q: Preciso atualizar o OpenVibe?**
**A:** Não automaticamente. Baixe nova versão quando sair.

**Q: Como saber se há nova versão?**
**A:** 
- Acompanhe no GitHub
- Entre no Discord
- Verifique rodapé do app (versão atual)

**Q: Posso usar múltiplas versões?**
**A:** Sim! Mantenha todas 3 (Basic, Pro, Studio) e use conforme necessário.

**Q: Meus projetos funcionam em todas versões?**
**A:** Sim! Projetos são compatíveis entre versões.

---

## ⚡ Otimização de Performance

### Para Apps Grandes

```javascript
// ✅ BOM: Componentes pequenos e focados
const TodoItem = ({ todo }) => (
  <View>
    <Text>{todo.title}</Text>
  </View>
);

// ❌ RUIM: Componente gigante com tudo
const App = () => {
  // 500 linhas de código...
};
```

### Para Listas Longas

```javascript
// ✅ BOM: Limite inicial de itens
const [items, setItems] = useState(data.slice(0, 20));

// ❌ RUIM: Renderizar 1000 itens de uma vez
const [items, setItems] = useState(allData); // Muito lento!
```

### Para Imagens

```javascript
// ✅ BOM: Imagens otimizadas
<Image 
  source={{ uri: 'url-da-imagem-pequena.jpg' }}
  style={{ width: 100, height: 100 }}
/>

// ❌ RUIM: Imagens muito grandes
<Image source={{ uri: 'imagem-4k.jpg' }} /> // Lento!
```

---

## 💡 Dicas e Truques

### 1. Prompts Eficientes

**Use templates de prompt:**
```
Estrutura recomendada:
"Crie um [tipo de app] com:
- [feature 1]
- [feature 2]
- [feature 3]
Use cores [cores] e design [estilo]"

Exemplo:
"Crie um app de tarefas com:
- Input para adicionar
- Lista com checkbox
- Botão deletar
Use cores roxas e design moderno"
```

### 2. Iteração Incremental

```
Passo 1: "Crie um contador simples"
↓ Funciona!
Passo 2: "Adicione botão de reset"
↓ Funciona!
Passo 3: "Adicione sons ao clicar"
↓ Funciona!
```

### 3. Reutilização (Studio)

```
1. Salve versões funcionais (💾 Salvar Versão)
2. Use biblioteca de componentes
3. Copie código entre projetos
```

### 4. Debugging Rápido

```javascript
// Adicione console.log para debugar
const handleClick = () => {
  console.log('Clicou!'); // Veja no DevTools
  setCount(count + 1);
};
```

### 5. Templates como Base

```
1. Comece com template similar
2. Modifique aos poucos
3. Mais rápido que começar do zero!
```

### 6. Organize Projetos

```
Nomenclatura:
✅ "App Tarefas - v1"
✅ "Calculadora Gorjeta - Cliente X"
✅ "Contador - Teste Dark Mode"

❌ "App1"
❌ "teste"
❌ "asdf"
```

### 7. Use Comentários

```javascript
// ✅ BOM: Código comentado
// Incrementa contador ao clicar
const increment = () => setCount(count + 1);

// ❌ RUIM: Sem comentários
const inc = () => setCount(count + 1);
```

---

## 🎯 Prompts Avançados

### Para Apps com Estado Complexo

```
"Crie um app de quiz com:
- Array de 5 perguntas
- Índice da pergunta atual
- Array de respostas do usuário
- Pontuação total
- Navegação próxima/anterior
- Tela final com resultado"
```

### Para Apps com Formulários

```
"Crie formulário de cadastro com:
- Inputs: nome, email, senha, confirmar senha
- Validação em tempo real
- Botão desabilitado se inválido
- Mensagens de erro embaixo de cada input
- Sucesso mostra resumo"
```

### Para Apps com API

```
"Crie app de clima que:
- Busca clima via fetch de API
- Input para nome da cidade
- Mostra temperatura, condição, ícone
- Loading state enquanto busca
- Tratamento de erro se cidade não existe"
```

---

## 🆘 Suporte

### Canais Oficiais

**🐛 Bugs e Issues:**
- GitHub Issues: [github.com/openvibe/issues](https://github.com/openvibe/issues)

**💬 Discussões e Ajuda:**
- Discord: [discord.gg/openvibe](https://discord.gg/openvibe)
- Canais: #help, #showcase, #general

**📧 Email:**
- Suporte: support@openvibe.dev
- Segurança: security@openvibe.dev

**📚 Documentação:**
- README.md
- QUICKSTART.md
- EXAMPLES.md
- Este arquivo (TROUBLESHOOTING.md)

---

## 📊 Checklist de Troubleshooting

Antes de pedir ajuda, verifique:

- [ ] Estou usando navegador suportado (Chrome/Firefox/Edge)?
- [ ] Tenho conexão com internet?
- [ ] Não estou em modo anônimo?
- [ ] Tentei recarregar a página?
- [ ] Limpei cache do navegador?
- [ ] Vi os logs de erro?
- [ ] Abri o Console (F12)?
- [ ] Tentei com prompt mais simples?
- [ ] Testei em outro navegador?
- [ ] Li a documentação relevante?

---

## 🎓 Recursos de Aprendizado

### Para React Native

- [Documentação Oficial](https://reactnative.dev)
- [React Native Express](https://reactnative.express)

### Para React

- [React Docs](https://react.dev)
- [React Tutorial](https://react.dev/learn)

### Para JavaScript

- [MDN JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)
- [JavaScript.info](https://javascript.info)

---

## 🔄 Reportar Problemas

### Template de Bug Report

```markdown
**Versão:** [Basic/Pro/Studio]
**Navegador:** [Chrome 120 / Firefox 115 / etc]
**OS:** [Windows 11 / macOS 14 / Linux]

**Descrição:**
[Descreva o problema]

**Passos para Reproduzir:**
1. Abrir OpenVibe
2. Clicar em X
3. Ver erro Y

**Comportamento Esperado:**
[O que deveria acontecer]

**Comportamento Atual:**
[O que está acontecendo]

**Console Errors:**
```
[Cole erros do console aqui]
```

**Screenshots:**
[Se aplicável]
```

---

## ✅ Problemas Resolvidos

Lista de problemas já corrigidos:

- ✅ Dark mode não persistia → Corrigido v2.0
- ✅ Preview quebrava com ScrollView → Corrigido v1.5
- ✅ Export JSON faltando campos → Corrigido v2.1
- ✅ CodeMirror não carregava → Corrigido v3.0

---

## 🎉 Ainda com Problemas?

1. **Procure** no GitHub Issues
2. **Pergunte** no Discord #help
3. **Crie** novo issue no GitHub
4. **Email** support@openvibe.dev

**Resposta média:** 24-48h

---

**Última atualização:** Janeiro 2026

*Este guia é atualizado regularmente com novos problemas e soluções.*
