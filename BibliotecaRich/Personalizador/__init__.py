# __init__.py

# Importando as funções de estilo
from .estilo import aplicar_estilo, destacar_palavra

# Importando as funções de layout
from .layout import mostrar_layout, layout_com_borda

# Importando as funções de painel
from .painel import mostrar_painel, painel_somente_conteudo

# Importando as funções de progresso
from .progresso import barra_progresso_simples, barra_progresso_leitura

# Definindo o que será importado com 'from Personalizador import *'
__all__ = [
    "aplicar_estilo", 
    "destacar_palavra",
    "mostrar_layout", 
    "layout_com_borda",
    "mostrar_painel", 
    "painel_somente_conteudo", 
    "barra_progresso_simples", 
    "barra_progresso_leitura"
]
