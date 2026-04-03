from collections import defaultdict
import sys

def resolver():
    datos = sys.stdin.read().split()

    if not datos:
        return

    N = int(datos[0])  
    M = int(datos[1])   
    S = int(datos[2])  

    idx = 3
    terminal_a_socio = {}

    for _ in range(M):
        s = int(datos[idx])
        t = int(datos[idx + 1])
        terminal_a_socio[t] = s
        idx += 2

    clientes_por_socio = [defaultdict(int) for _ in range(N + 1)]

    for _ in range(S):
        c = int(datos[idx])      
        t = int(datos[idx + 1])  
        idx += 2

        if t in terminal_a_socio:
            socio = terminal_a_socio[t]
            clientes_por_socio[socio][c] += 1

    for socio in range(1, N + 1):
        if not clientes_por_socio[socio]:
            print(socio, -1)
        else:
            mejor_cliente = -1
            mejor_conteo = -1

            for cliente, conteo in clientes_por_socio[socio].items():
                if conteo > mejor_conteo or (conteo == mejor_conteo and cliente < mejor_cliente):
                    mejor_conteo = conteo
                    mejor_cliente = cliente

            print(socio, mejor_cliente)

if __name__ == "__main__":
    resolver()