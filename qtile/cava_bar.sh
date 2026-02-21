#!/bin/bash

# Configuração do Cava para output em modo raw
# Este script captura a saída do cava e formata para a barra

# Verifica se já existe uma instância do cava rodando
if pgrep -x "cava" > /dev/null; then
    pkill -x "cava"
fi

# Roda o cava com configuração para output raw
cava -p /home/vibewill/.config/qtile/cava_config | while read -r line; do
    # Limita o tamanho da saída para a barra
    echo "$line" | cut -c1-20
done
