import unittest
from src.pes21_method import ROOT

class TestRepositoryDocumentation(unittest.TestCase):
    def test_canonical_repository_and_versions(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        guide = (ROOT / "docs/publicacao-github.md").read_text(encoding="utf-8")
        for text in (readme, agents, guide):
            self.assertIn("ptamay/mpes-criterios-overall", text)
        self.assertIn("v1.10", readme)
        self.assertIn("fórmula-base", readme.lower())
        self.assertIn("config/criteria.v1.json", guide)

    def test_publishing_scripts_target_existing_repo(self):
        for path in ("scripts/publicar-github.ps1", "scripts/publicar-github.sh"):
            content = (ROOT / path).read_text(encoding="utf-8")
            self.assertIn("ptamay/mpes-criterios-overall", content)
            self.assertNotIn("ptamay/pes21-criterios-overall", content)
            self.assertNotIn("gh repo create", content)
            self.assertNotIn("--force", content.replace("force-push", ""))
            self.assertIn("git push origin main", content)

    def test_multi_ai_entrypoints_share_agents(self):
        claude = (ROOT / "CLAUDE.md").read_text(encoding="utf-8")
        gemini = (ROOT / "GEMINI.md").read_text(encoding="utf-8")
        tutorial = (ROOT / "docs/uso-gemini.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("@AGENTS.md", claude)
        self.assertIn("@./AGENTS.md", gemini)
        for path in ("CLAUDE.md", "GEMINI.md", "docs/uso-gemini.md"):
            self.assertIn(path, readme)
        self.assertIn("Importar código", tutorial)
        self.assertIn("não", tutorial.lower())
        for file in (claude, gemini):
            self.assertIn("ptamay/mpes-criterios-overall", file if "ptamay/" in file else (ROOT / "AGENTS.md").read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
