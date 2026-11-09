import unittest
from pathlib import Path
from src.pes21_method import ROOT, load_json, validate_record

class TestMontoro(unittest.TestCase):
    def test_montoro_complete_and_index(self):
        c=load_json(ROOT/'config/criteria.v1.json')
        rec=load_json(ROOT/'examples/alvaro-montoro.json')
        result=validate_record(rec,c)
        self.assertEqual(result['overall_target'],78)
        self.assertAlmostEqual(result['index'],78.295,places=3)
        self.assertEqual(result['tier'],'Craque')
        self.assertIsNone(result['overall_game_verified'])
        self.assertEqual(rec['player']['sofascore_player_id'],1650770)
        self.assertEqual(len(rec['attributes']),25)
        self.assertIn('Nível C', ' '.join(rec['limitations']))
    def test_required_protocol(self):
        self.assertIn('Nível C', (ROOT/'docs/avaliacao-fisica.md').read_text(encoding='utf-8'))
        self.assertIn('protocolo FÍSICO'.lower(), (ROOT/'AGENTS.md').read_text(encoding='utf-8').lower())

if __name__ == '__main__':
    unittest.main()
