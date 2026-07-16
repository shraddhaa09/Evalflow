from pathlib import Path
import os
from collections import Counter

ROOT = Path(".")

print("=" * 70)
print("DATASET AUDIT REPORT")
print("=" * 70)

if not ROOT.exists():
    print("Dataset folder not found!")
    exit()

# -------------------------------
# Directory Structure
# -------------------------------

print("\nDIRECTORY STRUCTURE\n")

for root, dirs, files in os.walk(ROOT):
    level = root.replace(str(ROOT), "").count(os.sep)
    indent = "    " * level
    print(f"{indent}{Path(root).name}/")
    subindent = "    " * (level + 1)
    for f in files:
        print(f"{subindent}{f}")

# -------------------------------
# File Statistics
# -------------------------------

print("\nFILE STATISTICS\n")

extensions = Counter()
total_files = 0

for file in ROOT.rglob("*"):
    if file.is_file():
        total_files += 1
        extensions[file.suffix.lower()] += 1

print(f"Total Files : {total_files}")

print("\nFile Types:")

for ext, count in sorted(extensions.items()):
    print(f"{ext or '[no extension]'} : {count}")

# -------------------------------
# Folder Statistics
# -------------------------------

print("\nFOLDER STATISTICS\n")

for folder in ROOT.iterdir():
    if folder.is_dir():
        count = sum(1 for _ in folder.rglob("*") if _.is_file())
        print(f"{folder.name:<20} {count} files")

# -------------------------------
# Python Scripts
# -------------------------------

print("\nPYTHON SCRIPTS\n")

for py in ROOT.rglob("*.py"):
    print(py.relative_to(ROOT))

# -------------------------------
# Models
# -------------------------------

print("\nMODEL FILES\n")

for model in ROOT.rglob("*.pkl"):
    size = model.stat().st_size / (1024 * 1024)
    print(f"{model.name:<35} {size:.2f} MB")

print("\nAudit Complete.")