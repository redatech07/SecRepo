import json
from pathlib import Path


def export_report(report_data, output_dir="reports"):

    output_dir = Path(output_dir)
    report_path = output_dir / "secrepo_report.json"

    try:
        with open(report_path, "w", encoding="utf-8") as file:
            json.dump(report_data, file, indent=4, ensure_ascii=False)

    except OSError:
        return None

    return report_path