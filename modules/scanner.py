import os
from pathlib import Path

def should_scan_file(target_d, max_size = 5 * 1024 * 1024):

    try:
        if target_d.stat().st_size > max_size:
            return False
    except OSError:
        return False

    return True


def scan_repository(target_d):
    root = Path(target_d)

    if not root.exists():
        raise FileNotFoundError("Directory does not exist")

    if not root.is_dir():
        raise NotADirectoryError("The path is not a directory")

    all_files = []

    ignored_dirs = {
    # Version control internals
    ".git",
    ".svn",
    ".hg",

    # Python
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".tox",
    ".nox",
    ".hypothesis",

    # JavaScript / TypeScript
    "node_modules",

    # Java / Kotlin / Scala
    ".gradle",

    # C / C++
    "CMakeFiles",

    # Swift / Apple
    "DerivedData",
    "Carthage",

    # R
    ".Rproj.user",

    # Linux
    "lost+found",
    }

    ignored_files = {
    # macOS
    ".DS_Store",
    "._.DS_Store",

    # Windows
    "Thumbs.db",
    "ehthumbs.db",
    "desktop.ini",

    "README.md",
    }

    for current_root, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in ignored_dirs]
        for file in files:
            if file in ignored_files:
                continue
            file_path = Path(current_root) / file

            if should_scan_file(file_path):
                all_files.append(file_path)

    return all_files