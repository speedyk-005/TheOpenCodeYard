#!/usr/bin/env python3
"""
contribute-scrapt

Determines the correct yard for a piece of code and scaffolds
the directory structure for contributing to The Open CodeYard.
"""

import argparse
import os
import sys
from pathlib import Path


YARDS = {
    "scraps": "Small utilities, snippets, one-off scripts (< ~200 lines, single file)",
    "prototypes": "Larger experiments, proof-of-concepts, multi-file projects",
}


def guess_yard(file_path: str, line_count: int = None) -> str:
    """
    Guess which yard a file belongs to based on size and complexity.
    """
    path = Path(file_path)
    if not path.exists():
        return "scraps"  # default for pasted code

    if line_count is None:
        try:
            with open(path) as f:
                line_count = sum(1 for _ in f)
        except Exception:
            line_count = 0

    if path.is_dir():
        file_count = sum(1 for _ in path.rglob("*") if _.is_file())
        if file_count > 3 or line_count > 300:
            return "prototypes"
        return "scraps"

    if line_count > 200:
        return "prototypes"
    return "scraps"


def scaffold(yard: str, username: str, project_name: str, output_base: Path) -> Path:
    """
    Create the directory structure for a new contribution.
    Returns the path to the created project directory.
    """
    project_dir = output_base / "yards" / yard / username / project_name
    project_dir.mkdir(parents=True, exist_ok=True)
    return project_dir


def main():
    parser = argparse.ArgumentParser(
        description="Scaffold a scrap or prototype contribution"
    )
    parser.add_argument("path", help="Path to the code file or directory")
    parser.add_argument("--username", default=os.environ.get("USER", "unknown"),
                        help="GitHub username (default: $USER)")
    parser.add_argument("--project", help="Project name (default: inferred from path)")
    parser.add_argument("--yard", choices=list(YARDS.keys()),
                        help="Force a specific yard (default: auto-detect)")
    parser.add_argument("--output", default=Path.cwd(),
                        type=Path, help="Repository root (default: cwd)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print what would be done without doing it")

    args = parser.parse_args()

    path = Path(args.path)
    if not path.exists():
        print(f"Error: {args.path} does not exist", file=sys.stderr)
        return 1

    # Detect yard
    yard = args.yard or guess_yard(str(path))

    # Infer project name
    project = args.project or path.name.lower().replace(" ", "-")

    # Scaffold
    project_dir = scaffold(yard, args.username, project, args.output)

    if args.dry_run:
        print(f"[DRY RUN] Would create: {project_dir}/")
        print(f"[DRY RUN] Yard: {yard}")
        print(f"[DRY RUN] Would copy {path} into project directory")
        return 0

    print(f"✓ Created {project_dir}/")
    print(f"  Yard: {yard}")
    print(f"  Project: {project}")
    print(f"\nNext: copy your code files into the project directory,")
    print(f"      write a README.md, and commit.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
