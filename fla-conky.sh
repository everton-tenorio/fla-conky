#!/bin/bash

cd /home/.../fla-conky/
source venv/bin/activate

echo "# Executando scripts..."
python fla-jogos.py
python flamengo-carioca.py

deactivate
