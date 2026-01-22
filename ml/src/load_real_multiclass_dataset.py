from datasets import load_dataset
import csv
import random
from collections import Counter

print("⏳ Downloading LexGLUE ECHR dataset (real court judgments)...")

dataset = load_dataset("lex_glue", "ecthr_a", split="train")

output_file = "ml/data/raw/legal_dataset.csv"

data = []

for item in dataset:
    text = item["text"]
    labels = item["labels"]

    # Use only cases with exactly ONE main label (pure multi-class)
    if len(labels) != 1:
        continue

    label = f"Article_{labels[0]}"
    data.append([text, label])

print("Total usable samples:", len(data))

# Shuffle and limit size (for faster training, you can increase later)
random.shuffle(data)
data = data[:15000]   # 15,000 real legal documents

# Check class distribution
label_counts = Counter([row[1] for row in data])
print("Class distribution (top 10):", label_counts.most_common(10))

with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["text", "label"])
    writer.writerows(data)

print("✅ Real multi-class legal dataset saved to:")
print(output_file)
print("Total samples written:", len(data))
print("Total classes:", len(set([row[1] for row in data])))
