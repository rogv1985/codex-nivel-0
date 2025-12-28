"""
Programa: contador_palabras.py
Este script cuenta cuántas veces aparece una palabra objetivo en un texto,
usando coincidencia exacta por palabras separadas por espacios.

Entradas (por teclado, en este orden):
1) Texto (string)
2) Palabra objetivo (string)

Validaciones:
- Si el texto está vacío ("" o solo espacios) -> imprime "ERROR" y termina.
- Si la palabra objetivo está vacía ("" o solo espacios) -> imprime "ERROR" y termina.

Reglas de conteo:
- Coincidencia EXACTA por palabras separadas por espacios.
- Antes de separar en palabras, se elimina puntuación básica reemplazando
  por espacios: . , ; : ! ?
- No se normalizan mayúsculas/minúsculas ni se quitan acentos.

Ejemplos rápidos de uso:
Caso 1:
Texto: "El testigo declaró con claridad ante el juez y luego, en la audiencia final, otro testigo confirmó los mismos hechos con absoluta coherencia."
Objetivo: "testigo"
Salida esperada: 2

Caso 2:
Texto: "La declaración fue revisada por el juez y el abogado presentó nuevas pruebas documentales."
Objetivo: "testigo"
Salida esperada: 0

Caso 3:
Texto: "El testigo ofreció su versión de los hechos ante el tribunal."
Objetivo: ""
Salida esperada: ERROR
"""


def limpiar_texto(texto):
    """
    Reemplaza la puntuación básica por espacios.

    Recibe:
    - texto (str): cadena con el texto original.

    Devuelve:
    - str: el texto con la puntuación básica reemplazada por espacios.

    Ejemplo:
    >>> limpiar_texto("Hola, mundo!")
    'Hola  mundo '
    """
    signos = ".,;:!?"
    texto_limpio = texto  # Trabajamos sobre una copia para no perder el original.
    for signo in signos:
        # Cada signo de puntuación se reemplaza por un espacio.
        texto_limpio = texto_limpio.replace(signo, " ")
    return texto_limpio


def contar(texto_limpio, objetivo):
    """
    Cuenta coincidencias exactas de la palabra objetivo.

    Recibe:
    - texto_limpio (str): texto ya limpiado de la puntuación básica.
    - objetivo (str): palabra a buscar con coincidencia exacta.

    Devuelve:
    - int: número de coincidencias exactas encontradas.

    Ejemplo:
    >>> contar("hola hola adios", "hola")
    2
    """
    # split() separa por espacios (uno o más), formando palabras.
    palabras = texto_limpio.split()
    coincidencias = 0
    for palabra in palabras:
        # Comparamos palabra por palabra de manera exacta.
        if palabra == objetivo:
            coincidencias += 1
    return coincidencias


def main():
    """
    Punto de entrada del programa.

    Lee las dos entradas, valida que no estén vacías, limpia el texto,
    cuenta coincidencias exactas y muestra el resultado.

    Ejemplo:
    Entrada:
    El testigo declaró.
    testigo
    Salida:
    1
    """
    texto = input()
    objetivo = input()

    if texto.strip() == "":
        # Si el texto es vacío o solo espacios, se informa el error.
        print("ERROR")
        return

    if objetivo.strip() == "":
        # Si la palabra objetivo es vacía o solo espacios, se informa el error.
        print("ERROR")
        return

    # Primero limpiamos el texto de la puntuación básica.
    texto_limpio = limpiar_texto(texto)
    # Luego contamos coincidencias exactas con la palabra objetivo.
    resultado = contar(texto_limpio, objetivo)
    print(resultado)


if __name__ == "__main__":
    main()

# Notas:
# - Usar split() sirve para coincidencia exacta porque separa el texto en tokens
#   y permite comparar palabra por palabra con igualdad estricta.
# - Limitaciones: solo se reemplaza la puntuación básica (.,;:!?). Otros signos
#   como comillas, paréntesis o guiones no se contemplan y podrían afectar el conteo.
