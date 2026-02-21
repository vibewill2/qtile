#!/bin/bash

# Mata instâncias anteriores do cava
pkill -f "cava -p.*cava_config"

# Cria FIFO se não existir
[ ! -p /tmp/cava.fifo ] && mkfifo /tmp/cava.fifo

# Inicia o cava completamente desanexado do terminal
nohup cava -p ~/.config/qtile/cava_config > /dev/null 2>&1 &
disown

# Salva o PID
echo $! > /tmp/cava_qtile.pid 2>/dev/null || true
