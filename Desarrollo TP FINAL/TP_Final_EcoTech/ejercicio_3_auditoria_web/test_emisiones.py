import unittest
from ejercicio_3_auditoria_web.sustentabilidad.emisiones import calcular_emisiones_carbono

class TestCalculoEmisiones(unittest.TestCase):
    """
    Clase de prueba para auditar la precisión del algoritmo de cálculo de emisiones[cite: 2].
    """

    def test_calculo_nominal(self):
        # Valida exactitud numérica ante valores nominales
        self.assertEqual(calcular_emisiones_carbono(100, 0.4), 40.0)
        self.assertEqual(calcular_emisiones_carbono(250, 0.4), 100.0)

    def test_consumo_cero(self):
        # Valida el comportamiento con consumo nulo
        self.assertEqual(calcular_emisiones_carbono(0), 0.0)

    def test_consumo_negativo_excepcion(self):
        # Valida la correcta elevación de ValueError ante consumos fuera de rango[cite: 2]
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-50)


if __name__ == "__main__":
    unittest.main()