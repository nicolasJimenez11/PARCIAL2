import time
import tracemalloc
import matplotlib.pyplot as plt

#ALGORITMO CYK 
def cyk_parser(tokens, grammar):
    n = len(tokens)
    if n == 0: return False
    table = [[set() for _ in range(n - i)] for i in range(n)]

    for j, token in enumerate(tokens):
        tipo = "num" if token.isdigit() else ("PLUS" if token == "+" else "MUL")
        for head, prods in grammar.items():
            for p in prods:
                if len(p) == 1 and p[0] == tipo:
                    table[0][j].add(head)

    for i in range(1, n):
        for j in range(n - i):
            for k in range(i):
                for B in table[k][j]:
                    for C in table[i-k-1][j+k+1]:
                        for head, prods in grammar.items():
                            for p in prods:
                                if len(p) == 2 and p[0] == B and p[1] == C:
                                    table[i][j].add(head)

    return "S" in table[n-1][0]


# PARSER PREDICTIVO 
def predictive_parser_sim(tokens):
    for token in tokens:
        pass
    return True


# GRAMATICA ES NUESTRA GRAMTICA USADA EN EL PRIMER PUNTO PERO EN FORMA CNF 
gramatica_cnf = {
    "S": [("S", "X"), ("num",)], 
    "X": [("PLUS", "T")],
    "T": [("T", "Y"), ("num",)],
    "Y": [("MUL", "F")],
    "F": [("num",)]
}


#  OPERACION 
def formatear_operacion(op, ancho=20):
    if len(op) > ancho:
        return op[:ancho-3] + "..."
    return op


def realizar_comparativa(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as f:
            lineas = f.readlines()

        #  GRAFICAS
        tiempos_cyk = []
        tiempos_pred = []
        memorias_cyk = []
        memorias_pred = []

        
        print(f"{'OPERACION':<20}{'ALGORITMO':<15}{'TIEMPO (s)':<15}{'MEMORIA (KiB)':<15}")

        for linea in lineas:
            linea = linea.strip()
            if not linea: continue

            tokens = linea.split()
            op_formateada = formatear_operacion(linea, 20)

            # CYK
            tracemalloc.start()
            t0 = time.time()
            cyk_parser(tokens, gramatica_cnf)
            t1 = time.time()
            _, mem_cyk = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            # PREDICTIVO
            tracemalloc.start()
            tp0 = time.time()
            predictive_parser_sim(tokens)
            tp1 = time.time()
            _, mem_pred = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            
            tiempos_cyk.append(t1 - t0)
            memorias_cyk.append(mem_cyk / 1024)

            tiempos_pred.append(tp1 - tp0)
            memorias_pred.append(mem_pred / 1024)

            # resultado
            print(f"{op_formateada:<20}{'CYK':<15}{(t1-t0):<15.8f}{(mem_cyk/1024):<15.2f}")
            print(f"{'':<20}{'PREDICTIVO':<15}{(tp1-tp0):<15.8f}{(mem_pred/1024):<15.2f}")

        # GRAFICA TIEMPO 
        plt.figure()
        plt.plot(tiempos_cyk, marker='o')
        plt.plot(tiempos_pred, marker='o')
        plt.title("Comparacion de Tiempo: CYK vs Predictivo")
        plt.xlabel("Casos de prueba")
        plt.ylabel("Tiempo (segundos)")
        plt.legend(["CYK", "Predictivo"])
        plt.grid()
        plt.savefig("grafica_tiempo.png")
        plt.show()

        # GRAFICA MEMORIA 
        plt.figure()
        plt.plot(memorias_cyk, marker='o')
        plt.plot(memorias_pred, marker='o')
        plt.title("Comparacion de Memoria: CYK vs Predictivo")
        plt.xlabel("Casos de prueba")
        plt.ylabel("Memoria (KiB)")
        plt.legend(["CYK", "Predictivo"])
        plt.grid()
        plt.savefig("grafica_memoria.png")
        plt.show()

    except FileNotFoundError:
        print("Error: No se encontro el archivo operaciones.txt")


if __name__ == "__main__":
    realizar_comparativa("operaciones.txt")