import unittest
from src.pes21_method import ROOT, load_json, validate_record

class TestMessiNeymar2026(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config=load_json(ROOT/'config/criteria.v1.json')
        cls.m=load_json(ROOT/'examples/lionel-messi.json')
        cls.n=load_json(ROOT/'examples/neymar.json')

    def test_both_valid_and_non_game_ovr(self):
        for r,expected,idx in ((self.m,86,86.025),(self.n,82,82.185)):
            got=validate_record(r,self.config)
            self.assertAlmostEqual(got['index'],idx)
            self.assertEqual(got['overall_target'],expected)
            self.assertEqual(len(r['attributes']),25)
            self.assertIsNone(r['overall_game_verified'])

    def test_samesnapshot_context_and_dribble_order(self):
        self.assertEqual(self.m['attributes']['dribbling'],90)
        self.assertEqual(self.n['attributes']['dribbling'],88)
        self.assertGreater(self.m['attributes']['dribbling'],self.n['attributes']['dribbling'])
        snapshot=load_json(ROOT/'config/competition-snapshots.v1.json')['historical_snapshot']
        self.assertEqual(self.m['dimensions']['competition']['score'],snapshot['other_2025_leagues']['mls'])
        self.assertEqual(self.n['dimensions']['competition']['score'],snapshot['brazil_serie_a']['rating'])
        self.assertEqual(self.m['player']['club_as_of_snapshot'],'Inter Miami CF')
        self.assertEqual(self.n['player']['club_as_of_snapshot'],'Santos')

    def test_sofascore_scope_not_mixed(self):
        m=self.m['season_evidence'][-1]
        n=self.n['season_evidence'][-1]
        self.assertEqual((m['matches'],m['minutes'],m['goals'],m['assists']),(30,2574,26,13))
        self.assertEqual((n['matches'],n['minutes'],n['goals'],n['assists']),(14,1178,8,3))
        self.assertTrue(any('FotMob' in a for a in self.m['limitations']))
        self.assertTrue(any('FotMob' in a for a in self.n['limitations']))

if __name__=='__main__': unittest.main()
