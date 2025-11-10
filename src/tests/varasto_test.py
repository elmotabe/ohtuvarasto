"""testejä"""
import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    """Test class"""
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        """tyhjä varasto"""
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        """valmiiksi oikea tilavuus"""
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        """saldon lisäys"""
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        """vapaan tilan pienennys"""
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        """ottaminen toimii"""
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        """ottaminen lisää vapaata tilaa"""
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)


    def test_konstruktori_negatiivinen_alkusaldo(self):
        """alussa saldo negatiivinen"""
        v = Varasto(10, -3)
        self.assertEqual(v.tilavuus, 10)
        self.assertEqual(v.saldo, 0)

    def test_konstruktori_alkusaldo_suurempi_kuin_tilavuus(self):
        """saldo suurempi kun tilavuus"""
        v = Varasto(10, 20)
        self.assertEqual(v.saldo, 10)

    def test_lisays_negatiivinen_ei_muuta_saldoa(self):
        """negatiivisen lisäys ei muuta saldoa"""
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_yli_tilavuuden_tayttaa_varaston(self):
        """yli lisäys toimii oikein"""
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_otto_negatiivinen_palauttaa_nolla(self):
        """ei palauta negativiista"""
        self.varasto.lisaa_varastoon(5)
        saatu = self.varasto.ota_varastosta(-2)
        self.assertEqual(saatu, 0.0)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_otto_enemman_kuin_saldo_tyhjentaa_varaston(self):
        """varasto tyhjenee jos otetaan enemmän kun saldo"""
        self.varasto.lisaa_varastoon(6)
        saatu = self.varasto.ota_varastosta(8)
        self.assertEqual(saatu, 6)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_str_palauttaa_oikean_merkkijonon(self):
        """str toimii"""
        self.varasto.lisaa_varastoon(4)
        teksti = str(self.varasto)
        self.assertIn("saldo = 4", teksti)
        self.assertIn("vielä tilaa 6", teksti)

    def test_konstruktori_nolla_ja_negatiivinen_tilavuus(self):
        """negatiivinen tilavuus"""
        v = Varasto(0)
        self.assertAlmostEqual(v.tilavuus, 0.0)
        self.assertAlmostEqual(v.saldo, 0.0)

        v2 = Varasto(-5)
        self.assertAlmostEqual(v2.tilavuus, 0.0)
        self.assertAlmostEqual(v2.saldo, 0.0)
