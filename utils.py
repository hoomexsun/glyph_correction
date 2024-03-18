import csv
import json
from pathlib import Path


def create_wordmap(content: str, output: str, wordmap_path: str | Path):
    wordmap = {
        word: transliterated
        for word, transliterated in zip(content.split("\n"), output.split("\n"))
    }

    # Save in txt format
    txt_path = Path(wordmap_path).with_suffix(".txt")
    txt_path.write_text(
        "\n".join([f"{word}\t{corrected}" for word, corrected in wordmap.items()]),
        encoding="utf-8",
    )

    # Save in json format
    json_path = Path(wordmap_path).with_suffix(".json")
    json_path.write_text(json.dumps(wordmap, ensure_ascii=False), encoding="utf-8")

    # Save in csv format
    csv_path = Path(wordmap_path).with_suffix(".csv")
    with csv_path.open(mode="w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=("s550", "bn"))
        writer.writeheader()
        for word_s550, word_bn in wordmap.items():
            writer.writerow({"s550": word_s550, "bn": word_bn})
