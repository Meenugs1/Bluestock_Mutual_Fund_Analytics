import pandas as pd
import os
import glob

files = glob.glob("data/raw/*.csv")

cleaned_files = glob.glob("data/processed/*.csv")

print("\n========== RAW DATASETS ==========\n")

for file in files:
    df = pd.read_csv(file)

    print(f"\nFile: {os.path.basename(file)}")
    print(f"Shape: {df.shape}")
    print("Columns:")
    print(df.columns.tolist())

print("\n========== CLEANED DATASETS ==========\n")

for file in cleaned_files:
    df = pd.read_csv(file)

    print(f"\nFile: {os.path.basename(file)}")
    print(f"Shape: {df.shape}")
    print("Columns:")
    print(df.columns.tolist())