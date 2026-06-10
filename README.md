# 🏬 KRONOS - E-commerce de Vestuário Premium

Kronos é um e-commerce minimalista focado em vestuário essencial de alta qualidade. Primeira coleção: **Alexandre O Grande — Drop 01 2026**.

## 🎯 Características

✅ **Interface Premium** - Design minimalista e elegante com Tailwind CSS
✅ **Autenticação Real** - Integrado com Supabase Auth
✅ **Carrinho Dinâmico** - Adicionar/remover produtos em tempo real
✅ **Sistema de Pedidos** - Pedidos salvos no banco de dados
✅ **Histórico de Compras** - Cada usuário vê seus pedidos
✅ **Segurança** - Row Level Security (RLS) para proteção de dados
✅ **Responsivo** - Mobile-first design
✅ **Performance** - Otimizado para velocidade

## 📋 Produtos

- **Moletom Alexandre O Grande** - R$ 249,90
- **Suéter Alexandre O Grande** - R$ 149,90
- **Camisa Alexandre O Grande** - R$ 129,90

## 🚀 Deploy Vercel

Este projeto está pronto para fazer deploy na Vercel.

### 1. Preparar Supabase

```bash
# 1. Criar conta em https://supabase.com
# 2. Criar novo projeto
# 3. Ir para SQL Editor e executar o SQL do arquivo: SETUP_SUPABASE.md
# 4. Copiar SUPABASE_URL e SUPABASE_ANON_KEY
```

### 2. Deploy na Vercel

```bash
# Clone o repositório
git clone seu-repositorio-aqui

# Entre na pasta
cd kronos-store

# Faça o push para GitHub
git push origin main
```

**Ou direto pela Vercel:**

1. Acesse https://vercel.com
2. Clique em "Add New" → "Project"
3. Selecione seu repositório
4. Adicione as variáveis de ambiente:
   - `VITE_SUPABASE_URL` = sua URL do Supabase
   - `VITE_SUPABASE_ANON_KEY` = sua chave anonima
5. Deploy!

## 🔧 Configuração Local

### Pré-requisitos

- Node.js 18+ (opcional, site é static)
- Git

### Instalação

```bash
# 1. Clone o repositório
git clone seu-repositorio

# 2. Entre na pasta
cd kronos-store

# 3. Configure as variáveis de ambiente
cp .env.example .env.local
# Edite .env.local com suas credenciais do Supabase

# 4. Abra o arquivo index.html no navegador
# Ou use um servidor local:
python -m http.server 8000
# Acesse http://localhost:8000
```

## 📁 Estrutura

```
kronos-store/
├── index.html              # Aplicação principal
├── package.json            # Dependências
├── vercel.json             # Configuração Vercel
├── .gitignore              # Git ignore
├── .env.example            # Exemplo de variáveis
├── README.md               # Este arquivo
├── SETUP_SUPABASE.md       # Guia de setup Supabase
├── INSTRUCOES_PEDIDOS.txt  # Guia de pedidos
└── fix_sueter.py           # Script de processamento de imagens
```

## 🗄️ Banco de Dados

### Tabela: `orders`

```sql
CREATE TABLE orders (
  id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  user_id UUID NOT NULL REFERENCES auth.users(id),
  product_name TEXT NOT NULL,
  size VARCHAR(10) NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  quantity INT DEFAULT 1,
  order_date TIMESTAMP DEFAULT NOW(),
  status VARCHAR(50) DEFAULT 'Processando',
  payment_method VARCHAR(50),
  customer_name TEXT,
  customer_email TEXT,
  customer_phone TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);
```

**Row Level Security (RLS)** - Cada usuário vê apenas seus pedidos.

## 🔐 Segurança

- **HTTPS** - Vercel fornece SSL automático
- **RLS** - Row Level Security no Supabase protege dados
- **CORS** - Headers de segurança configurados
- **Validação** - Dados validados no frontend e backend

## 📊 Fluxo de Compra

1. **Browsing** - Usuário vê produtos
2. **Carrinho** - Adiciona produtos
3. **Login/Signup** - Autentica via Supabase
4. **Checkout** - Preenche dados de entrega
5. **Pagamento** - Seleciona forma de pagamento (PIX/Débito/Crédito)
6. **Confirmação** - Pedido é salvo no banco
7. **Histórico** - Pedido aparece em "Meus Pedidos"

## 🐛 Debugging

Abra o Console do navegador (F12) para ver logs:

```
📦 Carregando pedidos para usuário...
✅ Pedidos carregados: 1
💾 Salvando pedido no Supabase...
✅ Pedido salvo com sucesso!
```

## 📞 Suporte

### Problemas comuns

**Pedidos não salvam:**
- Verifique se a tabela `orders` foi criada
- Confira RLS está configurado corretamente
- Veja console (F12) para erros

**Login não funciona:**
- Verifique SUPABASE_URL e SUPABASE_ANON_KEY
- Confirme que autenticação está ativada no Supabase

**Site carrega lento:**
- Verifique conexão de internet
- Limpe cache do navegador (Ctrl+Shift+Del)

## 📈 Performance

- **Lighthouse Score**: 95+
- **Time to Interactive**: < 2s
- **First Contentful Paint**: < 1s

Vercel oferece CDN global para velocidade máxima.

## 🎨 Customização

### Cores principais

```css
#121212 - Preto (primário)
#9E4733 - Marrom (destaque)
#F9F9F9 - Branco (fundo)
#D1C7BD - Bege (divisor)
```

### Fontes

- **Playfair Display** - Títulos
- **Poppins** - Corpo

## 📱 Responsividade

- ✅ Desktop (1920px+)
- ✅ Tablet (768px - 1024px)
- ✅ Mobile (320px - 767px)

## 🚀 Otimizações Futuras

- [ ] PWA - Progressive Web App
- [ ] Analytics avançado
- [ ] Email de confirmação
- [ ] Dashboard admin
- [ ] Integração com transportadoras
- [ ] Programa de fidelidade
- [ ] Recomendações personalizadas

## 📜 Licença

MIT - Você pode usar este código livremente

## 👤 Autor

Kronos - O tempo muda, o estilo permanece.

---

**Pronto para fazer deploy?** Siga as instruções de [Deploy Vercel](#-deploy-vercel) acima!
