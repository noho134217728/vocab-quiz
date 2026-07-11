import csv
import json

input_file = "words.csv"
output_file = "words.json"

words = []

with open(input_file, encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for i, row in enumerate(reader, start=1):
        aliases = row["aliases"].split(";") if row["aliases"].strip() else []

        words.append({
            "id": i,
            "answer": row["answer"].strip(),
            "ja_prompt": row["ja_prompt"].strip(),
            "pos": row["pos"].strip(),
            "aliases": [a.strip() for a in aliases],
            "hint": row["hint"].strip(),
            "example": row["example"].strip()
        })

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(words, f, ensure_ascii=False, indent=2)

print(f"{output_file} を作成しました。")