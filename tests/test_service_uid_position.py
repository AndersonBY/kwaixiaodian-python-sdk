import importlib
import inspect
import pkgutil

import pytest


def iter_service_classes():
    pkg = importlib.import_module("kwaixiaodian.client.services")
    for modinfo in pkgutil.iter_modules(pkg.__path__, pkg.__name__ + "."):
        mod = importlib.import_module(modinfo.name)
        for name, obj in inspect.getmembers(mod, inspect.isclass):
            # Heuristic: public service classes end with 'Service'
            if name.endswith("Service") and obj.__module__ == mod.__name__:
                yield obj


@pytest.mark.unit
def test_uid_is_last_optional_parameter_in_services():
    failures = []
    found_any = False
    for cls in iter_service_classes():
        for name, member in inspect.getmembers(cls, inspect.isfunction):
            if name.startswith("_"):
                continue
            sig = inspect.signature(member)
            params = list(sig.parameters.values())
            # instance methods should have 'self' first; tolerate otherwise
            start_idx = 1 if params and params[0].name == "self" else 0
            # find uid if present
            uid_indices = [
                i
                for i, p in enumerate(params[start_idx:], start=start_idx)
                if p.name == "uid"
            ]
            if not uid_indices:
                continue
            found_any = True
            uid_idx = uid_indices[0]
            uid_param = params[uid_idx]
            # uid must be last declared parameter (ignoring *args/**kwargs if any)
            # find last positional-or-keyword/keyword-only parameter index
            last_index = max(
                (
                    i
                    for i, p in enumerate(params)
                    if p.kind in (p.POSITIONAL_OR_KEYWORD, p.KEYWORD_ONLY)
                ),
                default=len(params) - 1,
            )
            if uid_idx != last_index:
                failures.append(
                    f"{cls.__module__}.{cls.__name__}.{name} -> uid not last"
                )
                continue
            # uid must be optional (default None)
            if uid_param.default is not None:
                failures.append(
                    f"{cls.__module__}.{cls.__name__}.{name} -> uid default not None"
                )

    assert found_any, "No service methods with uid parameter found"
    assert not failures, "\n" + "\n".join(failures)
