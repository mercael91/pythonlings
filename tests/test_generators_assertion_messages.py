import ast
import pathlib


CHECKS = [
    "checks/generators/generators1.py",
    "checks/generators/generators3.py",
    "checks/generators/generators6.py",
]


def _asserts_without_message(path):
    tree = ast.parse(pathlib.Path(path).read_text())
    missing = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assert) and node.msg is None:
            missing.append(node.lineno)
    return missing


def test_generators_checks_have_actionable_assertion_messages():
    for path in CHECKS:
        missing = _asserts_without_message(path)
        assert missing == [], f"{path} has asserts without messages at lines {missing}"
