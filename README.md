# PARCIAL2

**INTRODUCCION**

Este trabajo presenta el desarrollo de diferentes analizadores sintácticos para resolver problemas de lógica y aritmética. Se comparan dos enfoques fundamentales: el análisis descendente mediante gramáticas LL(1) y herramientas como ANTLR, y el análisis ascendente utilizando el algoritmo CYK y Yacc/Bison.

A través de implementaciones en Python y C, se evalúa no solo la funcionalidad de cada parser, sino también su eficiencia en tiempo y memoria. El objetivo es demostrar por qué los modelos predictivos son la opción estándar en el desarrollo de compiladores frente a métodos de búsqueda exhaustiva.

**PUNTO 1**

Se uso el sistema operativo de linux ubunut, para la ejecucion se adjuntaran los comandos usados

**Paso 1**

GENERAR EL PERSER 

```bash
  antlr4 CRUD.g4
```

**Paso 2**

COMPILAR LOS ARCHIVOS GENERADOS 

```bash
javac *.java
```

**Paso 3**

Ver el arbol de derivacion 

```bash
grun CRUD s -gui
```

**DESCRIPCION DEL CODIGO**

El código define una gramática en ANTLR que permite interpretar diferentes operaciones tipo CRUD. Se establecen reglas para cada tipo de instrucción, como insertar, buscar, actualizar y eliminar, además de permitir listas de valores y condiciones.

También incluye reglas para manejar expresiones aritméticas, organizadas en niveles (expresión, término y factor) para respetar la precedencia de operadores. Finalmente, se definen los tokens básicos como identificadores, valores y operadores, junto con reglas para ignorar espacios en blanco.


**ANALISIS**

En este punto se creó una gramática en ANTLR para manejar operaciones tipo CRUD como insertar, buscar, actualizar y eliminar. También se permitió el uso de expresiones aritméticas dentro de los valores, respetando la precedencia de operadores.

Se probaron diferentes entradas y se generaron árboles de derivación para verificar que la gramática interpretara correctamente las instrucciones. Con esto se comprobó que el analizador funciona bien y solo acepta estructuras válidas.

**EJECUCION EN CONSOLA Y GRAFICAS**


