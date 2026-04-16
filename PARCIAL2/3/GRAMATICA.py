from collections import defaultdict

# GRAMATICA
gramatica = {
    "S": [["A", "a", "A", "b"], ["B", "b", "B", "a"]],
    "A": [["e"]],
    "B": [["e"]]
}

# PRIMEROS
def calcular_primeros():
    primeros = defaultdict(set)

    cambio = True
    while cambio:
        cambio = False
        for nt in gramatica:
            for prod in gramatica[nt]:

                agregar_epsilon = True

                for simbolo in prod:

                    if simbolo not in gramatica:  # terminal
                        if simbolo not in primeros[nt]:
                            primeros[nt].add(simbolo)
                            cambio = True
                        agregar_epsilon = False
                        break

                    else:  # no terminal
                        antes = len(primeros[nt])
                        primeros[nt] |= (primeros[simbolo] - {"e"})

                        if len(primeros[nt]) != antes:
                            cambio = True

                        if "e" not in primeros[simbolo]:
                            agregar_epsilon = False
                            break

                if agregar_epsilon:
                    if "e" not in primeros[nt]:
                        primeros[nt].add("e")
                        cambio = True

    return primeros

# SIGUIENTES
def calcular_siguientes(primeros):
    siguientes = defaultdict(set)
    siguientes["S"].add("$")

    cambio = True
    while cambio:
        cambio = False
        for nt in gramatica:
            for prod in gramatica[nt]:
                follow_temp = siguientes[nt].copy()

                for simbolo in reversed(prod):
                    if simbolo in gramatica:
                        antes = len(siguientes[simbolo])
                        siguientes[simbolo] |= follow_temp

                        if "e" in primeros[simbolo]:
                            follow_temp |= (primeros[simbolo] - {"e"})
                        else:
                            follow_temp = primeros[simbolo]

                        if len(siguientes[simbolo]) != antes:
                            cambio = True
                    else:
                        follow_temp = {simbolo}

    return siguientes

# PREDICCION
def calcular_prediccion(primeros, siguientes):
    prediccion = {}

    for nt in gramatica:
        for prod in gramatica[nt]:
            key = (nt, tuple(prod))
            conjunto = set()

            if prod == ["e"]:
                conjunto |= siguientes[nt]
            else:
                for simbolo in prod:
                    if simbolo not in gramatica:
                        conjunto.add(simbolo)
                        break
                    else:
                        conjunto |= (primeros[simbolo] - {"e"})
                        if "e" not in primeros[simbolo]:
                            break
                else:
                    conjunto |= siguientes[nt]

            prediccion[key] = conjunto

    return prediccion

# LL1
def es_LL1(prediccion):
    reglas = defaultdict(list)

    for (nt, prod), conj in prediccion.items():
        reglas[nt].append(conj)

    for nt in reglas:
        conjuntos = reglas[nt]
        for i in range(len(conjuntos)):
            for j in range(i+1, len(conjuntos)):
                if conjuntos[i] & conjuntos[j]:
                    return False
    return True

# EJECUCION
primeros = calcular_primeros()
siguientes = calcular_siguientes(primeros)
prediccion = calcular_prediccion(primeros, siguientes)

print("PRIMEROS:")
for k, v in primeros.items():
    print(k, ":", v)

print("SIGUIENTES:")
for k, v in siguientes.items():
    print(k, ":", v)

print("PREDICCION:")
for (nt, prod), conj in prediccion.items():
    print(f"{nt} -> {' '.join(prod)} : {conj}")

print("Es LL1:", es_LL1(prediccion))