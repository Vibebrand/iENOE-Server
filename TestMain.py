import unittest
import Servicio.TestServicioGestorSecciones

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Servicio.TestServicioGestorSecciones.TestServicioGestorSecciones)
    unittest.TextTestRunner(verbosity=2).run(suite)