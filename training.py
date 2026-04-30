import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# dataset
df = pd.read_csv("data/Final_Augmented_dataset_Diseases_and_Symptoms.csv")

# Cleaning Data
df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)

# Remove disease whuch have less than 5 sample
counts = df["diseases"].value_counts()
MIN_SAMPLES = 5
df = df[df["diseases"].isin(counts[counts >= MIN_SAMPLES].index)]

print(f"✅ Remaining diseases: {df['diseases'].nunique()}")

# Encoder
le = LabelEncoder()
df["diseases"] = le.fit_transform(df["diseases"])

# feature and target
X = df.drop("diseases", axis=1)
y = df["diseases"]

# train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Model (RandomForest)
model = RandomForestClassifier(
    n_estimators=150,
    max_depth=20,
    min_samples_split=4,
    min_samples_leaf=1,
    class_weight="balanced",
    random_state=42,
    n_jobs=1
)

print("\nTraining model...")
model.fit(X_train, y_train)

# Overall Accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"\nAccuracy: {round(accuracy * 100, 2)}%")

# Top 3 Accuracy of mmodel
probs = model.predict_proba(X_test)
top3 = np.argsort(probs, axis=1)[:, -3:]

correct = 0
for i, true_label in enumerate(y_test):
    if true_label in top3[i]:
        correct += 1

top3_accuracy = correct / len(y_test)

print(f"Top-3 Accuracy: {round(top3_accuracy * 100, 2)}%")

# Model training files
joblib.dump(model, "model.pkl")
joblib.dump(le, "label_encoder.pkl")
joblib.dump(list(X.columns), "features.pkl")

print("\nModel saved successfully!")
print("- model.pkl")
print("- label_encoder.pkl")
print("- features.pkl")
print(f"Total samples: {len(df)}")
print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")