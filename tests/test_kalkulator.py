import unittest

from src.kalkulator_geometri import (
    persegi,
    persegi_panjang,
    segitiga,
    lingkaran,
)


class TestKalkulatorGeometri(unittest.TestCase):

    def test_persegi(self):
        self.assertEqual(persegi(5), (25, 20))

    def test_persegi_panjang(self):
        self.assertEqual(
            persegi_panjang(8, 4),
            (32, 24)
        )

    def test_segitiga(self):
        self.assertEqual(
            segitiga(6, 4, 5, 5, 6),
            (12, 16)
        )

    def test_lingkaran(self):
        luas, keliling = lingkaran(7)
        self.assertAlmostEqual(luas, 153.93804, places=4)
        self.assertAlmostEqual(
            keliling, 43.98230, places=4
        )

    def test_input_nol(self):
        with self.assertRaises(ValueError):
            persegi(0)

    def test_segitiga_tidak_valid(self):
        with self.assertRaises(ValueError):
            segitiga(3, 4, 1, 2, 8)


if __name__ == "__main__":
    unittest.main()
