# 🚗 Car Price Prediction Model

This project aims to predict the price of used cars based on various attributes such as brand, fuel type, transmission, engine size, and more. It applies supervised machine learning techniques to train a regression model and evaluate its performance.

---

## 📌 Table of Contents

- [Project Objective](#project-objective)
- [Dataset Description](#dataset-description)
- [Working](#working)
- [Methodology](#methodology)
- [Technologies Used](#technologies-used)
- [Results](#results)
- [How to Run](#how-to-run)
- [Future Scope](#future-scope)
- [Author](#author)
- [License](#license)

---

## 🎯 Project Objective

To build a regression model that accurately predicts the selling price of a used car based on its features. The goal is to provide a reference for buyers and sellers in the used car market.

---

## 📂 Dataset Description

The dataset contains the following key features:

| Feature           | Description                              |
|------------------|------------------------------------------|
| Name             | Car name or brand                        |
| Year             | Year of manufacture                      |
| Selling_Price    | Price at which the car is sold (Target) |
| Present_Price    | Price of the car when new               |
| Kms_Driven       | Total kilometers driven                  |
| Fuel_Type        | Petrol, Diesel, or CNG                   |
| Seller_Type      | Individual or Dealer                     |
| Transmission     | Manual or Automatic                      |
| Owner            | Number of previous owners                |

> 📌 **Source**: [Mention source like Kaggle or UCI]

---

## ⚙️ Working

1. **Data Cleaning**: Checked for null values and cleaned outliers.
2. **Feature Engineering**:
   - Converted categorical columns using OneHotEncoding/LabelEncoding.
   - Derived new columns if necessary (e.g., car age = current year - manufacturing year).
3. **Model Training**:
   - Trained a Linear Regression model on the cleaned dataset.
   - Used 80/20 train-test split.
4. **Evaluation**:
   - Evaluated using R² Score, MAE, and MSE.
5. **Prediction**:
   - Used the trained model to predict prices for unseen data.

---

## 🧠 Methodology

### 🔸 1. Data Preprocessing
- Removed unnecessary columns
- Converted string categories to numerical (Label/OneHot Encoding)
- Removed extreme outliers using IQR or domain knowledge
- Normalized/standardized data if needed

### 🔸 2. Exploratory Data Analysis (EDA)
- Visualized feature correlations using heatmaps
- Analyzed distributions of selling price, fuel type, and transmission

### 🔸 3. Model Selection & Training
- **Model Used**: `Linear Regression`
- Compared with models like Random Forest and Decision Tree (optional)
- Split the dataset into train and test

### 🔸 4. Model Evaluation
- Metrics:
  - **R² Score**: Measures goodness of fit
  - **Mean Absolute Error (MAE)**
  - **Mean Squared Error (MSE)**

---

## 🛠️ Technologies Used

- Python 3.x
- Jupyter Notebook / Colab
- NumPy, Pandas – Data handling
- Matplotlib, Seaborn – Visualization
- Scikit-learn – ML Modeling

---

## 📈 Results

| Metric        | Value (Example) |
|---------------|-----------------|
| R² Score      | 0.91            |
| MAE           | 1.2 Lakhs       |
| MSE           | 3.6 Lakhs²      |

> The model gives accurate price predictions within a reasonable error margin.

---

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/dishambha/Car-Price-Pridiction-model
   cd Car-Price-Pridiction-model
