# -*- coding: utf-8 -*-
import base64
from PIL import Image

src = Image.open(r"C:\Users\Admin\Downloads\OWN.jpg").convert("RGB")
w, h = src.size
print(f"Original: {w}x{h}")

# A imagem tem 2400px de largura com duas blusas lado a lado
# Frente ocupa aprox x=0 a x=1100, verso de x=1300 a x=2400
# Tem um gap/espaco branco no meio (~x=1100 a x=1300)
# Vamos encontrar o ponto de divisao escaneando pixels brancos no centro vertical

mid_y = h // 2
# Escanear coluna por coluna no meio vertical procurando regiao mais clara (fundo branco)
pixels = []
for x in range(900, 1500):
    r, g, b = src.getpixel((x, mid_y))
    brightness = (r + g + b) / 3
    pixels.append((x, brightness))

# Achar o ponto mais brilhante (mais branco = gap entre as duas blusas)
split_x = max(pixels, key=lambda p: p[1])[0]
print(f"Ponto de divisao detectado: x={split_x}")

# Recortar com margem para centralizar cada blusa
# Frente: do inicio ate o split, centrada
frente = src.crop((0, 0, split_x, h))
# Verso: do split ate o fim
verso  = src.crop((split_x, 0, w, h))

print(f"Frente: {frente.size} | Verso: {verso.size}")

frente.save(r"C:\Users\Admin\Desktop\kronos store\sf.jpg", "JPEG", quality=97)
verso.save(r"C:\Users\Admin\Desktop\kronos store\sv.jpg", "JPEG", quality=97)
src.close()

with open(r"C:\Users\Admin\Desktop\kronos store\sf.jpg", "rb") as f:
    b64F = "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()
with open(r"C:\Users\Admin\Desktop\kronos store\sv.jpg", "rb") as f:
    b64V = "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()

print(f"b64 F: {len(b64F)} | V: {len(b64V)} | Iguais: {b64F == b64V}")

with open(r"C:\Users\Admin\Desktop\kronos store\index.html", "r", encoding="utf-8") as f:
    html = f.read()

start = html.index("            // Casacos")
end   = html.index("            // Camisas", start)

before = html[:start]
after  = html[end:]

new_block = (
    "            // Casacos\n"
    "            {\n"
    "                id: 4,\n"
    '                name: "Alexandre O Grande Su\u00e9ter",\n'
    "                price: 279.90,\n"
    '                category: "casacos",\n'
    '                imageFront: "' + b64F + '",\n'
    '                imageBack:  "' + b64V + '",\n'
    '                sizes: ["P", "M", "G", "GG"]\n'
    "            },\n"
)

html = before + new_block + after

with open(r"C:\Users\Admin\Desktop\kronos store\index.html", "w", encoding="utf-8") as f:
    f.write(html)

import os
os.remove(r"C:\Users\Admin\Desktop\kronos store\sf.jpg")
os.remove(r"C:\Users\Admin\Desktop\kronos store\sv.jpg")
print("Feito!")
