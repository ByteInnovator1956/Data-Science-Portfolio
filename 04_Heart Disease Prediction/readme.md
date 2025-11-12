Heart Disease Prediction



Overview

This project predicts the likelihood of a person having heart disease based on health-related attributes such as blood pressure, cholesterol, BMI, smoking habits, and lifestyle factors. It combines data analysis and machine learning to identify key risk factors and build an accurate predictive model.

Role: Data Analyst / Machine Learning Practitioner

Dataset

File: heartdisease_u5z_lx9fv.csv

Key Columns:

HeartDiseaseorAttack (target variable)

HighBP, HighChol, BMI, Smoker, Diabetes

Fruits, Veggies, HvyAlcoholConsump

MentHlth, PhysHlth

Sex, Age, Education, Income

Tools & Libraries

Python

Pandas, NumPy: Data loading, cleaning, and transformation

Matplotlib, Seaborn: Visualization and exploratory data analysis

Scikit-learn: Model building and evaluation (Logistic Regression, Decision Tree, Random Forest, SVM)

Workflow
1. Data Loading & Cleaning

Loaded CSV with proper encoding

Checked for missing values and duplicates

Examined class imbalance in the target variable

Verified dataset columns

2. Exploratory Data Analysis (EDA)

Analyzed correlations between risk factors and heart disease

Visualized distributions of numeric features like BMI, Age, and Blood Pressure

Compared disease prevalence across genders, age groups, and income levels

Identified class imbalance in the target variable

3. Feature Engineering

Encoded categorical variables: Sex, Smoker, Diabetes

Normalized numeric features as needed

Created derived features combining lifestyle and health indicators

4. Model Building

Split dataset into training and test sets

Trained multiple models:

Logistic Regression

Decision Tree Classifier

Random Forest

Support Vector Machine (SVM)

Evaluated models using:

Accuracy, Precision, Recall, F1-score, ROC-AUC

5. Model Evaluation & Selection

Compared model performances to select the best one

Used confusion matrix to visualize predictions and misclassifications

Key Insights

High blood pressure and high cholesterol are the strongest predictors of heart disease

Smoking and heavy alcohol consumption significantly increase risk

Healthy diet (fruits and vegetables) reduces the likelihood of heart disease

Age and BMI positively correlate with heart disease risk

Education and income levels influence prevalence, reflecting lifestyle and awareness factors

The final ML model achieved high recall, effectively identifying most at-risk individuals, which is crucial for medical use cases
