# Qtile - Barra Personalizada Moderna

## 🎨 Melhorias Implementadas

### 1. **Design Visual Moderno**
- **Tema Dracula**: Cores escuras e elegantes
- **Efeito Powerline**: Separadores visuais coloridos
- **Altura aumentada**: Barra de 30px para melhor legibilidade
- **Borda inferior**: Sutil linha roxa para definir a barra

### 2. **Organização dos Widgets**
- **Lado esquerdo**: Layout atual + grupos de trabalho + nome da janela
- **Lado direito**: Informações do sistema organizadas por cores

### 3. **Esquema de Cores**
| Widget | Cor | Função |
|--------|-----|--------|
| Layout | 🟣 Roxo | Identificação do layout atual |
| Música | 🟠 Laranja | Player de música (Cmus) |
| Teclado | 🟡 Amarelo | Layout do teclado |
| Rede | 🟢 Verde | Velocidade de rede |
| Memória | 🔴 Vermelho | Uso da RAM |
| CPU | 🔵 Ciano | Uso do processador |
| Volume | 🟣 Rosa | Controle de volume |
| Relógio | 🟣 Roxo | Data e hora |

### 4. **Ícones e Tipografia**
- **Fonte**: Noto Sans Mono (disponível no sistema)
- **Ícones Unicode**: Símbolos nativos para melhor compatibilidade
- **Tamanho otimizado**: 13px para texto, 16px para ícones

## 📁 Arquivos

### `config.py`
Configuração principal do Qtile com a nova barra personalizada.

### `theme.py`
Arquivo separado com todas as configurações de tema:
- Paleta de cores
- Configurações de fonte
- Parâmetros da barra
- Configurações dos widgets

## 🚀 Como Aplicar

1. **Recarregar configuração**:
   ```bash
   # Tecla de atalho: Mod4 + Ctrl + R
   # Ou via terminal:
   qtile cmd-obj -o cmd -f restart
   ```

2. **Se houver problemas com fontes**:
   ```bash
   # Instalar Nerd Fonts (opcional, para mais ícones)
   sudo dnf install fontawesome-fonts
   ```

## 🎛️ Personalização

### Alterar Cores
Edite o arquivo `theme.py` e modifique o dicionário `colors`:
```python
colors = {
    "bg": "#282a36",      # Cor de fundo
    "purple": "#bd93f9",  # Cor primária
    # ... outras cores
}
```

### Ajustar Widgets
No `config.py`, você pode:
- Remover widgets desnecessários
- Alterar a ordem dos widgets
- Modificar as configurações específicas

### Temas Alternativos
Você pode criar diferentes temas criando novos arquivos como `theme_dark.py`, `theme_light.py`, etc.

## 🔧 Widgets Incluídos

- **CurrentLayout**: Layout ativo
- **GroupBox**: Grupos de trabalho (1-9)
- **WindowName**: Nome da janela ativa
- **Cmus**: Player de música
- **KeyboardLayout**: Layout do teclado (BR/US)
- **Net**: Velocidade da rede
- **Memory**: Uso da memória RAM
- **CPU**: Uso do processador
- **Volume**: Controle de volume
- **Clock**: Data e hora
- **Systray**: Ícones do sistema

## 📋 Dicas

1. **Personalizar atalhos**: Os atalhos estão configurados para o seu uso atual
2. **Adicionar widgets**: Consulte a documentação do Qtile para novos widgets
3. **Backup**: Sempre faça backup antes de grandes alterações
4. **Testes**: Use `python -m py_compile config.py` para verificar sintaxe

Aproveite sua nova barra moderna! 🎉