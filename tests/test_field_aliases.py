import importlib
import inspect
import pkgutil

import pytest

import kwaixiaodian.models as models_pkg
from kwaixiaodian.models.base import BaseRequest


def iter_model_modules():
    for mod in pkgutil.iter_modules(models_pkg.__path__, models_pkg.__name__ + "."):
        name = mod.name
        # include all model modules
        yield importlib.import_module(name)


@pytest.mark.unit
def test_all_request_fields_have_aliases():
    exclusions = {
        "access_token",
        "uid",
        "api_version",
        "param",
        "api_method",
        "http_method",
    }

    failures = []
    found_any = False
    for mod in iter_model_modules():
        for _, obj in inspect.getmembers(mod, inspect.isclass):
            if obj is BaseRequest or not issubclass(obj, BaseRequest):
                continue
            found_any = True
            fields = getattr(obj, "model_fields", {})
            for fname, finfo in fields.items():
                if fname in exclusions:
                    continue
                if finfo.alias is None:
                    failures.append(
                        f"{mod.__name__}.{obj.__name__}.{fname} missing alias"
                    )

    assert found_any, "No BaseRequest subclasses discovered in models package"
    assert not failures, "\n" + "\n".join(failures)
