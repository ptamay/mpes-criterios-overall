import unittest
from src.pes21_method import ROOT, load_json, ATTRIBUTES, validate_record
from scripts.render_readme import BEGIN, END, build_section, replace_generated

class TestDocumentationAndSkills(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = load_json(ROOT/'config/pes21-skills.json')
        cls.readme = (ROOT/'README.md').read_text(encoding='utf-8')

    def test_catalog_has_41_player_skills_and_7_distinct_com_styles(self):
        skills=[x['en'] for x in self.catalog['player_skills']]
        com=[x['en'] for x in self.catalog['com_playing_styles']]
        self.assertEqual(len(skills),41)
        self.assertEqual(len(set(skills)),41)
        self.assertEqual(len(com),7)
        self.assertEqual(len(set(com)),7)
        self.assertFalse(set(skills) & set(com))

    def test_example_skills_are_valid_and_unmapped_terms_identified(self):
        valid={x['en'] for x in self.catalog['player_skills']}
        cfg=load_json(ROOT/'config/criteria.v1.json')
        for key in ['garnacho','lukaku']:
            record=load_json(ROOT/f'examples/{key}.json')
            self.assertTrue(set(record['other_pes_settings']['special_skills_proposed']) <= valid)
            self.assertIsInstance(record['other_pes_settings']['skills_pending_mapping'],list)
            validate_record(record,cfg)

    def test_unknown_skill_rejected(self):
        record=load_json(ROOT/'examples/garnacho.json')
        record['other_pes_settings']['special_skills_proposed'].append('Skill inventada')
        with self.assertRaisesRegex(ValueError,'catálogo PES 2021'):
            validate_record(record,load_json(ROOT/'config/criteria.v1.json'))

    def test_generated_table_matches_example_values_and_dictionary(self):
        self.assertIn(BEGIN,self.readme)
        self.assertIn(END,self.readme)
        self.assertEqual(replace_generated(self.readme),self.readme)
        for label in ('Resistência a lesões','Pé fraco — precisão','Forma física','Impulsão','Talento de GO','Estilo COM'):
            self.assertIn(label,self.readme)
        self.assertEqual(len(ATTRIBUTES),25)

    def test_explicit_two_source_historical_research_protocol(self):
        doc=(ROOT/'docs/coleta-historica.md').read_text(encoding='utf-8')
        agents=(ROOT/'AGENTS.md').read_text(encoding='utf-8')
        for text in (self.readme,doc,agents):
            for term in ('Opta','Sofascore','temporada','competição'):
                self.assertIn(term.lower(),text.lower())
        self.assertIn('NÃO DISPONÍVEL',doc)
        self.assertIn('não contêm uma média Sofascore histórica auditada por temporada',agents)

if __name__=='__main__':
    unittest.main()
