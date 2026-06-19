# Project 2: Data Classification Using AI 📊

This repository contains a complete predictive AI pipeline built for **Project 2** of the **DecodeLabs Industrial Training Program (Batch: 2026)**.

## Project Goal
Transitioning from simple rule-based logic to Supervised Learning, this project demonstrates a complete machine learning pipeline that trains a model to recognize data patterns and categorize new information.

## Key Requirements Met
- **Data Engineering:** Managed features and labels using Pandas DataFrames.
- **Data Splitting:** Divided the dataset into training (80%) and testing (20%) sets with shuffling to prevent bias.
- **Feature Scaling:** Applied `StandardScaler` to normalize features (Mean=0, Variance=1).
- **Algorithmic Logic:** Implemented a binary classification algorithm (`LogisticRegression`).
- **Validation:** Measured performance using accuracy scores and classification metrics.

## 🛠️ How to Run
1. Install dependencies: `pip install numpy pandas scikit-learn`
2. Run the pipeline: `python classification.py`
3. View the classification report in terminal.