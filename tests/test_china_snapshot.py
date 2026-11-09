import unittest
from decimal import Decimal, ROUND_HALF_UP
from src.pes21_method import ROOT, load_json, validate_record

class ChinaSnapshotTests(unittest.TestCase):
    def test_historical_comparison_same_date_and_conservative_not_official(self):
        s=load_json(ROOT/'config/competition-snapshots.v1.json')
        hist=s['historical_snapshot']
        self.assertEqual(hist['china_csl']['rating'],62.8)
        self.assertEqual(hist['brazil_serie_a']['rating'],77.9)
        self.assertAlmostEqual(hist['delta_brazil_minus_china'],15.1)
        self.assertEqual(hist['date'],'2025-11-03')
        self.assertFalse(s['approved_policy']['conservative_is_official_opta'])
        self.assertFalse(s['approved_policy']['current_2026_china_score_available'])
        self.assertTrue(s['approved_policy']['do_not_mix_years'])
    def test_cryzan_score_and_scenarios(self):
        r=load_json(ROOT/'examples/cryzan.json')
        c=load_json(ROOT/'config/criteria.v1.json')
        self.assertEqual(validate_record(r,c)['overall_target'],77)
        self.assertAlmostEqual(r['dimensions']['competition']['score'],62.8)
        index=Decimal('0.45')*78+Decimal('0.35')*82+Decimal('0.15')*Decimal('62.8')+Decimal('0.05')*77
        conservative=Decimal('0.45')*78+Decimal('0.35')*82+Decimal('0.15')*60+Decimal('0.05')*77
        self.assertEqual(index,Decimal('77.070'))
        self.assertEqual(conservative,Decimal('76.650'))
        self.assertEqual(int(index.quantize(Decimal('1'),rounding=ROUND_HALF_UP)),77)
        self.assertEqual(int(conservative.quantize(Decimal('1'),rounding=ROUND_HALF_UP)),77)
        self.assertEqual(r['season_evidence'][-1]['matches'],24)
        self.assertEqual(r['season_evidence'][-1]['goals'],20)
        self.assertEqual(r['attributes']['physical_contact'],80)
        self.assertEqual(r['attributes']['dribbling'],80)
    def test_context_rule_no_double_penalty_and_sources(self):
        p=load_json(ROOT/'config/competition-adjustment.v1.json')
        self.assertIsNone(p['numerical_league_transfer_coefficients'])
        self.assertAlmostEqual(p['china_historical_c_reference_2025_11'],62.8)
        self.assertAlmostEqual(p['china_conservative_c_scenario'],60.0)
        r=load_json(ROOT/'examples/cryzan.json')
        self.assertTrue(r['competition_context_adjustment']['double_count_warning'])
        self.assertFalse(r['competition_context_adjustment']['league_rating_current_2026_verified'])
        for field in ('speed','acceleration','jump','kicking_power'):
            self.assertEqual(r['attributes'][field],r['competition_context_adjustment']['unchanged_physical_attributes'][field])
