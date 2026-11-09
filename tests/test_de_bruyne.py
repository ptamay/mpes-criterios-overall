import unittest
from src.pes21_method import ROOT, load_json, validate_record

class TestDeBruyne(unittest.TestCase):
    def test_editorial_record(self):
        record=load_json(ROOT/'examples/kevin-de-bruyne.json')
        result=validate_record(record,load_json(ROOT/'config/criteria.v1.json'))
        self.assertAlmostEqual(result['index'],82.40)
        self.assertEqual(result['overall_target'],82)
        self.assertIsNone(result['overall_game_verified'])
        self.assertEqual(len(record['attributes']),25)
        self.assertEqual(record['other_pes_settings']['injury_resistance'],1)
    def test_physical_evidence_not_mislabeled(self):
        r=load_json(ROOT/'examples/kevin-de-bruyne.json')
        self.assertTrue(any('31,22 km/h' in t and '4 partidas' in t for t in r['limitations']))
        self.assertTrue(any('Aceleração não foi medida' in t for t in r['limitations']))

if __name__=='__main__': unittest.main()
