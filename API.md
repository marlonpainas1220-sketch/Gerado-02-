# 🔌 API & Integração - OpenVibe

## 📋 Índice

- [Visão Geral](#visão-geral)
- [Claude API](#claude-api)
- [Storage API](#storage-api)
- [Criando Apps com APIs Externas](#criando-apps-com-apis-externas)
- [Integrações Populares](#integrações-populares)
- [Exemplos Práticos](#exemplos-práticos)
- [Troubleshooting](#troubleshooting)

---

## 🌟 Visão Geral

### APIs Utilizadas pelo OpenVibe

```
OpenVibe usa 2 APIs principais:

1. Claude API (Anthropic)
   - Geração de código com IA
   - Modelo: Claude Sonnet 4
   - Endpoint: api.anthropic.com

2. Storage API (Browser)
   - Persistência local
   - window.storage
   - localStorage wrapper
```

### Apps Podem Usar Qualquer API

```
Seu app gerado pode integrar com:
✅ REST APIs
✅ GraphQL
✅ WebSocket
✅ Firebase
✅ Supabase
✅ Qualquer API pública
```

---

## 🤖 Claude API

### Como o OpenVibe Usa

```javascript
// Chamada interna do OpenVibe
const response = await fetch('https://api.anthropic.com/v1/messages', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    model: 'claude-sonnet-4-20250514',
    max_tokens: 4000,
    messages: [
      {
        role: 'user',
        content: promptDoUsuario
      }
    ]
  })
});

const data = await response.json();
const codigoGerado = data.content[0].text;
```

### Configuração

**Nenhuma configuração necessária!**
- ✅ OpenVibe já vem configurado
- ✅ Sem necessidade de API key própria
- ✅ Funciona imediatamente

### Limites e Quotas

```
Rate Limits da API:
- Requests: Ilimitados pelo OpenVibe
- Tokens: 4000 por geração
- Timeout: 30 segundos

Dicas:
- Prompts muito longos podem falhar
- Simplifique se der timeout
- Divida apps grandes em partes
```

### Uso Avançado (Customização)

Se quiser usar sua própria API key:

```javascript
// Modifique em openvibe-studio.html
const response = await fetch('https://api.anthropic.com/v1/messages', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'x-api-key': 'sua-api-key-aqui', // ADICIONE ISSO
  },
  body: JSON.stringify({
    model: 'claude-sonnet-4-20250514',
    max_tokens: 4000,
    messages: [...]
  })
});
```

**Vantagens de usar sua key:**
- Controle total
- Logs detalhados
- Analytics própria

**Desvantagens:**
- Custo por uso
- Precisa gerenciar key
- Complexidade adicional

---

## 💾 Storage API

### API Disponível

O OpenVibe fornece `window.storage`:

```javascript
// Salvar dados
await window.storage.set(key, value);

// Buscar dados
const result = await window.storage.get(key);

// Deletar dados
await window.storage.delete(key);

// Listar chaves
const result = await window.storage.list(prefix);
```

### Exemplos de Uso

#### Salvar Projeto
```javascript
const project = {
  id: '123',
  name: 'Meu App',
  code: 'código aqui...',
  created: new Date().toISOString()
};

await window.storage.set(
  `project:${project.id}`,
  JSON.stringify(project)
);
```

#### Carregar Projeto
```javascript
const result = await window.storage.get('project:123');
if (result) {
  const project = JSON.parse(result.value);
  console.log(project.name); // 'Meu App'
}
```

#### Listar Todos os Projetos
```javascript
const result = await window.storage.list('project:');
if (result?.keys) {
  for (const key of result.keys) {
    const data = await window.storage.get(key);
    const project = JSON.parse(data.value);
    console.log(project.name);
  }
}
```

### Limites

```
Storage Limits:
- Tamanho máximo: ~5-10MB (varia por navegador)
- Keys: Ilimitadas (dentro do espaço)
- Tipo: Apenas strings (use JSON.stringify)

Dicas:
- Sempre use try/catch
- Parse JSON ao ler
- Stringify ao salvar
- Limpe projetos antigos regularmente
```

---

## 🌐 Criando Apps com APIs Externas

### Estrutura Básica

```javascript
// Template para apps com API
const App = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchData = async () => {
    setLoading(true);
    setError(null);
    
    try {
      const response = await fetch('https://api.exemplo.com/data');
      const result = await response.json();
      setData(result);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <View>
      {loading && <Text>Carregando...</Text>}
      {error && <Text>Erro: {error}</Text>}
      {data && <Text>Dados: {JSON.stringify(data)}</Text>}
      <Button title="Buscar" onPress={fetchData} />
    </View>
  );
};
```

### Prompt para App com API

```
"Crie um app que busca dados de uma API com:

Setup:
- URL da API: https://api.exemplo.com/users
- Método: GET

Estados:
- data: dados recebidos
- loading: carregando?
- error: erro se houver

UI:
- Botão 'Buscar Dados'
- Loading spinner quando carregando
- Lista de resultados quando sucesso
- Mensagem de erro se falhar

Cada item da lista mostra:
- Nome do usuário
- Email
- Card branco com sombra"
```

---

## 🔥 Integrações Populares

### 1. Weather API (OpenWeather)

#### Prompt
```
"Crie um app de clima que:

API:
- URL: https://api.openweathermap.org/data/2.5/weather
- Params: ?q={cidade}&appid={key}&units=metric&lang=pt_br

UI:
- Input para nome da cidade
- Botão 'Buscar Clima'
- Card mostrando:
  * Nome da cidade
  * Temperatura (grande)
  * Descrição do clima
  * Ícone do clima
  * Umidade e vento

Estados:
- cidade, temperatura, descrição
- loading e error

Design:
- Fundo azul gradiente
- Texto branco
- Ícones grandes"
```

#### Código Gerado (Exemplo)
```javascript
const App = () => {
  const [cidade, setCidade] = useState('');
  const [clima, setClima] = useState(null);
  const [loading, setLoading] = useState(false);

  const buscarClima = async () => {
    setLoading(true);
    try {
      const API_KEY = 'sua-key-aqui';
      const url = `https://api.openweathermap.org/data/2.5/weather?q=${cidade}&appid=${API_KEY}&units=metric`;
      const response = await fetch(url);
      const data = await response.json();
      setClima(data);
    } catch (error) {
      alert('Erro ao buscar clima');
    }
    setLoading(false);
  };

  return (
    <View style={styles.container}>
      <TextInput
        placeholder="Digite a cidade"
        value={cidade}
        onChangeText={setCidade}
      />
      <Button title="Buscar" onPress={buscarClima} />
      
      {loading && <Text>Carregando...</Text>}
      
      {clima && (
        <View style={styles.resultado}>
          <Text style={styles.temp}>{clima.main.temp}°C</Text>
          <Text>{clima.weather[0].description}</Text>
        </View>
      )}
    </View>
  );
};
```

---

### 2. GitHub API

#### Prompt
```
"Crie um app que busca repositórios do GitHub:

API:
- URL: https://api.github.com/users/{username}/repos
- Método: GET
- Sem autenticação necessária

UI:
- Input para username
- Botão 'Buscar Repos'
- Lista de repositórios mostrando:
  * Nome do repo
  * Descrição
  * Estrelas ⭐
  * Linguagem principal
  * Link (não clicável, apenas texto)

Design:
- Header preto (#24292e)
- Cards brancos
- Badges coloridos para linguagens"
```

---

### 3. Rick and Morty API

#### Prompt
```
"Crie um app de personagens de Rick and Morty:

API:
- URL: https://rickandmortyapi.com/api/character
- Método: GET

UI:
- Título 'Rick and Morty Characters'
- Grid 2 colunas de cards
- Cada card mostra:
  * Imagem do personagem
  * Nome
  * Status (vivo/morto/desconhecido)
  * Espécie
  * Origem

Cores:
- Verde limão para vivos
- Vermelho para mortos
- Cinza para desconhecidos

Botão 'Carregar Mais' no final"
```

---

### 4. JSON Placeholder (Fake API)

#### Prompt
```
"Crie um app de posts usando JSON Placeholder:

API:
- Posts: https://jsonplaceholder.typicode.com/posts
- Comments: https://jsonplaceholder.typicode.com/posts/{id}/comments

Features:
- Lista de posts (título e preview)
- Clicar em post mostra:
  * Título completo
  * Corpo do post
  * Lista de comentários
- Botão voltar

UI:
- Header azul
- Posts em cards
- Comentários em lista cinza
- Avatar fake para cada comentário"
```

---

### 5. CoinGecko (Crypto Prices)

#### Prompt
```
"Crie um app de preços de criptomoedas:

API:
- URL: https://api.coingecko.com/api/v3/simple/price
- Params: ?ids=bitcoin,ethereum,cardano&vs_currencies=usd,brl

UI:
- Título 'Crypto Prices'
- Card para cada moeda mostrando:
  * Ícone (emoji)
  * Nome
  * Preço em USD
  * Preço em BRL
- Botão 'Atualizar Preços'
- Timestamp da última atualização

Auto-refresh a cada 30 segundos

Cores:
- Verde se preço subiu
- Vermelho se caiu"
```

---

## 📝 Exemplos Práticos Completos

### Exemplo 1: Todo App com API Backend

#### Prompt
```
"Crie um app de tarefas com backend fake:

API (JSON Placeholder):
- GET /todos - listar tarefas
- POST /todos - criar tarefa
- DELETE /todos/{id} - deletar

Obs: JSON Placeholder simula POST/DELETE
     mas não persiste dados

UI:
- Input + botão adicionar
- Lista de tarefas
- Checkbox para marcar concluída
- Botão deletar

Features:
- Busca tarefas ao abrir
- Adiciona otimisticamente (antes da API)
- Loading states
- Error handling

Design moderno com gradientes"
```

---

### Exemplo 2: Image Search App

#### Prompt
```
"Crie buscador de imagens usando Unsplash:

API:
- URL: https://api.unsplash.com/search/photos
- Params: ?query={busca}&per_page=12
- Header: Authorization: Client-ID {sua-key}

UI:
- Input de busca
- Botão 'Buscar'
- Grid 3 colunas de imagens
- Cada imagem:
  * Foto
  * Nome do fotógrafo
  * Número de likes

Funcionalidade:
- Busca ao pressionar Enter
- Loading placeholder
- Infinite scroll (carregar mais)

Design:
- Masonry layout
- Hover effects
- Modal ao clicar"
```

---

### Exemplo 3: News Reader

#### Prompt
```
"Crie um leitor de notícias:

API:
- URL: https://newsapi.org/v2/top-headlines
- Params: ?country=br&apiKey={key}

UI:
- Header 'Notícias do Brasil'
- Lista de notícias mostrando:
  * Imagem de capa
  * Título
  * Descrição
  * Fonte
  * Data
- Clicar abre em modal ou nova aba

Features:
- Pull to refresh
- Filtros por categoria
- Busca por palavra-chave
- Salvar favoritos (localStorage)

Design:
- Cards estilo jornal
- Imagens responsivas
- Typography clara"
```

---

## 🔧 Troubleshooting de APIs

### Erro: CORS

**Problema:**
```
Access to fetch blocked by CORS policy
```

**Soluções:**
```
✅ Opção 1: Use APIs com CORS habilitado
- Maioria das APIs públicas já tem

✅ Opção 2: Proxy CORS
- https://cors-anywhere.herokuapp.com/
- https://api.allorigins.win/get?url=

✅ Opção 3: Backend próprio
- Crie proxy simples em Node.js
- Faz request server-side
```

**Exemplo com Proxy:**
```javascript
// Ao invés de:
fetch('https://api-sem-cors.com/data')

// Use:
fetch('https://cors-anywhere.herokuapp.com/https://api-sem-cors.com/data')
```

---

### Erro: API Key Exposta

**Problema:**
```
API key visível no código do frontend
```

**Soluções:**
```
✅ Desenvolvimento/Testes:
- Tudo bem usar key direta
- Apenas para aprender

✅ Produção:
- NUNCA exponha keys no frontend
- Use backend proxy
- Environment variables
- Serverless functions (Vercel, Netlify)
```

**Exemplo Seguro:**
```javascript
// Frontend chama seu backend
fetch('https://seu-backend.com/api/weather?city=saopaulo')

// Backend faz chamada real com key
// API key fica segura no servidor
```

---

### Erro: Rate Limit

**Problema:**
```
429 Too Many Requests
```

**Soluções:**
```
✅ Implementar debounce
const debounce = (func, delay) => {
  let timeout;
  return (...args) => {
    clearTimeout(timeout);
    timeout = setTimeout(() => func(...args), delay);
  };
};

✅ Cache de resultados
- Salvar no localStorage
- Não refazer request se dados são recentes

✅ Loading states
- Desabilitar botão durante request
- Prevenir cliques múltiplos
```

---

### Erro: Network Failed

**Problema:**
```
TypeError: Failed to fetch
```

**Soluções:**
```
✅ Sempre use try/catch
try {
  const response = await fetch(url);
  const data = await response.json();
} catch (error) {
  setError('Sem conexão com internet');
}

✅ Timeout
const fetchWithTimeout = (url, timeout = 5000) => {
  return Promise.race([
    fetch(url),
    new Promise((_, reject) =>
      setTimeout(() => reject(new Error('Timeout')), timeout)
    )
  ]);
};

✅ Retry logic
let retries = 3;
while (retries > 0) {
  try {
    return await fetch(url);
  } catch (err) {
    retries--;
    if (retries === 0) throw err;
    await new Promise(r => setTimeout(r, 1000));
  }
}
```

---

## 📚 Recursos Adicionais

### APIs Gratuitas Recomendadas

**Sem Autenticação:**
- https://jsonplaceholder.typicode.com - Fake data
- https://randomuser.me - Random users
- https://dog.ceo/api - Dog images
- https://pokeapi.co - Pokemon data
- https://rickandmortyapi.com - Rick & Morty

**Com API Key Grátis:**
- https://openweathermap.org - Clima
- https://newsapi.org - Notícias
- https://unsplash.com - Imagens
- https://themoviedb.org - Filmes
- https://coingecko.com - Crypto

### Documentação

- **Fetch API:** developer.mozilla.org/pt-BR/docs/Web/API/Fetch_API
- **Async/Await:** javascript.info/async-await
- **REST APIs:** restfulapi.net

### Ferramentas

- **Testar APIs:** Postman, Insomnia
- **Mock APIs:** Mocky.io, JSONPlaceholder
- **CORS Proxy:** cors-anywhere, allorigins

---

## 🎯 Checklist para Apps com API

Antes de lançar seu app com API:

- [ ] Tratamento de erros implementado
- [ ] Loading states em todos requests
- [ ] CORS configurado ou resolvido
- [ ] Rate limiting considerado
- [ ] API keys seguras (se produção)
- [ ] Timeout implementado
- [ ] Cache quando apropriado
- [ ] Testes com internet lenta
- [ ] Testes offline
- [ ] Documentação de endpoints

---

**Última atualização:** Janeiro 2026

**Integre com qualquer API e crie apps incríveis! 🚀**
