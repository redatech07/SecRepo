import subprocess
from pathlib import Path


def get_git_root(directory):

    try:
        result = subprocess.run(["git", "-C", str(directory), "rev-parse", "--show-toplevel"], capture_output=True, text=True)

    except FileNotFoundError:
        raise RuntimeError("Git is not installed or not available")

    if result.returncode != 0:
        return None

    return Path(result.stdout.strip())

def get_tracked_files(directory):

    result = subprocess.run(["git", "-C", str(directory), "ls-files"], capture_output=True, text=True)

    if result.returncode != 0:
        return []

    files = result.stdout.splitlines()

    return files

def get_untracked_files(directory):

    result = subprocess.run(["git", "-C", str(directory), "ls-files", "--others", "--exclude-standard"], capture_output=True, text=True)

    if result.returncode != 0:
        return []

    files = result.stdout.splitlines()

    return files

def get_ignored_files(directory):

    result = subprocess.run(["git", "-C", str(directory), "ls-files", "--others","--ignored", "--exclude-standard"], capture_output=True, text=True)

    if result.returncode != 0:
        return []

    files = result.stdout.splitlines()

    return files