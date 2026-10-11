import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / "skills/peh-correct/scripts/local_workspace.py"


class WorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name)
        self.repo = self.path / "company code"
        self.repo.mkdir()
        subprocess.run(["git", "init", str(self.repo)], check=True, capture_output=True)

    def helper(self, repo=None, *args):
        return subprocess.run([sys.executable, str(HELPER), "--repo", str(repo or self.repo), *args], capture_output=True, text=True)

    def test_local_workspace_does_not_write_target(self):
        before = subprocess.run(["git", "-C", str(self.repo), "status", "--porcelain=v1"], capture_output=True, text=True, check=True).stdout
        result = self.helper(None, "--base-dir", str(self.path / "personal"), "--create")
        self.assertEqual(result.returncode, 0, result.stderr)
        output = json.loads(result.stdout)
        workspace = Path(output["workspace"])
        self.assertTrue(workspace.is_dir())
        self.assertNotIn(self.repo, workspace.parents)
        after = subprocess.run(["git", "-C", str(self.repo), "status", "--porcelain=v1"], capture_output=True, text=True, check=True).stdout
        self.assertEqual(before, after)

    def test_rejects_direct_and_symlink_paths_inside_target(self):
        direct = self.helper(None, "--base-dir", str(self.repo / "ignored-personal"), "--create")
        self.assertEqual(direct.returncode, 2)
        alias = self.path / "outside-link"
        alias.symlink_to(self.repo, target_is_directory=True)
        indirect = self.helper(None, "--base-dir", str(alias / "rules"), "--create")
        self.assertEqual(indirect.returncode, 2)
        self.assertFalse((self.repo / "rules").exists())

    def test_subfolder_and_symlink_resolve_to_same_project(self):
        folder = self.repo / "src"
        folder.mkdir()
        alias = self.path / "repo-alias"
        alias.symlink_to(self.repo, target_is_directory=True)
        base = str(self.path / "personal")
        keys = [json.loads(self.helper(repo, "--base-dir", base).stdout)["project_key"] for repo in (self.repo, folder, alias)]
        self.assertEqual(len(set(keys)), 1)
        self.assertFalse((self.path / "personal").exists())

    def test_different_same_named_repositories_do_not_share_state(self):
        other = self.path / "second/company code"
        other.mkdir(parents=True)
        subprocess.run(["git", "init", str(other)], check=True, capture_output=True)
        base = str(self.path / "personal")
        first = json.loads(self.helper(None, "--base-dir", base).stdout)["workspace"]
        second = json.loads(self.helper(other, "--base-dir", base).stdout)["workspace"]
        self.assertNotEqual(first, second)


if __name__ == "__main__":
    unittest.main()
