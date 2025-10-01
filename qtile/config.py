

from typing import List  # noqa: F401
import os
import subprocess

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook

# Tentar importar decorações (pode não estar disponível em todas as versões)
try:
    from libqtile.widget.decorations import RectDecoration
    DECORATIONS_AVAILABLE = True
except ImportError:
    DECORATIONS_AVAILABLE = False

# Import theme configuration
from theme import colors, font_config, bar_config, widget_config

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.nett(),
    Key([mod, "control"], "r", lazy.reload_config()),

        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    
    # Meus apps
    Key([mod],  "g"    , lazy.spawn("google-chrome"), desc="Navegador"),
    Key([mod],  "d"    , lazy.spawn("rofi -show drun"), desc="Menu"),
    Key([mod],  "f"    , lazy.spawn("thunar"), desc="Arquivos"),
    Key([mod], "p"     , lazy.spawn("waypaper")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
]

groups = [ Group(str(i)) for i in (1, 2, 3, 4, 5, 6, 7, 8, 9)]





for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.Tile(margin = 15),
    layout.Columns(border_focus_stack='#d75f5f',
        margin = 2,
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    layout.Stack(num_stacks=2),
    layout.Bsp(margin = 2),
    layout.Matrix(margin = 2),
    layout.MonadTall(margin = 2),
    layout.MonadWide(margin = 2),
    layout.RatioTile(margin = 2),
    layout.TreeTab(),
    layout.VerticalTile(margin = 2),
    layout.Zoomy(),
]

widget_defaults = dict(
    font=font_config["font"],
    fontsize=font_config["fontsize"],
    padding=3,
    background=colors["bg"],
)
extension_defaults = widget_defaults.copy()

# Função para criar separador visual
def create_separator(color=colors["selection"], size=2):
    return widget.Sep(
        linewidth=0,
        padding=6,
        foreground=color,
        background=colors["bg"]
    )

# Função para criar widget com background transparente
def create_transparent_widget(widget_obj, bg_color, fg_color="#000000"):
    widget_obj.background = bg_color
    widget_obj.foreground = fg_color
    return widget_obj

# Função para criar widget com estilo arredondado
def create_rounded_widget(widget_class, bg_color, fg_color="#000000", **kwargs):
    """Cria widget com bordas arredondadas"""
    if DECORATIONS_AVAILABLE:
        # Usar decorações se disponível
        default_kwargs = {
            'background': colors["bg"],
            'foreground': fg_color,
            'padding': 0,
            'decorations': [
                RectDecoration(
                    colour=bg_color,
                    radius=widget_config["rounded_size"],
                    filled=True,
                    padding_y=4,
                    padding_x=widget_config["padding"],
                )
            ],
        }
    else:
        # Fallback para estilo PowerLine
        default_kwargs = {
            'background': bg_color,
            'foreground': fg_color,
            'padding': widget_config["padding"],
        }
    
    default_kwargs.update(kwargs)
    return widget_class(**default_kwargs)

# Função para criar widgets em estilo PowerLine (alternativa aos arredondados)
def create_powerline_widget(widget_class, bg_color, fg_color="#000000", **kwargs):
    """Cria uma sequência de widgets com estilo PowerLine"""
    widgets = []
    
    # Separador inicial (arredondado visual)
    widgets.append(
        widget.TextBox(
            text="",  # Powerline left rounded
            background=colors["bg"],
            foreground=bg_color,
            fontsize=20,
            padding=0
        )
    )
    
    # Widget principal
    default_kwargs = {
        'background': bg_color,
        'foreground': fg_color,
        'padding': widget_config["padding"],
    }
    default_kwargs.update(kwargs)
    widgets.append(widget_class(**default_kwargs))
    
    # Separador final (arredondado visual)
    widgets.append(
        widget.TextBox(
            text="",  # Powerline right rounded
            background=colors["bg"],
            foreground=bg_color,
            fontsize=20,
            padding=0
        )
    )
    
    return widgets

# Função para criar espaçamento entre widgets arredondados
def create_widget_spacer(size=6):
    """Cria um espaçamento entre widgets"""
    return widget.Spacer(
        length=size,
        background=colors["bg"]
    )

