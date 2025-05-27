# 🤖 Chatbot Flask + Groq (Llama-3) - Sistema Completo

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-green?logo=flask)](https://flask.palletsprojects.com/)
[![React](https://img.shields.io/badge/React-18%2B-blue?logo=react)](https://reactjs.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?logo=sqlalchemy)](https://www.sqlalchemy.org/)
[![Groq API](https://img.shields.io/badge/Groq-API-orange)](https://console.groq.com/)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> Sistema completo de chatbot inteligente com múltiplas personalidades de IA, persistência de sessões, interface web moderna e integração com a API Groq (Llama-3). Inclui backend Flask robusto e frontend React responsivo.

---

## ✨ Funcionalidades

### 🚀 Backend (Flask)
- **API REST** completa para interação com o chatbot
- **Sistema de sessões** persistente com SQLAlchemy
- **Múltiplas personalidades de IA** (nutricionista, médico, psicólogo, veterinário, licitações)
- **Gerenciamento de prompts** dinâmico via arquivos JSON
- **Suporte a bancos** SQLite e PostgreSQL
- **Testes automatizados** com pytest
- **CORS habilitado** para integração frontend/backend

### 🎨 Frontend 
- **Interface HTML/JS** moderna e responsiva
- **Interface React** alternativa (em desenvolvimento)
- **Seleção de personalidades** em tempo real
- **Gerenciamento de sessões** via localStorage
- **Chat em tempo real** com indicadores visuais

### 🔧 Recursos Técnicos
- **Arquitetura modular** com services, routes e models separados
- **Sistema de configuração** flexível via variáveis de ambiente
- **Logging** estruturado para debug e monitoramento
- **Validação de dados** e tratamento de erros robusto

---

## 📦 Requisitos

### Backend
- Python 3.8+
- Conta e chave de API Groq
- SQLite (incluído) ou PostgreSQL (opcional)

### Frontend (opcional)
- Node.js 16+ (para React)
- npm ou yarn

---

## 🛠️ Instalação

### Backend (Flask)

1. **Clone o repositório:**
   ```sh
   git clone https://github.com/aldeandersantos/Chatbot_IA.git
   cd Chatbot_IA
   ```

2. **Instale as dependências Python:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Configure as variáveis de ambiente:**
   
   Copie o arquivo `.env.example` para `.env` e configure:
   ```env
   # Configurações da API Groq
   GROQ_API_KEY="sua_chave_api_groq"
   GROQ_API_URL="https://api.groq.com/openai/v1/chat/completions"
   MODEL_NAME="llama3-70b-8192"
   
   # Configurações do Banco de Dados
   DATABASE_URL="sqlite:///./chatbot.db"  # Para SQLite
   # DATABASE_URL="postgresql://usuario:senha@localhost:5432/chatbot_flask"  # Para PostgreSQL
   
   # Configurações do Flask
   FLASK_SECRET_KEY="sua_chave_secreta_segura"
   FLASK_ENV="development"
   ```

4. **Inicialize o banco de dados:**
   ```sh
   python -c "from db.create_tables import *"
   ```

### Frontend (Opcional)

Para usar a interface React:

1. **Navegue para o diretório frontend:**
   ```sh
   cd frontend
   ```

2. **Instale as dependências:**
   ```sh
   npm install
   ```

---

## ▶️ Como usar

### 🔴 Método 1: Interface HTML Standalone

1. **Inicie apenas o backend Flask:**
   ```sh
   python app.py
   ```

2. **Abra a interface web:**
   
   Navegue até: `http://localhost:5000` ou abra o arquivo `frontend/public/index.html` diretamente no navegador.

### 🔵 Método 2: Interface React (Desenvolvimento)

1. **Em um terminal, inicie o backend:**
   ```sh
   python app.py
   ```

2. **Em outro terminal, inicie o frontend React:**
   ```sh
   cd frontend
   npm start
   ```

3. **Acesse:** `http://localhost:3000`

### 🟡 Método 3: API REST Direta

Envie requisições POST para `http://localhost:5000/chat`:

**Exemplo básico:**
```json
{
  "message": "Olá, preciso de ajuda nutricional!"
}
```

**Exemplo com personalidade específica:**
```json
{
  "message": "Como cuidar do meu cachorro?",
  "personality": "veterinario",
  "session_id": "sessao-123"
}
```

**Exemplo com curl:**
```sh
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Olá!", "personality": "medico"}'
```

**Resposta esperada:**
```json
{
  "response": "Olá! Como posso ajudar com suas questões de saúde hoje?",
  "session_id": "uuid-gerado-automaticamente",
  "personality": "medico"
}
```

---

## 🤖 Personalidades de IA Disponíveis

O sistema inclui múltiplas personalidades especializadas:

| Personalidade | Especialização | Exemplo de Uso |
|---------------|----------------|----------------|
| 🥗 **nutricionista** | Nutrição e alimentação | Planos alimentares, orientações nutricionais |
| 👩‍⚕️ **medico** | Saúde geral | Informações médicas, prevenção, sintomas |
| 🧠 **psicologo** | Saúde mental | Bem-estar emocional, técnicas de relaxamento |
| 🐕 **veterinario** | Cuidados animais | Saúde pet, alimentação animal, comportamento |
| 📋 **jose_reinaldo_licitacoes** | Licitações públicas | Assessoria para vender ao governo |

### Endpoints da API

```
GET  /personalities              # Lista todas as personalidades
GET  /personality/{tipo}         # Info sobre personalidade específica
POST /chat                       # Enviar mensagem para o chatbot
```

---

## 📁 Estrutura do Projeto

```
Chatbot_Inteligente/
├── 🐍 Backend (Flask)
│   ├── app.py                   # Aplicação principal
│   ├── config.py                # Configurações
│   ├── requirements.txt         # Dependências Python
│   ├── .env.example            # Exemplo de configuração
│   │
│   ├── 🛣️ routes/              # Rotas da API
│   │   ├── __init__.py
│   │   └── chat.py             # Endpoints do chat
│   │
│   ├── 🔧 services/            # Serviços de negócio
│   │   ├── __init__.py
│   │   ├── groq_service.py     # Integração Groq API
│   │   ├── session_service.py  # Gerenciamento de sessões
│   │   └── prompt_service.py   # Gerenciamento de prompts
│   │
│   ├── 🗄️ db/                  # Banco de dados
│   │   ├── __init__.py
│   │   ├── models.py           # Modelos SQLAlchemy
│   │   ├── db.py              # Configuração do banco
│   │   ├── session_storage.py  # Armazenamento de sessões
│   │   ├── session_utils.py    # Utilitários de sessão
│   │   └── create_tables.py    # Criação de tabelas
│   │
│   ├── 🤖 ia_roles/            # Configuração das personalidades
│   │   ├── personality.json    # Definições das personalidades
│   │   ├── roles.json         # Regras gerais dos assistentes
│   │   └── *.example.json     # Exemplos de configuração
│   │
│   └── 🧪 tests/              # Testes automatizados
│       ├── test.py            # Testes do sistema
│       └── pytest.ini         # Configuração pytest
│
├── 🎨 Frontend
│   ├── 📄 public/             # Interface HTML standalone
│   │   └── index.html         # Chat completo em HTML/JS
│   │
│   └── ⚛️ src/               # Interface React (opcional)
│       ├── App.js
│       ├── index.js
│       ├── components/
│       │   └── Chat.js        # Componente de chat React
│       └── package.json
│
├── 📝 Documentação
│   ├── README.md              # Este arquivo
│   └── .gitignore            # Arquivos ignorados
│
└── 💾 Dados (gerados)
    ├── chatbot.db             # Banco SQLite
    └── sessions/              # Sessões em arquivo (backup)
```

---

## 🧪 Testes

Execute os testes automatizados:

```sh
# Executar todos os testes
pytest

# Executar com mais detalhes
pytest -v

# Executar teste específico
pytest tests/test.py::TestChatEndpoint::test_chat_sucesso
```

---

## 🔧 Configuração Avançada

### Personalização de Personalidades

Edite os arquivos em `ia_roles/`:
- `personality.json`: Define as personalidades e suas características
- `roles.json`: Define regras gerais aplicadas a todas as personalidades

### Banco de Dados

**SQLite (padrão):**
```env
DATABASE_URL="sqlite:///./chatbot.db"
```

**PostgreSQL:**
```env
DATABASE_URL="postgresql://usuario:senha@localhost:5432/nome_banco"
```

### Variáveis de Ambiente Completas

```env
# API Groq
GROQ_API_KEY="sua_chave_groq"
GROQ_API_URL="https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME="llama3-70b-8192"

# Banco de Dados  
DATABASE_URL="sqlite:///./chatbot.db"

# Flask
FLASK_SECRET_KEY="chave_secreta_super_segura"
FLASK_ENV="development"  # ou "production"
```

---

## 🚀 Deployment

### Desenvolvimento Local
```sh
python app.py  # Backend na porta 5000
cd frontend && npm start  # Frontend na porta 3000 (opcional)
```

### Produção
1. Configure `FLASK_ENV="production"` no `.env`
2. Use um servidor WSGI como Gunicorn:
   ```sh
   pip install gunicorn
   gunicorn app:app
   ```
3. Configure um proxy reverso (Nginx) se necessário

---

## 📚 Exemplos de Uso

### Chat com Nutricionista
```json
POST /chat
{
  "message": "Preciso de um plano alimentar para perder peso",
  "personality": "nutricionista"
}
```

### Consulta Veterinária
```json
POST /chat
{
  "message": "Meu gato não está comendo bem",
  "personality": "veterinario"
}
```

### Sessão Continuada
```json
POST /chat
{
  "message": "Continue nossa conversa anterior",
  "session_id": "sessao-existente-123",
  "personality": "medico"
}
```

---

## 🔍 API Reference

### POST `/chat`
Envia mensagem para o chatbot.

**Body:**
```json
{
  "message": "string (obrigatório)",
  "personality": "string (opcional, padrão: nutricionista)",
  "session_id": "string (opcional, gera automaticamente se vazio)"
}
```

**Response:**
```json
{
  "response": "Resposta da IA",
  "session_id": "ID da sessão",
  "personality": "Personalidade utilizada"
}
```

### GET `/personalities`
Lista personalidades disponíveis.

**Response:**
```json
{
  "personalities": ["nutricionista", "medico", "psicologo", "veterinario"],
  "default": "nutricionista"
}
```

### GET `/personality/{tipo}`
Informações sobre personalidade específica.

**Response:**
```json
{
  "personality": "nutricionista",
  "system_prompt": "Prompt detalhado da personalidade..."
}
```

---

## 🤝 Contribuição

Contribuições são muito bem-vindas! Para contribuir:

1. **Fork** o projeto
2. **Crie** uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. **Push** para a branch (`git push origin feature/AmazingFeature`)
5. **Abra** um Pull Request

### Áreas que Precisam de Ajuda
- 🎨 Melhorias na interface React
- 🧪 Mais testes automatizados
- 📱 Versão mobile
- 🌐 Internacionalização
- 🔒 Autenticação de usuários
- 📊 Dashboard de administração

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🙏 Agradecimentos

- [Groq](https://groq.com/) pela excelente API de IA
- [Flask](https://flask.palletsprojects.com/) pelo framework web
- [React](https://reactjs.org/) pela biblioteca frontend
- [SQLAlchemy](https://www.sqlalchemy.org/) pelo ORM
- Comunidade open source

---

**⭐ Se este projeto foi útil para você, considere dar uma estrela no GitHub!**
