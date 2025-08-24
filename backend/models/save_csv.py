import csv

def save_records_to_csv(records: list[dict], original_path: Path, input_root: Path, output_root: Path):
    relative_path = original_path.relative_to(input_root).with_suffix(".csv")
    output_path = output_root / relative_path
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "level", "number", "text"])
        writer.writeheader()
        writer.writerows(records)