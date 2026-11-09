import unittest
from src.pes21_method import ROOT, load_json, validate_record

class TestCryzan(unittest.TestCase):
    def test_record_math_and_attributes(self):
        r=load_json(ROOT/'examples/cryzan.json')
        x=validate_record(r, load_json(ROOT/'config/criteria.v1.json'))
        self.assertAlmostEqual(x['index'],77.07)
        self.assertEqual(r['overall_target'],77)
        self.assertEqual(len(r['attributes']),25)
        self.assertIsNone(r['overall_game_verified'])
    def test_context_transfer_no_arbitrary_physical_discount(self):
        r=load_json(ROOT/'examples/cryzan.json')
        p=load_json(ROOT/'config/competition-adjustment.v1.json')
        self.assertEqual(p['numerical_league_transfer_coefficients'],None)
        self.assertTrue(r['competition_context_adjustment']['double_count_warning'])
        self.assertEqual(r['attributes']['dribbling'],80)
        self.assertEqual(r['attributes']['finishing'],78)
        for a,v in [('speed',78),('acceleration',77),('jump',78),('kicking_power',83)]:
            self.assertEqual(r['attributes'][a],v)
            self.assertIn(a,p['attribute_dependency']['no_automatic_competition_discount'])

    def test_uncertainty(self):
        r=load_json(ROOT/'examples/cryzan.json')
        self.assertTrue(any('C60' in s for s in r['limitations']))
        self.assertTrue(any('Sofascore' in s for s in r['limitations']))
        self.assertTrue(any('Nível C' in s for s in r['limitations']))

if __name__=='__main__': unittest.main()
