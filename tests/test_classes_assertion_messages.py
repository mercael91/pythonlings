import ast
import pathlib


CHECKS_DIR = pathlib.Path(__file__).resolve().parent.parent / "checks" / "classes"
BATCH = ["classes7.py", "classes8.py", "classes9.py"]


def _asserts_without_msg(path):
    tree = ast.parse(path.read_text(encoding="utf-8"))
    missing = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assert) and node.msg is None:
            missing.append(node.lineno)
    return missing


def test_batch_asserts_have_messages():
    for name in BATCH:
        path = CHECKS_DIR / name
        assert path.exists(), f"missing check file: {path}"
        missing = _asserts_without_msg(path)
        assert not missing, f"{name} has asserts without messages at lines {missing}"
