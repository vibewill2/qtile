#!/usr/bin/env python3
import os
import sys
import subprocess

FIFO_PATH = '/tmp/cava.fifo'
START_SCRIPT = os.path.expanduser('~/.config/qtile/start_cava.sh')

def ensure_cava_running():
    """Garante que o Cava está rodando"""
    # Verifica se o FIFO existe
    if not os.path.exists(FIFO_PATH):
        subprocess.run([START_SCRIPT], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return
    
    # Verifica se o processo do cava está rodando
    try:
        result = subprocess.run(['pgrep', '-f', 'cava -p.*cava_config'], 
                              capture_output=True, text=True, timeout=1)
        if not result.stdout.strip():
            subprocess.run([START_SCRIPT], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        pass

def get_cava_output():
    """Lê dados do FIFO e formata para a barra"""
    try:
        ensure_cava_running()
        
        # Abre o FIFO em modo não-bloqueante para leitura
        if os.path.exists(FIFO_PATH):
            # Lê uma linha do FIFO com timeout
            with open(FIFO_PATH, 'r', opener=lambda path, flags: os.open(path, flags | os.O_NONBLOCK)) as fifo:
                try:
                    line = fifo.readline().strip()
                    if line:
                        # Converte números em barras visuais
                        bar_chars = '▁▂▃▄▅▆▇█'
                        bars = []
                        
                        for char in line[:10]:  # Limita a 10 caracteres
                            if char.isdigit():
                                level = int(char)
                                if level < len(bar_chars):
                                    bars.append(bar_chars[level])
                                else:
                                    bars.append(bar_chars[-1])
                        
                        return ''.join(bars) if bars else '▁' * 10
                except:
                    pass
        
        return '▁' * 10
            
    except Exception:
        return '▁' * 10

if __name__ == '__main__':
    print(get_cava_output())
