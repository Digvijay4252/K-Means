<!-- # K-Means

<img width="1592" height="917" alt="image" src="https://github.com/user-attachments/assets/772e5d10-dac3-41e8-b5be-52d833d4d232" /> -->

## Customer Cluster Predictor – K-Means Clustering

This project uses K-Means Clustering to segment customers into different behavioral clusters based on factors like income, spending score, and digital interaction patterns. A user-friendly Flask web application allows businesses to explore customer clusters and optimize marketing strategies.

---

## What is K-Means?
K-Means is an unsupervised learning algorithm that groups data into K distinct clusters based on similarity. It’s widely used in market segmentation, customer profiling, and recommendation systems.

---

##  Project Structure
```
K-Means/
├── app.py               # Flask app for prediction
├── train_model.py       # K-Means training script
├── model.pkl            # Trained KMeans model
├── encoders.pkl         # Encoded label mappings
├── customer_data.csv    # Dataset for training
│
├── templates/
    └── index.html       # Web UI form

```
---

##  Setup Instructions

1. **Clone the repository**

```
git clone https://github.com/Digvijay4252/K-Means.git
cd K-Means
```
Install dependencies
```
pip install -r requirements.txt
```
Run the application
```
python app.py
```
Open in browser

Visit: http://localhost:10000

# Sample Input
```
Gender: Male
Age: 29
Income: $50,000
Spending Score: 82
Time on Site: 50 mins
Time on App: 30 mins
Membership: 3 years
```
## Screenshots

### Step 1
<img width="1870" height="910" alt="image" src="https://github.com/user-attachments/assets/307ff196-f0b0-41ed-883f-0fca1f2dc65c" />

### Step 2
<img width="1869" height="913" alt="image" src="https://github.com/user-attachments/assets/62ed03b2-459c-40ba-8ce8-3b99e44fdc5d" />

### Step 3
<img width="1877" height="909" alt="image" src="https://github.com/user-attachments/assets/b5242925-7502-46ba-ac7d-f5f4fda442a5" />



## Future Improvements
Auto-optimize cluster count (K) using silhouette score

Add user analytics dashboard

Export cluster reports

Integrate database support
