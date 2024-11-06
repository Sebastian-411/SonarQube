import unittest
from main import calcular_area_cuadrado, calcular_area_rectangulo, calcular_area_circulo

class TestCalculoAreas(unittest.TestCase):

    def test_calcular_area_cuadrado(self):
        self.assertEqual(calcular_area_cuadrado(4), 16)
        self.assertEqual(calcular_area_cuadrado(0), 0)

    def test_calcular_area_rectangulo(self):
        self.assertEqual(calcular_area_rectangulo(5, 3), 15)
        self.assertEqual(calcular_area_rectangulo(0, 3), 0)

    def test_calcular_area_circulo(self):
        self.assertAlmostEqual(calcular_area_circulo(2), 12.566370614359172)
        self.assertAlmostEqual(calcular_area_circulo(0), 0)

if __name__ == "__main__":
    unittest.main()
