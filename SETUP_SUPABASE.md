# 📦 Setup do Sistema de Pedidos - Supabase

## O que foi implementado:

Agora o sistema está **100% real**! Os pedidos são salvos no banco de dados Supabase quando o usuário completa a compra.

### Como funciona:

1. ✅ Usuário faz login
2. ✅ Adiciona itens ao carrinho
3. ✅ Finaliza o checkout
4. ✅ Pedido é salvo no Supabase com dados reais
5. ✅ Ao abrir "Meus Pedidos", carrega os pedidos do banco de dados

---

## 🔧 Configuração necessária no Supabase:

### 1. Criar a Tabela `orders`

No painel do Supabase, vá para **SQL Editor** e execute este comando:

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

-- Criar índice para buscar pedidos por usuário
CREATE INDEX idx_orders_user_id ON orders(user_id);
```

### 2. Configurar Row Level Security (RLS)

Para que cada usuário veja apenas seus próprios pedidos, adicione as políticas:

```sql
-- Ativar RLS
ALTER TABLE orders ENABLE ROW LEVEL SECURITY;

-- Usuários podem ver apenas seus próprios pedidos
CREATE POLICY "Users can view their own orders"
  ON orders FOR SELECT
  USING (auth.uid() = user_id);

-- Usuários podem inserir seus próprios pedidos
CREATE POLICY "Users can insert their own orders"
  ON orders FOR INSERT
  WITH CHECK (auth.uid() = user_id);

-- (Opcional) Admins podem ver todos os pedidos
CREATE POLICY "Admins can view all orders"
  ON orders FOR SELECT
  USING (auth.jwt() ->> 'is_admin' = 'true');
```

---

## 📝 Estrutura da Tabela:

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `id` | BIGINT | ID único do pedido |
| `user_id` | UUID | ID do usuário que fez o pedido |
| `product_name` | TEXT | Nome do produto (ex: "Alexandre O Grande — Moletom") |
| `size` | VARCHAR(10) | Tamanho (P, M, G, GG) |
| `price` | DECIMAL(10,2) | Preço unitário |
| `quantity` | INT | Quantidade |
| `order_date` | TIMESTAMP | Data do pedido |
| `status` | VARCHAR(50) | Processando / Em trânsito / Entregue |
| `payment_method` | VARCHAR(50) | pix / debito / credito |
| `customer_name` | TEXT | Nome do cliente |
| `customer_email` | TEXT | Email do cliente |
| `customer_phone` | TEXT | Telefone (opcional) |
| `created_at` | TIMESTAMP | Data de criação |

---

## 🧪 Como Testar:

1. **Configure a tabela** (copie o SQL acima no Supabase SQL Editor)
2. **Faça login** no seu site
3. **Adicione um produto ao carrinho**
4. **Complete o checkout**
5. **Abra "Meus Pedidos"** (clique no avatar)
6. **Veja seu pedido aparecer na lista!** ✅

---

## 🐛 Debugging:

Se os pedidos não aparecerem:

1. Abra o **Console do navegador (F12)**
2. Procure por estas mensagens:
   - ✅ "Pedidos carregados: 1" → Funcionando!
   - ⚠️ "Nenhum pedido encontrado" → Verifique se salvou a tabela
   - ❌ "Erro ao buscar pedidos" → Problema de RLS ou permissões

3. **Verifique no Supabase:**
   - Vá para **Table Editor** → `orders`
   - Procure pelos seus pedidos salvos
   - Verifique se o `user_id` está correto

---

## 📊 Próximas Melhorias (Opcional):

- [ ] Adicionar histórico de status (Processando → Em trânsito → Entregue)
- [ ] Enviar email de confirmação do pedido
- [ ] Dashboard admin para gerenciar pedidos
- [ ] Rastreamento em tempo real
- [ ] Integração com transportadoras (Sedex, etc)

---

## 📞 Suporte:

Se tiver dúvidas:
1. Verifique os logs do console (F12)
2. Consulte a documentação do Supabase: https://supabase.com/docs
3. Verifique se as credenciais do Supabase estão corretas no HTML

**Pronto! Sistema real funcionando! 🎉**
