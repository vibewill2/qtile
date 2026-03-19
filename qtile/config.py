from typing import List  # noqa: F401
import os
import subprocess

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook

# Import theme configuration
from theme import colors, font_config, bar_config, widget_config

mod = "mod4"
terminal = guess_terminal()

# --- Atalhos de Teclado ---
keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "control"], "r", lazy.reload_config()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "b", lazy.function(lambda qtile: trocar_wallpaper())),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn(terminal)),
    
    Key([mod], "g", lazy.spawn("vivaldi")),
    Key([mod], "d", lazy.spawn("rofi -show drun")),
    Key([mod], "f", lazy.spawn("nemo")),
    Key([mod], "p", lazy.spawn("/home/vibewill/.config/waypaper/run_selector.sh")),
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
]

groups = [Group(str(i)) for i in (1, 2, 3, 4, 5, 6, 7, 8, 9)]
for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)),
    ])

layouts = [
    layout.Columns(border_focus=colors["purple"], margin=12, border_width=2),
    layout.Max(),
    layout.MonadTall(margin=12, border_focus=colors["purple"]),
]

widget_defaults = dict(
    font=font_config["font"],
    fontsize=font_config["fontsize"],
    padding=3,
    background=colors["bg"],
)
extension_defaults = widget_defaults.copy()

# --- Powerline ---
def get_powerline(direction='left', fg=colors["bg"], bg=colors["bg"]):
    text = "" if direction == 'left' else ""
    return widget.TextBox(
        text=text,
        background=bg,
        foreground=fg,
        padding=0,
        fontsize=28
    )

# --- Screens ---
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(
                    background=colors["purple"],
                    foreground="#000000",
                    fmt="  {} ",
                ),
                get_powerline('right', colors["purple"], colors["bg"]),

                widget.GroupBox(
                    highlight_method="block",
                    this_current_screen_border=colors["purple"],
                    active=colors["cyan"],
                    inactive=colors["comment"],
                    padding_x=8,
                    rounded=True,
                ),

                widget.WindowName(
                    foreground=colors["green"],
                    format=" {name}",
                    max_chars=40,
                ),

                widget.Spacer(),

                # 🎵 Música
                get_powerline('left', colors["orange"], colors["bg"]),
                widget.Cmus(
                    background=colors["orange"],
                    foreground="#000000",
                    format=" ♫ {artist} - {title} ",
                ),

                # 🔥 CAVA (CORRIGIDO)
                get_powerline('left', colors["cyan"], colors["orange"]),
                widget.GenPollCommand(
                    background=colors["cyan"],
                    foreground="#000000",
                    cmd="~/.config/qtile/cava_widget.py",
                    update_interval=0.05,
                    shell=True,
                    fmt=" {} "
                ),

                # Teclado
                get_powerline('left', colors["yellow"], colors["cyan"]),
                widget.KeyboardLayout(
                    background=colors["yellow"],
                    foreground="#000000",
                    configured_keyboards=['br', 'us'],
                    fmt="  {} ",
                ),

                # Rede
                get_powerline('left', colors["green"], colors["yellow"]),
                widget.Net(
                    background=colors["green"],
                    foreground="#000000",
                    format=" 󰓅 {down} ",
                ),

                # RAM
                get_powerline('left', colors["red"], colors["green"]),
                widget.Memory(
                    background=colors["red"],
                    foreground="#000000",
                    format="  {MemUsed:.0f}M ",
                ),

                # CPU
                get_powerline('left', colors["cyan"], colors["red"]),
                widget.CPU(
                    background=colors["cyan"],
                    foreground="#000000",
                    format="  {load_percent}% ",
                ),

                # Volume
                get_powerline('left', colors["pink"], colors["cyan"]),
                widget.Volume(
                    background=colors["pink"],
                    foreground="#000000",
                    fmt="  {} ",
                ),

                # Relógio
                get_powerline('left', colors["purple"], colors["pink"]),
                widget.Clock(
                    background=colors["purple"],
                    foreground="#000000",
                    format="  %H:%M ",
                ),

                get_powerline('left', colors["bg"], colors["purple"]),
                widget.Systray(padding=10),

                widget.TextBox(
                    text=" ⏻ ",
                    background=colors["red"],
                    foreground="#000000",
                    fontsize=16,
                    padding=10,
                    mouse_callbacks={'Button1': lazy.spawn('/home/vibewill/.config/qtile/power-menu.sh menu')}
                ),
            ],
            bar_config["height"],
            background=bar_config["background"],
            margin=bar_config["margin"]
        ),
    ),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating()),
    Drag([mod], "Button3", lazy.window.set_size_floating()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "qtile"

@hook.subscribe.startup_once
def autostart():
    subprocess.Popen([os.path.expanduser('~/.config/qtile/autostart.sh')])

def trocar_wallpaper():
    subprocess.Popen("feh --recursive --randomize --bg-fill ~/Imagens/wallpapers", shell=True)