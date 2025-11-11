Overview

The models/ folder is the brain of your project.
It stores all the pre-trained machine learning assets that actually decide whether a piece of text is disaster-related or not and what type of disaster it belongs to.

Think of it like your “control center”: the cleaned data comes in from model.build/, and these models analyze it to generate predictions.

Key Points

Holds pre-trained ML model(s) and vectorizer(s)

Used by hypomodel.ipynb to classify data from cleaned_dataset.csv

Supports multi-class disaster classification

No raw data stored here – only models (learned weights) and vectorizers (text transformers)

Files Overview

disaster_classifier5.pkl

Type: Logistic Regression model (multi-class)

Purpose: Classifies text into disaster types (Flood, Storm, Earthquake, etc.)

Trained on: clean_disaster_text_dataset.csv (Kaggle disaster tweets dataset)

Performance: ~96% accuracy

disaster_vectorizer3.pkl

Type: TfidfVectorizer (text to numerical features)

Purpose: Converts cleaned text into numerical vectors that the ML model can process

Parameters: max_features=5000, ngram_range=(1,2)

Used in combination with: disaster_classifier5.pkl

Flow

cleaned_dataset.csv → vectorizer → model → disaster type prediction + confidence

Optional keyword assist: Model predictions are boosted or flagged if certain disaster-related keywords exist.

Output: final_disaster_data.csv (saved in data/)

Summary
models/ = prediction engine storage

Input: Preprocessed & cleaned text (clean_text)

Output: Disaster type, confidence score, reason (model or keyword)

Main files:

disaster_classifier5.pkl → ML model

disaster_vectorizer3.pkl → Text vectorizer
