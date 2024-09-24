# Constantes
NUMERO_MAXIMO = 150  # Número total de Pokémon da 1ª geração
TIPOS = ('Normal', 'Fogo', 'Água', 'Planta')

# Funções
def verificar_tipo_pokemon(tipo):
    """Verifica se um tipo de Pokémon é válido."""
    return tipo in TIPOS

print("dir() dentro do módulo: ", dir(), '\n')
