#!/bin/bash
picom --config ~/.config/picom/picom.conf &
dunst &
xset s noblank &
xset s off &
xset -dpms &
~/.fehbg &
swww-daemon &
~/.config/qtile/start_cava.sh &
