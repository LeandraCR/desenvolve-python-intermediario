import pokedex

TIPOS = ("1", "2")
def funcao_exemplo():
    TIPOS = ("A", "B")
    print("dir() na função: ", dir())
    print("TIPOS na função: ", TIPOS, '\n')

print("dir() no programa principal: ", dir())
print("TIPOS no programa principal: ", TIPOS, '\n')

funcao_exemplo()

print("TIPOS do módulo pokédex no programa principal (pokedex.TIPOS):\n", pokedex.TIPOS)
