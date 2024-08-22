from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib
import pandas as pd

# Load the Iris dataset
data = load_iris()

# Create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df["target"] = data.target

# Save the dataset to a CSV file
df.to_csv("iris.csv", index=False)

print("Data saved to iris.csv")

# Load the dataset
df = pd.read_csv("iris.csv")

# Split the data into features and target
X = df.drop("target", axis=1)
y = df["target"]

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
model = SVC(kernel="linear")
model.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test_scaled)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save the model
joblib.dump(model, "iris_model.pkl")
print("Model saved to iris_model.pkl")
