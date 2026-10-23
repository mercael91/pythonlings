import ast
from pathlib import Path


CHECKS_DIR = Path(__file__).resolve().parent.parent / "checks" / "functional"


def _asserts_without_message(path):
    tree = ast.parse(path.read_text(encoding="utf-8"))
    missing = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assert) and node.msg is None:
            missing.append(node.lineno)
    return missing


def test_functional7_asserts_have_messages():
    path = CHECKS_DIR / "functional7.py"
    assert _asserts_without_message(path) == []


def test_functional8_asserts_have_messages():
    path = CHECKS_DIR / "functional8.py"
    assert _asserts_without_message(path) == []