# Função para criar widget com background colorido
def create_powerline_widget(widget_obj, bg_color, fg_color=colors["bg"]):
    widget_obj.background = bg_color
    widget_obj.foreground = fg_color
    return widget_obj

screens = [
    Screen(
        top=bar.Bar(
            [
                # Seção de layout e grupos (lado esquerdo)
                widget.TextBox(
                    text="",
                    background=colors["bg"],
                    padding=4
                ),
                
                widget.CurrentLayout(
                    background=colors["purple"],
                    foreground="#000000",
                    fmt="  {}",
                    padding=12
                ),
                
                widget.TextBox(
                    text="",
                    background=colors["bg"],
                    padding=4
                ),

                create_widget_spacer(12),

                widget.GroupBox(
                    background=colors["bg"],
                    foreground=colors["fg"],
                    active=colors["cyan"],
                    inactive=colors["comment"],
                    highlight_method="block",
                    this_current_screen_border=colors["purple"],
                    this_screen_border=colors["selection"],
                    other_current_screen_border=colors["pink"],
                    other_screen_border=colors["selection"],
                    urgent_border=colors["red"],
                    rounded=True,
                    padding_x=8,
                    padding_y=6,
                    borderwidth=2,
                    fontsize=12
                ),

                create_separator(),

                # Nome da janela ativa
                widget.WindowName(
                    background=colors["bg"],
                    foreground=colors["green"],
                    format="{name}",
                    max_chars=50,
                    padding=8
                ),

                # Spacer para empurrar widgets para direita
                widget.Spacer(
                    background=colors["bg"]
                ),

                # Seção de informações do sistema (lado direito)
                
                # Música (Cmus)
                create_rounded_widget(
                    widget.Cmus,
                    colors["orange"],
                    "#000000",
                    format="♫ {artist} - {title}",
                    max_chars=30,
                    play_color="#000000",
                    noplay_color="#000000"
                ),

                create_widget_spacer(8),

                # Teclado
                create_rounded_widget(
                    widget.KeyboardLayout,
                    colors["yellow"],
                    "#000000",
                    configured_keyboards=['br', 'us'],
                    fmt=" {}"
                ),

                create_widget_spacer(8),

                # Rede
                create_rounded_widget(
                    widget.Net,
                    colors["green"],
                    "#000000",
                    format=" {down} ↓↑ {up}",
                    update_interval=1.0
                ),

                create_widget_spacer(8),

                # Memória
                create_rounded_widget(
                    widget.Memory,
                    colors["red"],
                    "#000000",
                    format=" {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}",
                    update_interval=1.0
                ),

                create_widget_spacer(8),

                # CPU
                widget.TextBox(
                    text="",
                    background=colors["bg"],
                    padding=4
                ),
                
                widget.CPU(
                    background=colors["cyan"],
                    foreground="#000000",
                    format=" {load_percent}%",
                    update_interval=1.0,
                    padding=12
                ),
                
                widget.TextBox(
                    text="",
                    background=colors["bg"],
                    padding=4
                ),

                create_widget_spacer(8),

                # Volume
                create_rounded_widget(
                    widget.Volume,
                    colors["pink"],
                    "#000000",
                    fmt="♪ {}",
                    step=5
                ),

                create_widget_spacer(8),

                # Clock
                widget.TextBox(
                    text="",
                    background=colors["bg"],
                    padding=4
                ),
                
                widget.Clock(
                    background=colors["purple"],
                    foreground="#000000",
                    format=" %d/%m %H:%M",
                    padding=12
                ),
                
                widget.TextBox(
                    text="",
                    background=colors["bg"],
                    padding=4
                ),

                # Systray
                widget.Systray(
                    background=colors["bg"],
                    padding=8
                ),

                create_separator(size=8),
            ],
            bar_config["height"],
            background=bar_config["background"],
            border_width=bar_config["border_width"],
            border_color=bar_config["border_color"],
            margin=bar_config["margin"]
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# Start com linux
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])

wmname = "qtile"
