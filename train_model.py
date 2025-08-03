import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib

# Load dataset
data = pd.read_csv('ecommerce_customers.csv')

# Drop CustomerID
data = data.drop(columns=['CustomerID'])

# Encode Gender
le_gender = LabelEncoder()
data['Gender'] = le_gender.fit_transform(data['Gender'])  # Male=1, Female=0

# Features
X = data[['Gender', 'Age', 'Annual_Income', 'Spending_Score', 'Time_on_Site', 'Time_on_App', 'Membership_Years']]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train KMeans
kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(X_scaled)

# Save model, scaler, and encoder
joblib.dump(kmeans, 'kmeans_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(le_gender, 'gender_encoder.pkl')

print("K-Means model, scaler, and encoder saved.")
