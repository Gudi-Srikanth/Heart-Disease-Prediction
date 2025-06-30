# 🫀 Heart Disease Prediction using Machine Learning

A user-friendly web app that uses ensemble ML techniques to predict 10-year heart disease risk based on medical and lifestyle data. Built using Python (Flask), HTML/CSS, and a trained `StackingCVClassifier`.

---

## 🎥 Demo

> 📽️ **Watch the working demo here**  
> 🔗 [Click to view demo video](static/Heart-Diesase-Prediction_Demo.mp4)

---

## 🚀 Overview

This project is part of a research effort to apply machine learning to cardiovascular risk prediction. It combines classic ML models with an advanced stacking ensemble to improve predictive accuracy.

https://www.taylorfrancis.com/chapters/edit/10.1201/9781003591788-13/leveraging-machine-learning-web-applications-heart-disease-prediction-ravi-boda-mohan-rao-gudi-srikanth-bommidi-sathvik-kotha-ajay-kumar-kurma-srujan
---

## 🧠 Machine Learning Models Used

| Model                  | Accuracy (%) |
|------------------------|--------------|
| Logistic Regression    | 85.25        |
| Naive Bayes            | 85.25        |
| Random Forest          | 86.89        |
| XGBoost                | 90.16        |
| K-Nearest Neighbors    | 88.52        |
| Decision Tree          | 81.97        |
| Support Vector Classifier | 88.52     |
| **StackingCVClassifier** | **91.80** ✅ |

---

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3
- **Backend**: Python, Flask
- **ML Stack**: scikit-learn, XGBoost, KNN, SVC

---

## 🧪 How to Run Locally

```bash
git clone https://github.com/Gudi-Srikanth/Heart-Disease-Prediction.git
cd Heart-Disease-Prediction
pip install flask numpy scikit-learn xgboost
python app.py
