from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib
import pandas as pd

# Load the Iris dataset
data = load_iris()

# Create a DataFrame, where the columns are data.feature_names
df = _____
df["target"] = data.target

# Save the dataset to a CSV file, setting index to False
_____

print("Data saved to iris.csv")

# Load the dataset from the above CSV
df = _____

# Split the data into features and target. Features = everything BUT target
X = _____
y = _____

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

joblib.dump(scaler, "scaler.pkl")

print("Data processing complete")

# Train a Support Vector Machine model

# Create an instance of an SVC object, where kernel="linear"
model = _____

# run .fit() on the model, using the scaled train values and the y_train
model.fit(X_train_scaled, y_train)

# Make predictions on the test set, X_test_scaled
y_pred = _____

# Evaluate the model, using accuracy_score imported above. Compare y_test and y_pred
accuracy = _____
print(f"Model Accuracy: {accuracy:.2f}")

# Save the model
joblib.dump(model, "iris_model.pkl")
print("Model saved to iris_model.pkl")
