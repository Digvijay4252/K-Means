from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# Load model and encoders
model = joblib.load('kmeans_model.pkl')
scaler = joblib.load('scaler.pkl')
gender_encoder = joblib.load('gender_encoder.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    cluster = None
    if request.method == 'POST':
        try:
            gender = request.form['gender']
            age = int(request.form['age'])
            income = float(request.form['income'])
            score = float(request.form['score'])
            site_time = float(request.form['site_time'])
            app_time = float(request.form['app_time'])
            membership = int(request.form['membership'])

            gender_encoded = gender_encoder.transform([gender])[0]
            features = [[gender_encoded, age, income, score, site_time, app_time, membership]]
            scaled_features = scaler.transform(features)
            cluster = int(model.predict(scaled_features)[0])

        except Exception as e:
            cluster = f"Error: {e}"

    return render_template('index.html', cluster=cluster)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
