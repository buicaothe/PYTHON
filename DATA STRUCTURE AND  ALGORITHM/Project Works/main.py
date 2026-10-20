"""Command-line entry point for the DSA project scenarios.

Usage:
    python main.py                 # run every scenario
    python main.py --scenario all  # same as default
    python main.py --scenario dynamic_array_grades
"""

from __future__ import annotations

import argparse
import importlib
import os
import sys
import pkgutil

# Allow running this file from anywhere inside the project root by inserting
# the project root (this file's parent directory) onto sys.path so that
# ``from src.dsa...`` imports resolve.
_PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)


SCENARIO_DIR = os.path.join(_PROJECT_ROOT, "scenarios")


def list_scenarios() -> list[str]:
    """Return the sorted names of the runnable scenario modules."""
    names: list[str] = []
    for _finder, name, _is_pkg in pkgutil.iter_modules([SCENARIO_DIR]):
        if not name.startswith("_"):
            names.append(name)
    return sorted(names)


def run_scenario(name: str) -> int:
    """Import and run the scenario module named ``name``; return exit code."""
    module = importlib.import_module(f"scenarios.{name}")
    main_fn = getattr(module, "main", None)
    if main_fn is None:
        print(f"scenario {name!r} has no main()", file=sys.stderr)
        return 1
    print(f"\n===== scenario: {name} =====")
    main_fn()
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run DSA project scenarios.")
    parser.add_argument(
        "--scenario",
        default="all",
        help="Scenario name, or 'all' to run every scenario (default: all).",
    )
    args = parser.parse_args(argv)

    if args.scenario == "all":
        scenarios = list_scenarios()
    else:
        scenarios = [args.scenario]

    if not scenarios:
        print("No scenarios found.", file=sys.stderr)
        return 1

    exit_code = 0
    for name in scenarios:
        code = run_scenario(name)
        if code != 0:
            exit_code = code
    print()
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())