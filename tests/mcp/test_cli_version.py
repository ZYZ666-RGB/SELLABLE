"""`sellable-mcp --version` prints the server version with no subcommand."""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

from mcp_server.server import SERVER_INFO

ROOT = Path(__file__).resolve().parents[2]


def test_version_flag_prints_server_info_with_no_subcommand(tmp_path):
    env = {**os.environ, "SELLABLE_HOME": str(tmp_path), "PYTHONPATH": str(ROOT)}
    result = subprocess.run(
        [sys.executable, "-m", "mcp_server.server", "--version"],
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == f"sellable-mcp {SERVER_INFO['version']}"
