import unittest
from src.pes21_method import ROOT,load_json,validate_record

class TestCompetitionAdjustment(unittest.TestCase):
 def test_policy_and_example(self):
  p=load_json(ROOT/'config/competition-adjustment.v1.json')
  c=load_json(ROOT/'config/criteria.v1.json')
  self.assertEqual(p['status'],'APPROVED_PRINCIPLE_NOT_CALIBRATED')
  self.assertIsNone(p['numerical_league_transfer_coefficients'])
  self.assertEqual(c['weights'],{'technical':.45,'performance':.35,'competition':.15,'history':.05})
  self.assertIn('dribbling',p['attribute_dependency']['high'])
  self.assertIn('speed',p['attribute_dependency']['no_automatic_competition_discount'])
  r=load_json(ROOT/'examples/cryzan.json')
  self.assertEqual(validate_record(r,c)['overall_target'],77)
 def test_docs_and_source_disclaimer(self):
  d=(ROOT/'docs/contextualizacao-competitiva.md').read_text(encoding='utf-8')
  a=(ROOT/'AGENTS.md').read_text(encoding='utf-8')
  for token in ('dupla penalização','fator','drible','velocidade'):
   self.assertIn(token,d.lower())
  self.assertIn('NORMALIZAÇÃO COMPETITIVA',a)

if __name__=='__main__':unittest.main()
