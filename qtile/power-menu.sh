#!/bin/bash

# Power Menu para Qtile
# Opções de energia disponíveis

if [ "$1" = "menu" ]; then
    # Mostrar menu usando dmenu ou rofi
    options="🔒 Bloquear\n🏠 Logout\n💤 Suspender\n🔄 Reiniciar\n⚡ Desligar\n❌ Cancelar"
    
    # Tentar rofi primeiro, depois dmenu
    if command -v rofi >/dev/null 2>&1; then
        choice=$(echo -e "$options" | rofi -dmenu -i -p "Ação: " -theme-str 'window {width: 200px;}' -lines 6)
    elif command -v dmenu >/dev/null 2>&1; then
        choice=$(echo -e "$options" | dmenu -p "Ação: ")
    else
        # Fallback: usar zenity se disponível
        if command -v zenity >/dev/null 2>&1; then
            choice=$(zenity --list --title="Menu de Energia" --text="Escolha uma ação:" \
                --column="Ação" "🔒 Bloquear" "🏠 Logout" "💤 Suspender" "🔄 Reiniciar" "⚡ Desligar" "❌ Cancelar")
        else
            notify-send "Erro" "Nenhum menu disponível (rofi, dmenu, zenity)"
            exit 1
        fi
    fi
    
    # Executar a ação escolhida
    if [ -n "$choice" ]; then
        "$0" "$choice"
    fi
    exit 0
fi

if [ "$1" = "power-menu" ]; then
    echo "🔒 Bloquear"
    echo "🏠 Logout"
    echo "💤 Suspender"
    echo "🔄 Reiniciar"
    echo "⚡ Desligar"
    echo "❌ Cancelar"
    exit 0
fi

case "$1" in
    "🔒 Bloquear")
        # Comando para bloquear a tela
        swaylock --color 000000 --inside-color 1e1e1e --ring-color 333333 --key-hl-color 00ff00 --text-color ffffff || \
        i3lock -c 000000 || \
        loginctl lock-session
        ;;
    "🏠 Logout")
        # Logout do Qtile
        qtile cmd-obj -o cmd -f shutdown
        ;;
    "💤 Suspender")
        # Suspender o sistema
        systemctl suspend
        ;;
    "🔄 Reiniciar")
        # Confirmar antes de reiniciar
        if command -v zenity >/dev/null 2>&1; then
            zenity --question --title="Confirmação" --text="Tem certeza que deseja reiniciar o sistema?" && systemctl reboot
        elif command -v rofi >/dev/null 2>&1; then
            choice=$(echo -e "Sim\nNão" | rofi -dmenu -p "Reiniciar sistema? ")
            [ "$choice" = "Sim" ] && systemctl reboot
        else
            systemctl reboot
        fi
        ;;
    "⚡ Desligar")
        # Confirmar antes de desligar
        if command -v zenity >/dev/null 2>&1; then
            zenity --question --title="Confirmação" --text="Tem certeza que deseja desligar o sistema?" && systemctl poweroff
        elif command -v rofi >/dev/null 2>&1; then
            choice=$(echo -e "Sim\nNão" | rofi -dmenu -p "Desligar sistema? ")
            [ "$choice" = "Sim" ] && systemctl poweroff
        else
            systemctl poweroff
        fi
        ;;
    "❌ Cancelar")
        # Não fazer nada
        exit 0
        ;;
    *)
        exit 1
        ;;
esac