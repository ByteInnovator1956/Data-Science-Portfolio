import pandas as pd
import re
import os
import subprocess
import spacy
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

# === 0 Run main_data_pipeline.py to fetch + merge data ===
print("Running main_data_pipeline.py to collect and merge all data...\n")
try:
    subprocess.run(["python", "main_data_pipeline.py"], check=True)
    print("main_data_pipeline.py executed successfully!\n")
except subprocess.CalledProcessError as e:
    raise RuntimeError(f"Error while running main_data_pipeline.py: {e}")

# === 1 Load merged dataset ===
merged_file_path = os.path.join("data", "merged_data.csv")
if not os.path.exists(merged_file_path):
    raise FileNotFoundError(f"Merged dataset not found at {merged_file_path}. Ensure main_data_pipeline.py works properly.")

df = pd.read_csv(merged_file_path, encoding='utf-8', engine='python')
print("Merged dataset loaded successfully!")
print("Initial shape:", df.shape)

# === 2 Detect timestamp column ===
possible_timestamp_cols = ['timestamp', 'created_utc', 'published', 'date']
timestamp_col = None
for col in possible_timestamp_cols:
    if col in df.columns:
        timestamp_col = col
        break

if not timestamp_col:
    print("No timestamp column found. Adding default index-based timestamp.")
    df['timestamp'] = pd.date_range(end=pd.Timestamp.now(), periods=len(df))
    timestamp_col = 'timestamp'

# === 3 Combine text columns ===
text_columns = ['title', 'description', 'content', 'text', 'summary']
available_text_cols = [col for col in text_columns if col in df.columns]
if not available_text_cols:
    raise ValueError("No suitable text columns found to combine!")

df['combined_text'] = df[available_text_cols].astype(str).agg(' '.join, axis=1)

# Drop empty or invalid rows
df['combined_text'] = df['combined_text'].replace(r'^(nan\s?)+$', pd.NA, regex=True)
df.dropna(subset=['combined_text'], inplace=True)
df = df[df['combined_text'].str.strip() != '']
print("Combined text column created successfully!")

# === 4 Clean text ===
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'http\S+|www.\S+', '', text)  # remove URLs
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)   # remove special chars
    text = re.sub(r'\s+', ' ', text).strip()     # remove extra spaces
    return text

df['clean_text'] = df['combined_text'].apply(clean_text)
print("Text cleaning completed!")

# === 5 NEW: Extract locations using spaCy ===
print("Loading spaCy model for location extraction...")
try:
    nlp = spacy.load("en_core_web_sm")
    
    def extract_location(text):
        doc = nlp(text[:100000] if len(text) > 100000 else text)  # Limit text length to avoid memory issues
        locations = [ent.text for ent in doc.ents if ent.label_ in ["GPE", "LOC", "FAC"]]
        return ", ".join(set(locations)) if locations else "Unknown"
    
    print("Extracting locations from text...")
    # Use original combined_text instead of clean_text to preserve proper nouns
    df['location'] = df['combined_text'].apply(extract_location)
    print("Location extraction completed!")
except Exception as e:
    print(f"Warning: Location extraction failed - {str(e)}")
    print("Creating empty location column instead.")
    df['location'] = "Unknown"

# === 6 Sort by timestamp ===
df[timestamp_col] = pd.to_datetime(df[timestamp_col], errors='coerce')
df = df.sort_values(by=timestamp_col, ascending=False)
print(f"Data sorted by timestamp ({timestamp_col}) - latest first!")

# === 7 Keep relevant columns ===
final_columns = ['source', timestamp_col, 'clean_text', 'location']
available_cols = [col for col in final_columns if col in df.columns]
final_df = df[available_cols]
print("Columns filtered and arranged!")

# === 8 Save cleaned dataset ===
cleaned_file_path = os.path.join("data", "cleaned_dataset.csv")
final_df.to_csv(cleaned_file_path, index=False)
print(f"Cleaned dataset saved as {cleaned_file_path}")
print("Final shape:", final_df.shape)
print("Cleaning process completed successfully!")