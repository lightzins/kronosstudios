# 🚀 Guia de Deploy - Vercel

## ⚡ Quick Start (5 minutos)

### 1. Prepare Supabase

```bash
# 1. Crie uma conta em https://supabase.com (grátis)
# 2. Crie um novo projeto
# 3. Copie sua URL do projeto (ex: https://seu-projeto.supabase.co)
# 4. Vá para Settings → API para pegar a ANON KEY
# 5. Execute o SQL do arquivo SETUP_SUPABASE.md em SQL Editor
```

### 2. Prepare GitHub

```bash
# 1. Crie um novo repositório em https://github.com/new
# 2. Nome: kronos-store
# 3. Descrição: E-commerce Kronos - Vestuário Premium

# Na sua máquina:
cd "C:\Users\Admin\Desktop\kronos store"
git init
git add .
git commit -m "Initial commit - Kronos store"
git branch -M main
git remote add origin https://github.com/seu-usuario/kronos-store.git
git push -u origin main
```

### 3. Deploy na Vercel

**Opção A: Direto pela Vercel (Recomendado)**

1. Acesse https://vercel.com/new
2. Selecione "Importar Projeto Existente"
3. Cole: `https://github.com/seu-usuario/kronos-store.git`
4. Clique em "Importar"
5. Em "Environment Variables", adicione:
   ```
   VITE_SUPABASE_URL = https://seu-projeto.supabase.co
   VITE_SUPABASE_ANON_KEY = sua-chave-anonima-aqui
   ```
6. Clique "Deploy"
7. Pronto! ✅

**Opção B: Usando Vercel CLI**

```bash
# 1. Instale Vercel CLI
npm i -g vercel

# 2. Faça login
vercel login

# 3. Deploy
vercel

# 4. Escolha as opções (ou use defaults)
# 5. Será perguntado sobre variáveis de ambiente
```

---

## 📋 Checklist Pre-Deploy

- [ ] Supabase criado
- [ ] Tabela 'orders' criada (execute SQL)
- [ ] SUPABASE_URL copiado
- [ ] SUPABASE_ANON_KEY copiado
- [ ] GitHub repositório criado
- [ ] Código feito push para GitHub
- [ ] Vercel configurado
- [ ] Variáveis de ambiente adicionadas

---

## 🔍 Verificar Deploy

Após deploy:

1. **Acesse sua URL da Vercel** (ex: kronos-store.vercel.app)
2. **Teste o site:**
   - Veja produtos
   - Tente fazer login (criar conta no Supabase primeiro)
   - Adicione ao carrinho
   - Faça uma compra teste
3. **Verifique console** (F12) para erros
4. **Teste "Meus Pedidos"** após compra

---

## 🔧 Variáveis de Ambiente

### Para Desenvolvimento Local

Crie arquivo `.env.local`:

```
VITE_SUPABASE_URL=https://seu-projeto.supabase.co
VITE_SUPABASE_ANON_KEY=sua-chave-anonima
```

### Para Vercel (Production)

Adicione em Vercel Dashboard:
- Settings → Environment Variables

---

## 📊 Domínio Customizado

1. Em Vercel: Settings → Domains
2. Adicione seu domínio (ex: kronos.com.br)
3. Configure DNS no seu provedor
4. Espere propagação (até 24h)

---

## 🔒 SSL/HTTPS

✅ **Automático na Vercel!**
- Vercel fornece SSL grátis
- Renovação automática
- Sem custo extra

---

## 📈 Monitoramento

**Vercel Dashboard:**
- Deployments → Ver histórico
- Analytics → Performance
- Functions → Logs

---

## 🆘 Troubleshooting

### Erro: "SUPABASE_URL não definido"

```bash
# Solução:
# 1. Verifique se adicionou variáveis em Vercel Settings
# 2. Redeploy: git push (ativa novo deploy automático)
# 3. Aguarde 2-3 minutos
```

### Erro: "Falha ao conectar Supabase"

```bash
# Solução:
# 1. Confira SUPABASE_URL está correto
# 2. Confira SUPABASE_ANON_KEY está correto
# 3. Verifique se tabela 'orders' existe no Supabase
# 4. Confira RLS está configurado
```

### Site carrega lento

```bash
# Vercel é rápido por padrão
# Se estiver lento:
# 1. Limpe cache: Ctrl+Shift+Del
# 2. Aguarde propagação CDN (5min)
# 3. Verifique conexão de internet
```

---

## 📱 Teste Mobile

```bash
# Seu site estará em:
https://kronos-store.vercel.app

# Teste em celular:
# 1. Acesse em navegador do celular
# 2. Funciona perfeitamente (responsivo)
# 3. Pode até fazer compra no celular!
```

---

## 🎯 Próximos Passos

1. ✅ Crie conta cliente real no Supabase (teste login)
2. ✅ Faça compra de teste
3. ✅ Veja pedido em "Meus Pedidos"
4. ✅ Compartilhe URL com amigos
5. ✅ Receba feedback

---

## 📊 Estatísticas

Vercel oferece:
- **Build Time**: < 1min
- **Uptime**: 99.9%+
- **Speed Index**: < 2s
- **CDN Global**: 200+ pontos

---

## 💰 Custos

- **Vercel**: Grátis (para sites estáticos)
- **Supabase**: Grátis (até limites generosos)
- **Domínio**: ~R$ 40-100/ano (opcional)

**Total: Pode ser completamente grátis!**

---

## ✨ Você está pronto!

Siga os 3 passos acima e seu site estará online em minutos.

**Dúvidas?** Leia README.md ou INSTRUCOES_PEDIDOS.txt

🚀 Boa sorte!
