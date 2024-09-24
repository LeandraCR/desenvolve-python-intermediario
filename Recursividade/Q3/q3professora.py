def somatorio(n):
    ## caso base / condição de parada
    if n == 1:
        return n
    ## passo recursivo
    else:
        return n + somatorio(n - 1)

somatorio(5)
