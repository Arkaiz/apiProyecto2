import unittest                
from python.funciones_auxiliares import calculariva             
class tests_iva(unittest.TestCase):          
    def test_iva(self):
        self.assertEqual(calculariva(100),21)
if __name__ == '__main__':
    unittest.main()
