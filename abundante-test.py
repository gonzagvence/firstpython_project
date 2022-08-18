import unittest

# Se importa el código a testear.
from abundante import es_divisor, suma_divisores_positivos, es_abundante, \
                      suma_abundantes, abundante_mas_cercano

#####################################################################

class TestAbundancia(unittest.TestCase):
    def test_divisible(self):
        self.assertTrue(es_divisor(5, 10), True)
        self.assertTrue(es_divisor(1,1), True)
        self.assertTrue(es_divisor(1,5), True)
        self.assertFalse(es_divisor(15,5),False)

    def test_sumadivisores(self):
        self.assertEqual(suma_divisores_positivos(12),28)
        self.assertEqual(suma_divisores_positivos(1),1)
        self.assertEqual(suma_divisores_positivos(13),14)
        self.assertEqual(suma_divisores_positivos(179),180)

    def test_esabundante(self):
        self.assertTrue(es_abundante(12), True)
        self.assertFalse(es_abundante(1009) ,False)
        self.assertFalse(es_abundante(13), False)
        self.assertFalse(es_abundante(32), False)

    def test_sumaabundantes(self):
        self.assertEqual(suma_abundantes(1, 12), 12)
        self.assertEqual(suma_abundantes(1, 11), 0)
        self.assertEqual(suma_abundantes(12, 12), 12)
        self.assertEqual(suma_abundantes(12, 18), 30)

    def test_abundantemascercano(self):
        self.assertEqual(abundante_mas_cercano(1), 12)
        self.assertEqual(abundante_mas_cercano(15), 18)
        self.assertEqual(abundante_mas_cercano(12), 12)
        self.assertNotEqual(abundante_mas_cercano(22), 20)


unittest.main()
