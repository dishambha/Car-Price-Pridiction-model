# 🚗 Car Price Prediction Model

This project predicts the **selling price** of used cars based on user-provided attributes such as fuel type, transmission, kilometers driven, and more. It uses supervised machine learning techniques and provides an easy-to-use web interface.

---

## 📌 Table of Contents

- [Project Objective](#project-objective)
- [Dataset Description](#dataset-description)
- [Working](#working)
- [Methodology](#methodology)
- [Technologies Used](#technologies-used)
- [Web App Interface](#web-app-interface)
- [Results](#results)
- [How to Run](#how-to-run)
- [Future Scope](#future-scope)
- [Author](#author)
- [License](#license)

---

## 🎯 Project Objective

To develop a regression-based machine learning model that predicts the resale price of used cars. The model helps buyers and sellers estimate the market value of a car based on specific input features.

---

## 📂 Dataset Description

The dataset contains the following features:

| Feature           | Description                              |
|------------------|------------------------------------------|
| Name             | Car brand/model                          |
| Year             | Year of manufacture                      |
| Selling_Price    | Price at which the car is sold (Target) |
| Present_Price    | Price of the car when new               |
| Kms_Driven       | Total kilometers driven                  |
| Fuel_Type        | Petrol, Diesel, or CNG                   |
| Seller_Type      | Individual or Dealer                     |
| Transmission     | Manual or Automatic                      |
| Owner            | Number of previous owners                |

> 📌 **Source**: *[Mention your dataset source, e.g., Kaggle or UCI]*

---

## ⚙️ Working

1. Clean and preprocess the dataset.
2. Convert categorical variables into numerical format.
3. Train a regression model (Linear Regression).
4. Evaluate the model using R² Score, MAE, and MSE.
5. Predict selling price based on user inputs in the deployed web interface.

---

## 🧠 Methodology

### 🔹 1. Data Preprocessing
- Removed null values and irrelevant columns.
- Encoded categorical features.
- Created new features like car age.
- Handled outliers where necessary.

### 🔹 2. EDA (Exploratory Data Analysis)
- Analyzed price trends by fuel type, seller type, etc.
- Used correlation heatmaps and distribution plots.

### 🔹 3. Model Training
- Used **Linear Regression** as the base model.
- Train-test split: 80/20
- Optionally compared with Random Forest and Decision Tree.

### 🔹 4. Evaluation Metrics
- **R² Score**
- **Mean Absolute Error (MAE)**
- **Mean Squared Error (MSE)**

---

## 🛠️ Technologies Used

- Python 3.x
- Jupyter Notebook / Google Colab
- Libraries: NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn
- Web App: Streamlit or Flask

---

## 🖼️ Web App Interface

The user-friendly interface allows users to input car details and instantly view predicted selling prices.

![Car Price Prediction UI](images/Screenshot-UI.png)

---

## 📈 Results

| Metric        | Value (Example) |
|---------------|-----------------|
| R² Score      | 0.91            |
| MAE           | 1.2 Lakhs       |
| MSE           | 3.6 Lakhs²      |

> ✅ The model performs well and gives a realistic estimate of the resale value.

---

## 🚀 How to Run

### 🧪 For Notebook:

1. Clone the repo:
   ```bash
   git clone https://github.com/dishambha/Car-Price-Pridiction-model
   cd Car-Price-Pridiction-model
