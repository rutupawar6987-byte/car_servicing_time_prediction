import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset
data = pd.read_csv("dataset.csv")

# Map your features to match the CSV
data['Condition'] = data['Brake_Condition'].map({'Good': 8, 'Fair': 5, 'Poor': 2})  # Example numeric encoding
data['Spare_Parts_Availability'] = data['Failure_History']  # 1 if parts failed before
data['Staff_Experience'] = 5  # If unknown, you can assign a default
data['Spare_Parts_Type'] = 1  # 1=new, 0=own (assign default or from another source)
data['Year'] = data['Year_of_Manufacture']

# Features and target
features = ["Vehicle_Type", "Condition", "Spare_Parts_Availability",
            "Staff_Experience", "Spare_Parts_Type", "Year"]
target = "Downtime_Maintenance"

X = pd.get_dummies(data[features])
y = data[target]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Save model and columns
joblib.dump((model, X.columns), "rf_model.pkl")

print("✅ Model trained and saved successfully!")
