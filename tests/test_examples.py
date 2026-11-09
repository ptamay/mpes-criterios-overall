import copy
import unittest
from pathlib import Path
from src.pes21_method import ROOT, load_json, validate_record

class TestExamples(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.criteria=load_json(ROOT/'config/criteria.v1.json')

    def test_garnacho(self):
        out=validate_record(load_json(ROOT/'examples/garnacho.json'),self.criteria)
        self.assertEqual(out['overall_target'],78)
        self.assertAlmostEqual(out['index'],77.85)
        self.assertEqual(out['tier'],'Craque')
        self.assertFalse(out['calibrated'])

    def test_lukaku(self):
        out=validate_record(load_json(ROOT/'examples/lukaku.json'),self.criteria)
        self.assertEqual(out['overall_target'],79)
        self.assertAlmostEqual(out['index'],79.20)
        self.assertIsNone(out['overall_game_verified'])

    def test_missing_attribute_fails(self):
        rec=load_json(ROOT/'examples/garnacho.json')
        rec['attributes'].pop('jump')
        with self.assertRaisesRegex(ValueError,'25 atributos'):
            validate_record(rec,self.criteria)

    def test_not_allow_unverified_game_ovr(self):
        rec=load_json(ROOT/'examples/lukaku.json')
        rec['overall_game_verified']=79
        with self.assertRaisesRegex(ValueError,'evidência'):
            validate_record(rec,self.criteria)

    def test_shrinkage_rule_not_applied_without_calibration(self):
        self.assertEqual(self.criteria['smoothing']['status'],'proposal_not_applied_to_examples')
        self.assertEqual(self.criteria['calibration_status'],'NOT_CALIBRATED')

if __name__=='__main__':
    unittest.main()
