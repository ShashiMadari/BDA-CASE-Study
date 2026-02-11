from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import joblib
import pandas as pd
from collections import Counter
import os

app = Flask(__name__)

# ================= MongoDB Connection =================
client = MongoClient("mongodb://localhost:27017/")
db = client["HeartDiseaseDB"]
collection = db["patients"]

# ================= Load ML Model =================
model = joblib.load("random_forest_heart_model.pkl")

# ================= Home Page =================
@app.route("/")
def home():
    return render_template("index.html")


# ================= Predict + Add =================
@app.route("/predict", methods=["POST"])
def predict():

    # -------- Patient Identity --------
    name = request.form["name"]
    age = int(request.form["age"])

    # -------- Patient Clinical Data --------
    patient = {
        "name": name,
        "age": age,
        "sex": int(request.form["sex"]),
        "cp": int(request.form["cp"]),
        "trestbps": int(request.form["trestbps"]),
        "chol": int(request.form["chol"]),
        "fbs": int(request.form["fbs"]),
        "restecg": int(request.form["restecg"]),
        "thalach": int(request.form["thalach"]),
        "exang": int(request.form["exang"]),
        "oldpeak": float(request.form["oldpeak"]),
        "slope": int(request.form["slope"]),
        "ca": int(request.form["ca"]),
        "thal": int(request.form["thal"])
    }

    # ================= ML Preprocessing =================
    # Remove name before prediction
    input_df = pd.DataFrame([patient]).drop(columns=["name"])
    input_df = pd.get_dummies(input_df)

    # Ensure all trained features exist
    for col in model.feature_names_in_:
        if col not in input_df.columns:
            input_df[col] = 0

    # Correct feature order
    input_df = input_df[model.feature_names_in_]

    # Prediction
    prediction = int(model.predict(input_df)[0])

    # ================= MongoDB Logic =================
    existing = collection.find_one({"name": name, "age": age})

    if not existing:
        patient["target"] = prediction
        collection.insert_one(patient)
        message = "Patient not found → New record added to MongoDB."
    else:
        message = "Patient found → Prediction generated."

    result = "Heart Disease Detected ❤️" if prediction == 1 else "No Heart Disease ✅"

    return render_template("result.html", result=result, message=message)

# ================= Search Patient for Delete =================
@app.route("/search_delete", methods=["POST"])
def search_delete():
    name = request.form["name"]
    age = int(request.form["age"])

    patient = collection.find_one({"name": name, "age": age})

    if patient:
        return render_template("confirm_delete.html", patient=patient)
    else:
        return "Patient not found"
@app.route("/retrain")
def retrain_model():
    try:
        os.system("python train_model.py")
        return "✅ Model retrained successfully using latest patient data."
    except Exception as e:
        return f"❌ Retraining failed: {str(e)}", 500

# ================= Confirm Delete =================
@app.route("/delete", methods=["POST"])
def delete():
    name = request.form.get("name")
    age = request.form.get("age", type=int)

    if not name or age is None:
        return "Invalid delete request", 400

    collection.delete_one({"name": name, "age": age})
    return "Patient deleted successfully"

# ================= Chart Data API =================
@app.route("/chart-data")
def chart_data():
    data = list(collection.find({}, {
        "_id": 0,
        "age": 1,
        "chol": 1,
        "trestbps": 1,
        "thalach": 1,
        "cp": 1,
        "sex": 1,
        "fbs": 1,
        "target": 1
    }))

    # Basic lists
    targets = [d["target"] for d in data]
    ages = [d["age"] for d in data]
    chols = [d["chol"] for d in data]
    bps = [d["trestbps"] for d in data]
    thalach = [d["thalach"] for d in data]

    # Categorical distributions
    disease_count = Counter(targets)
    cp_count = Counter([d["cp"] for d in data])
    sex_disease = Counter([(d["sex"], d["target"]) for d in data])
    fbs_disease = Counter([(d["fbs"], d["target"]) for d in data])

    return jsonify({

        # 1️⃣ Disease Distribution
        "target_labels": ["No Disease", "Heart Disease"],
        "target_counts": [
            disease_count.get(0, 0),
            disease_count.get(1, 0)
        ],

        # 2️⃣ Age vs Disease
        "age": ages,
        "age_target": targets,

        # 3️⃣ Cholesterol vs Disease
        "chol": chols,
        "chol_target": targets,

        # 4️⃣ Blood Pressure vs Disease
        "bp": bps,
        "bp_target": targets,

        # 5️⃣ Max Heart Rate vs Disease
        "thalach": thalach,
        "thalach_target": targets,

        # 6️⃣ Chest Pain Type Distribution
        "cp_labels": list(cp_count.keys()),
        "cp_counts": list(cp_count.values()),

        # 7️⃣ Sex vs Disease
        "sex_disease": {
            "male_no": sex_disease.get((1, 0), 0),
            "male_yes": sex_disease.get((1, 1), 0),
            "female_no": sex_disease.get((0, 0), 0),
            "female_yes": sex_disease.get((0, 1), 0)
        },

        # 8️⃣ Fasting Blood Sugar vs Disease
        "fbs_disease": {
            "normal_no": fbs_disease.get((0, 0), 0),
            "normal_yes": fbs_disease.get((0, 1), 0),
            "high_no": fbs_disease.get((1, 0), 0),
            "high_yes": fbs_disease.get((1, 1), 0)
        }
    })


# ================= Dashboard =================
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# ================= Run Flask App =================
if __name__ == "__main__":
    app.run(debug=True)
