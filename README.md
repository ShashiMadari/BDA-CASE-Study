# ❤️ Heart Disease Prediction System (BDA Case Study)

## 📌 Overview

The **Heart Disease Prediction System** is a Big Data Analytics (BDA) case study project that uses Machine Learning techniques to predict the likelihood of heart disease based on patient health parameters.

The project combines:

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Machine Learning Model Training
- Flask Web Application
- Predictive Analytics

The trained **Random Forest Model** is integrated into a Flask-based web application, allowing users to input patient information and receive heart disease predictions through a user-friendly interface.

---

## 🎯 Objectives

The primary objectives of this project are:

- Analyze healthcare data
- Identify factors contributing to heart disease
- Build a predictive machine learning model
- Deploy the model using Flask
- Provide an easy-to-use prediction interface
- Demonstrate practical Big Data Analytics techniques

---

## ✨ Features

### Data Processing

- Data Cleaning
- Missing Value Handling
- Feature Selection
- Data Transformation

### Machine Learning

- Random Forest Classification
- Model Training
- Model Evaluation
- Prediction Generation

### Web Application

- User Input Form
- Prediction Dashboard
- Result Visualization
- Record Management Interface

---

## 🛠️ Technologies Used

### Programming Language

- Python

### Data Analytics

- Pandas
- NumPy

### Machine Learning

- Scikit-Learn
- Random Forest Classifier

### Web Framework

- Flask

### Visualization

- Matplotlib
- Seaborn

### Database Concepts

- MongoDB Cleaning Documentation

---

## 📂 Project Structure

```text
BDA-case/
│
├── templates/
│   ├── confirm_delete.html
│   ├── dashboard.html
│   ├── index.html
│   └── result.html
│
├── BdaMongodbcleaning.txt
├── HeartDiseaseTrain-Test.csv
├── Untitled.ipynb
├── app.py
├── bda main report.docx
├── random_forest_heart_model.pkl
├── train_model.py
└── README.md
```

---

## 📋 File Description

| File/Folder | Description |
|------------|-------------|
| templates/ | HTML templates used by the Flask application |
| confirm_delete.html | Confirmation page for deleting records |
| dashboard.html | Dashboard displaying analytics and prediction information |
| index.html | Home page containing patient data input form |
| result.html | Displays prediction results |
| BdaMongodbcleaning.txt | MongoDB cleaning and preprocessing notes |
| HeartDiseaseTrain-Test.csv | Dataset used for training and testing |
| Untitled.ipynb | Jupyter notebook containing analysis and experiments |
| app.py | Main Flask application |
| bda main report.docx | Final project report |
| random_forest_heart_model.pkl | Trained Random Forest model |
| train_model.py | Script used to train and save the machine learning model |
| README.md | Project documentation |

---

## ⚙️ Installation & Setup

### Clone the Repository

```bash
git clone https://github.com/ShashiMadari/project2.git
```

### Navigate to the Project Directory

```bash
cd project2/BDA-case
```

### Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 📦 Install Dependencies

Install required libraries:

```bash
pip install flask
pip install pandas
pip install numpy
pip install scikit-learn
pip install matplotlib
pip install seaborn
pip install joblib
pip install jupyter
```

Or use:

```bash
pip install -r requirements.txt
```

if a requirements file is available.

---

## 🧹 Data Preprocessing

The dataset used:

```text
HeartDiseaseTrain-Test.csv
```

The preprocessing stage includes:

- Removing duplicate records
- Handling missing values
- Feature selection
- Data normalization (if required)
- Preparing data for model training

Additional preprocessing notes can be found in:

```text
BdaMongodbcleaning.txt
```

---

## 🤖 Model Training

The machine learning model is trained using:

```text
train_model.py
```

Run:

```bash
python train_model.py
```

This script:

- Loads the dataset
- Splits training and testing data
- Trains the Random Forest model
- Evaluates model performance
- Saves the model as:

```text
random_forest_heart_model.pkl
```

---

## 🚀 Running the Application

Start the Flask application:

```bash
python app.py
```

Open your browser and navigate to:

```text
http://127.0.0.1:5000/
```

---

## 🌐 Application Workflow

### Step 1

Open the home page.

### Step 2

Enter patient information such as:

- Age
- Sex
- Blood Pressure
- Cholesterol
- Heart Rate
- Other medical attributes

### Step 3

Submit the form.

### Step 4

The trained Random Forest model processes the data.

### Step 5

The application displays:

- Heart Disease Prediction
- Risk Assessment Result

---

## 🔄 System Workflow

```text
HeartDiseaseTrain-Test.csv
            │
            ▼
     train_model.py
            │
            ▼
Random Forest Model
(random_forest_heart_model.pkl)
            │
            ▼
         app.py
            │
            ▼
      Flask Web App
            │
            ▼
      HTML Templates
            │
            ▼
 Heart Disease Prediction
```

---

## 📊 Analysis & Visualization

The project notebook:

```text
Untitled.ipynb
```

contains:

- Exploratory Data Analysis (EDA)
- Statistical summaries
- Correlation analysis
- Data visualizations
- Model experimentation

---

## 📈 Expected Output

The system predicts whether a patient is:

- At Risk of Heart Disease
- Not at Risk of Heart Disease

based on the trained machine learning model.

---

## 📄 Project Report

Detailed documentation is available in:

```text
bda main report.docx
```

The report includes:

- Problem Statement
- Dataset Description
- Methodology
- Data Analysis
- Machine Learning Approach
- Results
- Conclusion

---

## 🔮 Future Enhancements

Potential improvements include:

- MongoDB Integration
- User Authentication
- Real-Time Predictions
- Interactive Dashboard
- Multiple Machine Learning Models
- Deep Learning-Based Predictions
- Cloud Deployment (AWS, Azure, GCP)

---

## 🏁 Conclusion

This project demonstrates the practical application of **Big Data Analytics** and **Machine Learning** in healthcare.

By leveraging patient data and predictive modeling, the system provides valuable insights into heart disease risk, helping showcase how data-driven solutions can support healthcare decision-making.

---

## 👨‍💻 Author

**Shashi Madari**

Computer Science Engineering Student

📧 Email: shashimadari44@gmail.com

🐙 GitHub: https://github.com/ShashiMadari

---

## 📜 License

This project is intended for:

- Educational Purposes
- Academic Projects
- Research and Learning

Feel free to modify and extend the project for study and experimentation.
