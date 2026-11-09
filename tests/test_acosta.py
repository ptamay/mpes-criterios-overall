import unittest
from src.pes21_method import ROOT, load_json, validate_record

class TestAcosta(unittest.TestCase):
    def test_record_and_math(self):
        r = load_json(ROOT/'examples/luciano-acosta.json')
        x = validate_record(r, load_json(ROOT/'config/criteria.v1.json'))
        self.assertAlmostEqual(x['index'], 79.195)
        self.assertEqual(r['overall_target'], 79)
        self.assertEqual(len(r['attributes']), 25)
        self.assertIsNone(r['overall_game_verified'])
    def test_provenance_guardrails(self):
        r = load_json(ROOT/'examples/luciano-acosta.json')
        self.assertTrue(any('Sofascore' in s and 'não extraídos' in s for s in r['limitations']))
        self.assertTrue(any('Nível C' in s for s in r['limitations']))
        self.assertTrue(any('2023' in s and 'recorte' in s for s in r['limitations']))

if __name__ == '__main__': unittest.main()
