# 🧱 StrengthCast — Concrete Strength Predictor

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://adityajare-strengthcast-main-sewv1x.streamlit.app/)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit%20App-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://adityajare-strengthcast-main-sewv1x.streamlit.app/)

> 🌐 **Live Demo:** Try the app online at **[adityajare-strengthcast-main-sewv1x.streamlit.app](https://adityajare-strengthcast-main-sewv1x.streamlit.app/)**

An intelligent concrete compressive strength prediction web application that estimates the strength of concrete based on its mix composition. The machine learning model, data preprocessing, and training pipeline were built entirely from scratch.

## 📖 Overview

Predicting concrete strength is essential for ensuring structural safety and optimizing material usage. This system takes **8 key mix design parameters** as input and uses a trained machine learning model to predict the compressive strength of concrete in **MPa**.

### Input Features

| Parameter | Description | Range |
|---|---|---|
| Cement | Cement content in the mix | 100 – 600 kg/m³ |
| Blast Furnace Slag | Slag content in the mix | 0 – 400 kg/m³ |
| Fly Ash | Fly ash content in the mix | 0 – 200 kg/m³ |
| Water | Water content in the mix | 100 – 400 kg/m³ |
| Superplasticizer | Superplasticizer dosage | 0 – 35 kg/m³ |
| Coarse Aggregate | Coarse aggregate content | 500 – 1200 kg/m³ |
| Fine Aggregate | Fine aggregate content | 500 – 1200 kg/m³ |
| Age | Curing age of the concrete | 1 – 365 days |

### Strength Classification

| Category | Range | Indicator |
|---|---|---|
| 🔴 Weak Concrete | ≤ 20 MPa | Error alert |
| 🟡 Normal Concrete | 21 – 60 MPa | Warning alert |
| 🟢 High Strength Concrete | > 60 MPa | Success alert |

## 🧠 Machine Learning

The entire ML pipeline — data preprocessing, feature engineering, model selection, and training — was designed and implemented from scratch in a **Jupyter Notebook**.

### Model Comparison (after GridSearchCV)

Three regression models were evaluated to find the best fit:

| Algorithm | R² Score | RMSE (MPa) | MAE (MPa) |
|---|---|---|---|
| Linear Regression | 0.6276 | 9.7965 | 7.7456 |
| Random Forest | 0.8805 | 5.5491 | 3.8006 |
| **XGBoost** ✅ | **0.9289** | **4.2791** | **2.9638** |

XGBoost outperformed Linear Regression by **~30 points in R²**, confirming that concrete strength depends on **nonlinear interactions** between mix ratios and curing age that linear models cannot capture.

### Final Model

- **Model**: XGBoost Regressor — serialized as `concrete_strength_model.pkl` via joblib
- **Input**: 8 numerical features (cement, blast furnace slag, fly ash, water, superplasticizer, coarse aggregate, fine aggregate, age)
- **Output**: Predicted compressive strength in MPa (regression)

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend / UI | Streamlit |
| ML Framework | XGBoost, scikit-learn |
| Data Handling | pandas |
| Serialization | joblib |
| Package Mgmt | uv |
| Language | Python 3.12 |

## 🚀 Getting Started

### 🌐 Live Web App

Try the deployed application directly in your browser without any local setup:
👉 **[StrengthCast Live Demo](https://adityajare-strengthcast-main-sewv1x.streamlit.app/)**

---

### Local Setup

#### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/AdityaJare/StrengthCast.git
cd StrengthCast
```

2. **Install dependencies**

Using uv (recommended):

```bash
uv sync
```

Or using pip:

```bash
pip install -r requirements.txt
```

3. **Run the application**

```bash
uv run streamlit run main.py
```

Or without uv:

```bash
streamlit run main.py
```

4. **Open in browser** — Navigate to `http://localhost:8501`

## 📂 Project Structure

```
StrengthCast/
├── main.py                       # Streamlit application entry point
├── concrete_strength_model.pkl   # Trained ML model (serialized)
├── pyproject.toml                # Project metadata & dependencies
├── requirements.txt              # Pip-compatible dependency list
├── uv.lock                       # Locked dependency versions (uv)
├── .python-version               # Python version specification
├── .gitignore                    # Git ignore rules
└── README.md                    # Project documentation
```

## 🖥️ Usage

1. Adjust the input fields for each concrete mix parameter to match your mix design.
2. Click the **"Predict Concrete Strength"** button.
3. The app will display the predicted compressive strength in MPa along with a classification indicator (weak, normal, or high strength).

## 📦 Dependencies

| Package | Version |
|---|---|
| streamlit | ≥ 1.64.0 |
| scikit-learn | ≥ 1.9.1 |
| xgboost | ≥ 3.4.1 |
| pandas | ≥ 3.0.6 |

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

## 📝 License

This project is open source and available for personal and educational use.

## 👤 Author

**[AdityaJare](https://github.com/AdityaJare)**

Built with ❤️ as a hands-on machine learning project — from data preprocessing and model training to deployment.
