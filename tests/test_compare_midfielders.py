import unittest
from src.pes21_method import ROOT, load_json, validate_record

class TestMidfielderComparison(unittest.TestCase):
    def test_scores_and_completeness(self):
        cfg=load_json(ROOT/'config/criteria.v1.json')
        mt=load_json(ROOT/'examples/alvaro-montoro.json')
        bt=load_json(ROOT/'examples/gabriel-bontempo.json')
        self.assertAlmostEqual(validate_record(mt,cfg)['index'],78.295,places=3)
        self.assertAlmostEqual(validate_record(bt,cfg)['index'],76.145,places=3)
        self.assertEqual((mt['overall_target'],bt['overall_target']),(78,76))
        self.assertGreater(mt['attributes']['dribbling'],bt['attributes']['dribbling'])
        self.assertGreater(bt['attributes']['low_pass'],mt['attributes']['low_pass'])
        self.assertGreater(bt['attributes']['ball_winning'],mt['attributes']['ball_winning'])
        self.assertEqual(len(mt['attributes']),25)
        self.assertEqual(len(bt['attributes']),25)
        self.assertIsNone(mt['overall_game_verified'])
        self.assertIsNone(bt['overall_game_verified'])
    def test_physical_conservatism(self):
        docs=(ROOT/'docs/avaliacao-fisica.md').read_text(encoding='utf-8')
        self.assertIn('Nível C',docs)
        for player in ('alvaro-montoro','gabriel-bontempo'):
            d=load_json(ROOT/f'examples/{player}.json')
            self.assertIn('Nível C',' '.join(d['limitations']))

if __name__ == '__main__':
    unittest.main()
