def intervalo_fechado(a, b):
    if a > b:
        print(f'{a} é maior do que {b}')
        return

    ## caso base / condição de parada
    if a == b:
        print(a, end = ' ')
    ## passo recursivo
    else:
        intervalo_fechado(a + 1, b)
        print(a, end = ' ')

intervalo_fechado(1, 10)
