import ast
from pathlib import Path

MODELS_DIR = Path("src/kwaixiaodian/models")


def iter_request_classes(py_path: Path):
    src = py_path.read_text(encoding="utf-8")
    tree = ast.parse(src)
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            # is subclass of BaseRequest
            is_request = any(
                (isinstance(b, ast.Name) and b.id == "BaseRequest")
                or (isinstance(b, ast.Attribute) and b.attr == "BaseRequest")
                for b in node.bases
            )
            if not is_request:
                continue
            # has literal api_method
            api_method = None
            for b in node.body:
                if isinstance(b, ast.FunctionDef) and b.name == "api_method":
                    for st in b.body:
                        if (
                            isinstance(st, ast.Return)
                            and isinstance(st.value, ast.Constant)
                            and isinstance(st.value.value, str)
                        ):
                            api_method = st.value.value
            yield node, api_method


def test_models_have_http_method_constant():
    # no exclusions expected; all request classes must declare class-level http_method
    exclude = set()

    failures = []
    for py_path in MODELS_DIR.glob("*.py"):
        if py_path.resolve() in exclude:
            continue
        for cls, api in iter_request_classes(py_path):
            # allow abstract/helper base requests that don't declare api_method
            if not api:
                continue
            has_ann_const = any(
                isinstance(b, ast.AnnAssign)
                and isinstance(b.target, ast.Name)
                and b.target.id == "http_method"
                for b in cls.body
            )
            if not has_ann_const:
                failures.append((str(py_path), cls.name, api))

    assert not failures, (
        f"Missing http_method constant in: {failures[:10]} (showing up to 10)"
    )
