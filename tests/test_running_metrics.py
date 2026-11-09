import unittest
from src.pes21_method import ROOT

class TestRunningMetricsProtocol(unittest.TestCase):
    def test_sofascore_running_performance_is_first_class_source(self):
        docs = (ROOT/'docs/avaliacao-fisica.md').read_text(encoding='utf-8')
        agents = (ROOT/'AGENTS.md').read_text(encoding='utf-8')
        hist = (ROOT/'docs/coleta-historica.md').read_text(encoding='utf-8')
        for term in ('Desempenho de corrida','top_speed_kmh','sprints_per90','distance_km_per90','Nível A','aceleração'):
            self.assertIn(term,docs)
        self.assertIn('Sofascore',agents)
        self.assertIn('Desempenho de corrida',hist)
        self.assertIn('não associar'.lower(),docs.lower())
    def test_pace_not_identified_with_acceleration(self):
        doc=(ROOT/'docs/avaliacao-fisica.md').read_text(encoding='utf-8').lower()
        self.assertIn('não medem aceleração',doc)
        self.assertIn('não determina por si só um atributo pes',doc)

if __name__=='__main__': unittest.main()
