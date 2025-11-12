import subprocess
import os
import pandas as pd
import sys

# Ensure UTF-8 encoding
os.environ["PYTHONIOENCODING"] = "utf-8"

# Paths
DATA_DIR = os.path.join(os.getcwd(), "data")
DATA_COLLECTION_PATH = os.path.join(os.getcwd(), "data_collection")

# Check if data directory exists, create if not
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
    print(f"Created data directory: {DATA_DIR}")

# === Step 1: Run all data collection scripts ===
scripts = ["twitter_data.py", "newsapi_data.py", "reddit_data.py", "rss_data.py"]

print("Starting data collection pipeline...\n")

for script in scripts:
    script_path = os.path.join(DATA_COLLECTION_PATH, script)
    print(f"Running {script} ...")
    try:
        result = subprocess.run(
            ["python", script_path],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore"
        )
        print(f"Finished {script}\n")
        # Print any output from the script to help with debugging
        if result.stdout:
            print(f"Output from {script}:\n{result.stdout}\n")
        if result.stderr:
            print(f"Errors from {script}:\n{result.stderr}\n")
    except subprocess.CalledProcessError as e:
        print(f"Error while running {script}\n{e.stderr}\n")

print("All data collection scripts executed!\n")

# === Step 2: Merge all CSVs into one dataset ===
print("Merging all collected CSVs...\n")

# List all files in the data directory to debug
all_files = os.listdir(DATA_DIR)
print(f"All files in data directory: {all_files}")

# MODIFIED: Include the specific data files you're looking for
# This assumes your data collection scripts are creating these files
csv_files_to_merge = ["newsapi_data.csv", "reddit_data.csv", "rss_data.csv", "twitter_data.csv"]
csv_files = [f for f in all_files if f in csv_files_to_merge]

if not csv_files:
    print("No CSV files found in data folder. Exiting.")
    sys.exit()

print(f"Found {len(csv_files)} CSV files: {csv_files}\n")

dfs = []
for file in csv_files:
    file_path = os.path.join(DATA_DIR, file)
    try:
        df = pd.read_csv(file_path, encoding="utf-8")
        df["source_file"] = file  # track origin
        # Detect and combine available text columns
        text_cols = ["title", "description", "content", "text", "summary"]
        available_text_cols = [col for col in text_cols if col in df.columns]
        if available_text_cols:
            df["combined_text"] = df[available_text_cols].astype(str).agg(' '.join, axis=1)
        else:
            df["combined_text"] = pd.NA

        # Standardize timestamp column
        for ts_col in ["timestamp", "created_utc", "published"]:
            if ts_col in df.columns:
                df["timestamp"] = pd.to_datetime(df[ts_col], errors="coerce")
                break
        else:
            df["timestamp"] = pd.Timestamp.now()

        dfs.append(df)
        print(f"Loaded {file} ({len(df)} rows, {len(available_text_cols)} text columns combined)")
    except Exception as e:
        print(f"Error loading {file}: {e}")

# Concatenate all
if dfs:
    merged_df = pd.concat(dfs, ignore_index=True)
    merged_df.drop_duplicates(inplace=True)
    
    output_path = os.path.join(DATA_DIR, "merged_data.csv")
    merged_df.to_csv(output_path, index=False, encoding="utf-8")
    
    print(f"\nSuccessfully merged {len(csv_files)} files!")
    print(f"Saved merged dataset to: {output_path}")
    print(f"Total records after merging: {len(merged_df)}\n")
else:
    print("No dataframes to merge. Check if CSVs were created properly.")

print("Data merging pipeline completed successfully!")