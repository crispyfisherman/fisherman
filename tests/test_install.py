from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name) / "skills repo"
        shutil.copytree(ROOT, self.repo, ignore=shutil.ignore_patterns(".git", ".generated", "__pycache__", ".trial-output"))
        self.home = Path(self.temp.name) / "user home"

    def run_installer(self, *args):
        return subprocess.run([sys.executable, str(self.repo / "scripts/install.py"), "--home", str(self.home), *args], capture_output=True, text=True)

    def test_both_hosts_can_discover_skills_and_uninstall_preserves_neighbors(self):
        neighbor = self.home / ".claude/skills/existing-skill/SKILL.md"
        neighbor.parent.mkdir(parents=True)
        neighbor.write_text("original")
        result = self.run_installer()
        self.assertEqual(result.returncode, 0, result.stderr)
        for skill in (self.repo / "skills").iterdir():
            for folder in (".agents/skills", ".claude/skills"):
                installed = self.home / folder / skill.name
                self.assertTrue(installed.is_symlink())
                self.assertTrue((installed / "SKILL.md").is_file())
                for resource in (skill / "references").iterdir():
                    self.assertEqual((installed / "references" / resource.name).read_bytes(), resource.read_bytes())
        review = (self.home / ".claude/skills/peh-review/SKILL.md").read_text()
        for value in ("context: fork", "agent: general-purpose", "background: false", "effort: high", "$ARGUMENTS"):
            self.assertIn(value, review)
        self.assertNotIn("context: fork", (self.home / ".claude/skills/peh-correct/SKILL.md").read_text())
        self.assertEqual(self.run_installer().returncode, 0)
        self.assertEqual(self.run_installer("--uninstall").returncode, 0)
        self.assertEqual(neighbor.read_text(), "original")
        self.assertFalse((self.home / ".agents/skills/peh-review").exists())

    def test_collision_fails_before_installing_other_skills(self):
        conflict = self.home / ".agents/skills/peh-review/SKILL.md"
        conflict.parent.mkdir(parents=True)
        conflict.write_text("my custom review")
        result = self.run_installer()
        self.assertEqual(result.returncode, 2)
        self.assertEqual(conflict.read_text(), "my custom review")
        self.assertFalse((self.home / ".agents/skills/peh-correct").exists())
        self.assertFalse((self.repo / ".generated").exists())

    def test_dry_run_makes_no_directories(self):
        result = self.run_installer("--dry-run")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(self.home.exists())
        self.assertFalse((self.repo / ".generated").exists())

    def test_standalone_selection_does_not_require_sibling_skills(self):
        result = self.run_installer("--target", "claude", "--skills", "peh-trace-system")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.home / ".claude/skills/peh-trace-system/references/study.md").is_file())
        self.assertFalse((self.home / ".agents").exists())
        self.assertEqual(len(list((self.home / ".claude/skills").iterdir())), 1)

    def test_reinstall_refreshes_generated_instruction_content(self):
        self.assertEqual(self.run_installer("--target", "claude").returncode, 0)
        source = self.repo / "skills/peh-review/SKILL.md"
        source.write_text(source.read_text() + "\nA new evidence requirement.\n")
        self.assertEqual(self.run_installer("--target", "claude").returncode, 0)
        self.assertIn("A new evidence requirement.", (self.home / ".claude/skills/peh-review/SKILL.md").read_text())


if __name__ == "__main__":
    unittest.main()
