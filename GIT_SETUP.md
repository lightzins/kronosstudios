# 🔧 Setup Git & GitHub

## ⚡ Configuração Rápida

### 1. Instalar Git

**Windows:**
```bash
# Baixe de https://git-scm.com/download/win
# Instale com as opções padrão
```

**Verificar instalação:**
```bash
git --version
```

### 2. Configurar Git (primeira vez)

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@gmail.com"

# Verificar configuração
git config --global --list
```

### 3. Criar Repositório no GitHub

1. Acesse https://github.com/new
2. **Repository name:** `kronos-store`
3. **Description:** "E-commerce Kronos - Vestuário Premium"
4. **Public** (deixe visível)
5. **Clique:** "Create repository"

### 4. Fazer Push do Código

Abra o terminal na pasta do projeto:

```bash
cd "C:\Users\Admin\Desktop\kronos store"

# Inicializar Git
git init

# Adicionar todos os arquivos
git add .

# Fazer commit
git commit -m "Initial commit - Kronos store"

# Renomear branch para main
git branch -M main

# Adicionar remote (copie a URL do GitHub)
git remote add origin https://github.com/SEU-USUARIO/kronos-store.git

# Fazer push (primeira vez)
git push -u origin main

# Próximos pushes (mais rápido)
git push
```

---

## 📋 Comandos Úteis

### Ver status
```bash
git status
```

### Ver histórico
```bash
git log --oneline
```

### Fazer mudanças e push
```bash
git add .
git commit -m "Descrição das mudanças"
git push
```

### Criar branch
```bash
git checkout -b nova-feature
git push -u origin nova-feature
```

### Descartar mudanças
```bash
git checkout -- arquivo.txt
```

### Ver diferenças
```bash
git diff
```

---

## ✨ Workflow Recomendado

```
1. Modifique arquivos
   ↓
2. git status (verificar o que mudou)
   ↓
3. git add . (adicionar mudanças)
   ↓
4. git commit -m "Mensagem clara" (fazer commit)
   ↓
5. git push (enviar para GitHub)
   ↓
6. Vercel detecta e faz deploy automático! 🚀
```

---

## 🔐 Segurança

### Adicione .env ao .gitignore (IMPORTANTE!)

O arquivo `.env` **NUNCA** deve ser feito push.

Nosso `.gitignore` já contém:
```
.env
.env.local
.env.*.local
```

### Verificar antes de push

```bash
# Verificar o que vai ser enviado
git status

# Certifique-se que .env NÃO aparece na lista!
```

---

## 🆘 Problemas Comuns

### "Permission denied (publickey)"

**Solução:** Configure SSH Key do GitHub

```bash
# 1. Gerar chave
ssh-keygen -t ed25519 -C "seu-email@gmail.com"

# 2. Copiar chave pública
cat ~/.ssh/id_ed25519.pub

# 3. No GitHub: Settings → SSH Keys → Add key
# 4. Cole a chave e salve

# 5. Testar conexão
ssh -T git@github.com
```

### "fatal: remote origin already exists"

```bash
# Remover remote anterior
git remote remove origin

# Adicionar novamente
git remote add origin https://seu-repo.git
```

### "Your branch is ahead of 'origin/main'"

```bash
# Fazer push das mudanças
git push
```

---

## 📊 Após Setup

1. ✅ Git configurado
2. ✅ Repositório GitHub criado
3. ✅ Código feito push
4. ✅ Vercel conectado ao GitHub
5. ✅ Pronto para deploy automático!

---

## 🚀 Deploy Automático

Após configurar Vercel no GitHub:

1. Faça mudanças no código
2. `git push`
3. **Vercel detecta automaticamente** ✨
4. **Faz novo deploy** 🚀
5. Seu site atualiza sozinho!

---

## 📝 Boas Práticas

### Mensagens de commit clara

```bash
# ✅ BOM
git commit -m "Add order history to user dashboard"

# ❌ RUIM
git commit -m "fix"
```

### Commit frequente

```bash
# Melhor fazer vários commits pequenos
git commit -m "Fix checkout form validation"
git commit -m "Add loading spinner to orders"
git commit -m "Update colors to new branding"

# Do que um gigante
git commit -m "Fixed everything"
```

### Sempre pull antes de push

```bash
git pull
git add .
git commit -m "..."
git push
```

---

## 🎯 Próximos Passos

1. ✅ Rode: `git init`
2. ✅ Rode: `git add .`
3. ✅ Rode: `git commit -m "Initial commit"`
4. ✅ Rode: `git push -u origin main`
5. ✅ Vercel faz deploy automático!

---

**Pronto! Agora seu código está versionado e seu site deploiado automaticamente!** 🎉
