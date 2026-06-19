import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

def run_classification_pipeline():
    print("--- DecodeLabs AI Pipeline: Project 2 (Data Classification) ---\n")
    
    # 1. Load & Understand Dataset
    # Creating a dummy dataset: [Age, Estimated_Salary] -> Target: Purchased (0=No, 1=Yes)
    data = {
        'Age': [22, 25, 47, 52, 46, 56, 27, 32, 25, 38, 42, 60, 19, 29, 54, 21, 50, 33, 35, 48],
        'Estimated_Salary': [20000, 25000, 70000, 90000, 110000, 150000, 30000, 45000, 22000, 60000, 
                             75000, 140000, 180000, 35000, 120000, 15000, 85000, 52000, 65000, 95000],
        'Purchased': [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1]
    }
    
    df = pd.DataFrame(data)
    print("[STEP 1] Dataset Loaded Successfully!")
    print(df.head(), "\n") # Showing the first 5 rows
    
    # Features (X) and Target (y)
    X = df[['Age', 'Estimated_Salary']]
    y = df['Purchased']
    
    # 2. Structural Integrity: Split Data into Training & Testing Sets
    # 80% data for training and 20% for testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, shuffle=True)
    print(f"[STEP 2] Data Split Completed. Training samples: {len(X_train)}, Testing samples: {len(X_test)}")
    
    # Feature Scaling (StandardScaler as per DecodeLabs criteria: Mean=0, Variance=1)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    print("[STEP 2.1] Feature Scaling Applied to remove order bias.\n")
    
    # 3. Apply a Classification Algorithm
    # Using Logistic Regression for binary classification
    model = LogisticRegression()
    print("[STEP 3] Training the Classification Model (Logistic Regression)...")
    model.fit(X_train_scaled, y_train)
    print("Model Training Complete!\n")
    
    # 4. Model Testing & Validation
    y_pred = model.predict(X_test_scaled)
    
    # Calculate Quality Metrics
    accuracy = accuracy_score(y_test, y_pred)
    print("--- EVALUATION METRICS ---")
    print(f"Accuracy Score: {accuracy * 100:.2f}%")
    print("\nDetailed Classification Report:")
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    run_classification_pipeline()