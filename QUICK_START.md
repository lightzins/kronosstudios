# ⚡ Quick Start - Do Zero ao Deploy em 30 Minutos

Siga este guia e seu e-commerce estará online!

---

## 🎯 Passo 1: Supabase (10 min)

### 1.1 Criar Conta Supabase

1. Vá para https://supabase.com
2. Clique "Sign Up"
3. Use Google/GitHub ou email
4. Verifique seu email

### 1.2 Criar Projeto

1. Clique "New Project"
2. **Name:** `kronos`
3. **Database Password:** Salve em local seguro
4. **Region:** Escolha próximo a você (Brazil = São Paulo)
5. Clique "Create new project"
6. **Aguarde 2-3 minutos** até ficar pronto

### 1.3 Configurar Banco de Dados

1. Vá para **SQL Editor** (esquerda)
2. Clique **"New Query"**
3. Cole todo o SQL do arquivo: **SETUP_SUPABASE.md**
4. Clique **"Run"** (ícone play)
5. Pronto! ✅ Tabela criada

### 1.4 Copiar Credenciais

1. Vá para **Settings** → **API**
2. Copie:
   - **Project URL** → `VITE_SUPABASE_URL`
   - **Anon Key** → `VITE_SUPABASE_ANON_KEY`

**Guarde estas credenciais!** Você vai precisar.

---

## 🔧 Passo 2: GitHub (5 min)

### 2.1 Criar Repositório

1. Vá para https://github.com/new
2. **Repository name:** `kronos-store`
3. **Description:** E-commerce Kronos
4. **Public** (deixe marcado)
5. Clique **"Create repository"**

### 2.2 Fazer Push do Código

Abra um terminal/PowerShell na pasta do projeto:

```powershell
cd "C:\Users\Admin\Desktop\kronos store"

# Inicializar
git init
git add .
git commit -m "Initial commit"
git branch -M main

# Copie a URL do GitHub e rode:
git remote add origin https://github.com/SEU-USUARIO/kronos-store.git
git push -u origin main
```

**Pronto!** Seu código está no GitHub.

---

## 🚀 Passo 3: Vercel (5 min)

### 3.1 Conectar e Deploy

1. Vá para https://vercel.com
2. Clique **"Sign Up"**
3. Escolha "GitHub"
4. Autorize Vercel
5. Clique **"Add New Project"**
6. **Selecione:** `kronos-store`
7. Clique **"Import"**

### 3.2 Adicionar Variáveis de Ambiente

Na página de configuração:

1. Clique **"Environment Variables"**
2. Adicione:

| Variable | Value |
|----------|-------|
| VITE_SUPABASE_URL | (copie do passo 1.4) |
| VITE_SUPABASE_ANON_KEY | (copie do passo 1.4) |

3. Clique **"Deploy"**

**Aguarde 2-3 minutos...**

### 3.3 Seu Site Está Online! 🎉

Você verá uma URL como:
```
https://kronos-store.vercel.app
```

---

## ✅ Testar o Site

1. Acesse sua URL da Vercel
2. **Criar conta:**
   - Clique perfil
   - "Não tenho conta"
   - Preencha dados
   - Clique "Criar Conta"
3. **Verificar email:** Confirme em seu email
4. **Fazer login novamente**
5. **Comprar:**
   - Adicione um produto
   - Clique "Finalizar Compra"
   - Preencha dados
   - Confirme pagamento
6. **Ver pedido:**
   - Clique perfil
   - Veja em "Meus Pedidos"
   - ✅ Pedido apareceu!

---

## 📊 Resumo do que você fez

| Serviço | O quê | Custo |
|---------|-------|-------|
| **Supabase** | Banco de dados | Grátis |
| **GitHub** | Versionamento | Grátis |
| **Vercel** | Hosting | Grátis |
| **Seu Site** | E-commerce | **Grátis!** |

---

## 🎯 Próximas Melhorias (Opcional)

- [ ] Adicionar seu domínio customizado
- [ ] Implementar email de confirmação
- [ ] Dashboard admin
- [ ] Integração com gateway de pagamento
- [ ] Analytics e tracking
- [ ] Sistema de pontos/fidelidade

---

## 📞 Algo Deu Errado?

### Erro: "Site não carrega"
```
1. Abra console (F12)
2. Veja se há erro relacionado a Supabase
3. Verifique variáveis em Vercel Settings
4. Fça novo deploy: git push
```

### Erro: "Login não funciona"
```
1. Confira SUPABASE_URL está correto
2. Confira SUPABASE_ANON_KEY está correto
3. Verifique se Supabase Auth está ativado
```

### Erro: "Pedidos não salvam"
```
1. Verifique se tabela 'orders' foi criada
2. Confira RLS está configurado
3. Veja console do navegador (F12)
```

---

## 📚 Para Aprender Mais

| Tópico | Arquivo |
|--------|---------|
| **Deploy** | DEPLOY_VERCEL.md |
| **Supabase** | SETUP_SUPABASE.md |
| **Git** | GIT_SETUP.md |
| **Pedidos** | INSTRUCOES_PEDIDOS.txt |
| **Geral** | README.md |

---

## 🎉 Parabéns!

Seu e-commerce Kronos está online e pronto para vender!

**Próximos passos:**
1. Divulgue seu site
2. Configure domínio customizado (opcional)
3. Monitore pedidos
4. Implemente melhorias

---

**Qualquer dúvida, consulte os guias específicos ou a documentação no README.md**

🚀 Sucesso!
