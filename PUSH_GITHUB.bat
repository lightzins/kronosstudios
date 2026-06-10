@echo off
REM Script para fazer push do projeto para GitHub
REM Use: Abra este arquivo e ele fará tudo automaticamente

echo ========================================
echo KRONOS STORE - PUSH GITHUB
echo ========================================
echo.

REM Inicializar Git
echo [1/6] Inicializando Git...
git init

REM Adicionar todos os arquivos
echo [2/6] Adicionando arquivos...
git add .

REM Fazer commit inicial
echo [3/6] Fazendo commit...
git commit -m "Initial commit - Kronos Store E-commerce"

REM Renomear branch para main
echo [4/6] Configurando branch main...
git branch -M main

REM Adicionar remote
echo [5/6] Adicionando remote GitHub...
git remote add origin https://github.com/lightzins/kronosstudios.git

REM Fazer push
echo [6/6] Fazendo push para GitHub...
git push -u origin main

echo.
echo ========================================
echo SUCESSO! Projeto enviado para GitHub!
echo ========================================
echo.
echo URL do seu repositorio:
echo https://github.com/lightzins/kronosstudios
echo.
echo Proximo passo: Deploy na Vercel
echo Acesse: https://vercel.com/new
echo.
pause
