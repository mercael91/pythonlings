import ast
from pathlib import Path


CHECKS_DIR = Path(__file__).resolve().parent.parent / "checks" / "oop_advanced"


def test_check_lines_within_80_chars():
    for path in sorted(CHECKS_DIR.glob("oop_advanced*.py")):
        for lineno, line in enumerate(path.read_text().splitlines(), 1):
            assert len(line) <= 80, (
                "%s:%d exceeds 80 chars (%d)" % (path.name, lineno, len(line))
            )


def test_checks_parse():
    for path in sorted(CHECKS_DIR.glob("oop_advanced*.py")):
        ast.parse(path.read_text(), filename=str(path))
