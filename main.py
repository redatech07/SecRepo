import argparse
from pathlib import Path

from modules.scanner import scan_repository
from modules.file_checker import read_file
from modules.secret_checker import detect_keyword_secrets
from modules.git_checker import (get_git_root, get_tracked_files, get_untracked_files, get_ignored_files)
from modules.reporter import export_report


def get_args():

    parser = argparse.ArgumentParser(description="SecRepo - Security Scanner")
    parser.add_argument("-d", "--directory", type=str, required=True, help="Target directory")

    return parser.parse_args()


args = get_args()
target_d = args.directory

print("\n" + "=" * 55)
print("                       SECREPO")
print("             Local Repository Security Auditor")
print("=" * 55)


all_files = scan_repository(target_d)

findings_list = []
readable_files = 0

for file in all_files:

    content = read_file(file)

    if content is None:
        continue

    readable_files += 1

    findings = detect_keyword_secrets(content)

    for finding in findings:

        findings_list.append({
            "file": str(file),
            "line": finding["line"],
            "type": finding["type"],
            "keyword": finding["keyword"]
        })


print("\n[1] SCAN SUMMARY")
print("-" * 55)

print(f"Target directory : {target_d}")
print(f"Files discovered : {len(all_files)}")
print(f"Files readable   : {readable_files}")
print(f"Secrets detected : {len(findings_list)}")


print("\n[2] SECRET DETECTION")
print("-" * 55)

if findings_list:

    for finding in findings_list:

        print(
            f"[!] {finding['file']} | "
            f"Line: {finding['line']} | "
            f"Type: {finding['type']} | "
            f"Keyword: {finding['keyword']}"
        )

else:
    print("No potential secrets detected.")


print("\n[3] GIT ANALYSIS")
print("-" * 55)

git_root = get_git_root(target_d)
git_results = []

if git_root:

    print(f"Git repository : {git_root}")

    tracked_files = get_tracked_files(git_root)
    untracked_files = get_untracked_files(git_root)
    ignored_files = get_ignored_files(git_root)

    for file in all_files:

        absolute_path = (Path.cwd() / file).resolve()

        try:
            relative_path = absolute_path.relative_to(git_root).as_posix()

        except ValueError:
            git_status = "OUTSIDE_GIT"
            display_path = str(file)

        else:
            display_path = relative_path

            if relative_path in tracked_files:
                git_status = "TRACKED"
            elif relative_path in untracked_files:
                git_status = "UNTRACKED"
            elif relative_path in ignored_files:
                git_status = "IGNORED"
            else:
                git_status = "UNKNOWN"

        git_results.append({
            "file": display_path,
            "status": git_status
        })

    print(f"Tracked files   : {len(tracked_files)}")
    print(f"Untracked files : {len(untracked_files)}")
    print(f"Ignored files   : {len(ignored_files)}")

    print("\n[4] FILE STATUS")
    print("-" * 55)

    for result in git_results:
        print(f"{result['file']:<40} | {result['status']}")

else:
    print("Target is not inside a Git repository.")


print("\n[5] REPORT")
print("-" * 55)

report_data = {
    "project": "SecRepo",
    "target_directory": str(target_d),
    "files_scanned": len(all_files),
    "files_readable": readable_files,
    "secrets_detected": len(findings_list),
    "findings": findings_list,
    "git_repository": str(git_root) if git_root else None,
    "git_results": git_results
}

report_path = export_report(report_data)

if report_path:
    print("JSON report generated successfully.")
    print(f"Report location : {report_path}")
else:
    print("Failed to generate JSON report.")


print("\n" + "=" * 55)
print("                    SCAN COMPLETED")
print("=" * 55)