# Construcción de la fase inicial de un Compilador con Lex y Yacc 🚀

Lex y Yacc son herramientas utilizadas para la construcción de compiladores e intérpretes. Estos permiten procesar y traducir código fuente mediante dos fases principales, `Analizador Léxico` y `Analizador Sintáctico`.

## 🖥️ Entorno e Información

El proyecto se ejecuta en un **entorno Docker**, permitiendo un ambiente controlado y reproducible para el desarrollo del compilador.

### 1. Analizador Léxico (Lex - `simple_language.l`)

Lex se encarga de **tokenizar** el código fuente, es decir, dividirlo en unidades mínimas significativas llamadas *tokens*.  
En el archivo `simple_language.l`, se han definido reglas para reconocer:

- **Identificadores** (nombres de variables)
- **Números** (constantes numéricas)
- **Operadores** (`+`, `-`, `*`, `/`, `=`)  
- **Errores léxicos**, para detectar tokens inválidos en el código fuente.

### 2. Analizador Sintáctico (Yacc - `simple_language.y`)

Yacc recibe los *tokens* generados por Lex y los organiza en una estructura jerárquica según la **gramática** definida.  
Esto permite interpretar y validar expresiones correctamente.  

#### Modificaciones realizadas

1. Se agregó **asignación de valores** a variables (`x = 5`).
2. Se implementó **operaciones aritméticas simples** (`x + y`).
3. Se probaron **expresiones más complejas** y se verificó su procesamiento.
4. Se permitió la **asignación con expresiones aritméticas** (`x = a + b * 2`).
5. Se incorporó **manejo de errores** para detectar tokens inválidos.
6. Se experimentó con **precedencia de operadores**, observando su impacto en la generación del árbol sintáctico.

## 📜 Instrucciones

1. **Clonar el repositorio**:
   1.1 HTTPS:

    ```bash
    git clone https://github.com/JosueSay/LenguageDesign
    ```

   1.2 SSH:

    ```bash
    git clone git@github.com:JosueSay/LenguageDesign.git
    ```

2. Navegar a la carpeta `Lex_Yacc`

    ```bash
     cd Lex_Yacc
    ```

3. Ejecutar el Docker

    ```bash
    docker buildx build -t lab1 .
    docker run --rm -it -v "$(pwd)":/home lab1
    ```

    3.1 En caso de trabajar en powershell se puede utilizar el siguiente comando para correr el docker:

    ```bash
    docker run --rm -it -v "${PWD}:/home" lab1
    ```

4. Crea nuestro analizador lexico y grafico con estos comandos.

    ```bash
    cd files
    flex simple_language.l
    bison -d simple_language.y -o y.tab.c
    g++ lex.yy.c y.tab.c -o parser    
    ```

5. Ejecutar el programa.

    ```bash
    ./parser
    ```

6. Se puede ingresan caracteres para la entrada de Analizador Léxico y Sintáctico como:

    ```bash
    4+5:
    ```

## 🎥 Multimedia

### Demostración

[Enlace a demostración en YouTube](https://youtu.be/EZBBljW2kW4)

### Explicación

[Enlace a explicativo en YouTube](https://youtu.be/4qcCxBGBVBU)
