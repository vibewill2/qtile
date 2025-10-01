# Theme configuration for Qtile
# Dracula color scheme

colors = {
    # Main colors com transparência
    "bg": "#282a36cc",         # Background (80% opacidade)
    "bg_solid": "#282a36",     # Background sólido para widgets
    "fg": "#f8f8f2",           # Foreground
    "selection": "#44475a",    # Selection/highlight
    "comment": "#6272a4",      # Comments/inactive
    
    # Accent colors com leve transparência
    "red": "#ff5555dd",        # Errors/warnings (87% opacidade)
    "orange": "#ffb86cdd",     # Music/media (87% opacidade)
    "yellow": "#f1fa8cdd",     # Keyboard/input (87% opacidade)
    "green": "#50fa7bdd",      # Network/success (87% opacidade)
    "purple": "#bd93f9dd",     # Layout/primary (87% opacidade)
    "cyan": "#8be9fddd",       # CPU/system (87% opacidade)
    "pink": "#ff79c6dd",       # Volume/audio (87% opacidade)
}

# Font settings
font_config = {
    "font": "JetBrainsMono Nerd Font",
    "fontsize": 13,
    "icon_fontsize": 16,
    "powerline_fontsize": 18,
}

# Bar configuration
bar_config = {
    "height": 32,
    "background": colors["bg"],
    "border_width": [0, 0, 0, 0],  # Remove bordas para cantos arredondados
    "border_color": colors["purple"],
    "margin": [4, 8, 4, 8],  # Margem para criar efeito flutuante
}

# Widget configuration
widget_config = {
    "padding": 8,
    "separator_padding": 6,
    "max_window_name_chars": 50,
    "network_update_interval": 1.0,
    "cpu_update_interval": 1.0,
    "memory_update_interval": 1.0,
    "rounded_size": 12,  # Tamanho do arredondamento
    "widget_margin": 2,   # Margem entre widgets
}
