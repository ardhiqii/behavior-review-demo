"""Run one JSON probe from the checkout under test."""

from __future__ import annotations

import importlib
import json
import sys
from pathlib import Path


def load_target(spec: str):
    module_path, _, function_name = spec.partition(":")
    module = importlib.import_module(module_path)
    return getattr(module, function_name)


def main(argv: list[str]) -> int:
    probe = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
    sys.path.insert(0, str(Path.cwd()))
    function = load_target(probe["target"])
    try:
        value = function(*probe["args"])
        payload = {"probe": probe["id"], "outcome": "value", "value": value}
    except Exception as exc:  # noqa: BLE001 - the probe records real failures
        payload = {
            "probe": probe["id"],
            "outcome": "exception",
            "error_type": type(exc).__name__,
            "error": str(exc),
        }
    print(json.dumps(payload, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
