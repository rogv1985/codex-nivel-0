"""
Contador de palabras con coincidencia exacta.
"""


def limpiar_texto(texto):
    """
    Reemplaza la puntuación básica por espacios.
    """
    signos = ".,;:!?"
    texto_limpio = texto
    for signo in signos:
        texto_limpio = texto_limpio.replace(signo, " ")
    return texto_limpio


def contar(texto_limpio, objetivo):
    """
    Cuenta coincidencias exactas de la palabra objetivo.
    """
    palabras = texto_limpio.split()
    coincidencias = 0
    for palabra in palabras:
        if palabra == objetivo:
            coincidencias += 1
    return coincidencias


def main():
    """
    Punto de entrada del programa.
    """
    texto = input()
    objetivo = input()

    if texto.strip() == "":
        print("ERROR")
        return

    if objetivo.strip() == "":
        print("ERROR")
        return

    texto_limpio = limpiar_texto(texto)
    resultado = contar(texto_limpio, objetivo)
    print(resultado)


if __name__ == "__main__":
    main()
