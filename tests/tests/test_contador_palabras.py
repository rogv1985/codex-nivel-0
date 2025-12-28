import sys
import os

# Agregar la raíz del proyecto al PYTHONPATH para que pytest encuentre el módulo
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import unittest
from contador_palabras import limpiar_texto, contar

class TestContadorPalabras(unittest.TestCase):
    """
    Tests automatizados para el script contador_palabras.py
    """

    def test_coincidencia_simple(self):
        texto = "El testigo habló ante el juez. El testigo fue claro."
        objetivo = "testigo"
        texto_limpio = limpiar_texto(texto)
        resultado = contar(texto_limpio, objetivo)
        self.assertEqual(resultado, 2)

    def test_sin_coincidencias(self):
        texto = "La declaración fue revisada por el juez."
        objetivo = "testigo"
        texto_limpio = limpiar_texto(texto)
        resultado = contar(texto_limpio, objetivo)
        self.assertEqual(resultado, 0)

    def test_puntuacion(self):
        texto = "testigo,testigo;testigo!"
        objetivo = "testigo"
        texto_limpio = limpiar_texto(texto)
        resultado = contar(texto_limpio, objetivo)
        self.assertEqual(resultado, 3)

    def test_texto_vacio(self):
        texto = ""
        objetivo = "testigo"
        self.assertEqual(texto.strip(), "")

    def test_objetivo_vacio(self):
        texto = "El testigo habló"
        objetivo = ""
        self.assertEqual(objetivo.strip(), "")


if __name__ == "__main__":
    unittest.main()
