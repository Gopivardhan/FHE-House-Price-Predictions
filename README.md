
# 🏠 FHE House Price Predictions Gopi Vardhan Vallabhaneni

This project leverages **Fully Homomorphic Encryption (FHE)** techniques to enable **secure and private house price predictions**. The goal is to demonstrate how encrypted data can be processed and analyzed without compromising user privacy.

---

## 🔍 Project Overview

Traditional machine learning models require access to plaintext data, which poses a privacy risk. This project integrates machine learning with FHE to:

- Train a house price prediction model.
- Encrypt input data using FHE.
- Perform predictions on encrypted data.
- Decrypt results on the client side.

---

## 📦 Features

- Preprocessing of housing datasets
- Training a regression model for price prediction
- FHE encryption & decryption pipeline
- Encrypted inference

---

## 🛠️ Technologies Used

- Python
- Scikit-learn
- Pandas & NumPy
- Concrete-ML (Zama’s FHE framework)
- Jupyter Notebook

---

## 📁 Project Structure

```
FHE-House-Price-Predictions/
├── data/               # Raw and processed datasets
├── notebooks/          # Jupyter notebooks for development
├── src/                # Source code for model training & FHE operations
├── results/            # Output and results of prediction
└── README.md           # Project overview
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Gopivardhan/FHE-House-Price-Predictions.git
cd FHE-House-Price-Predictions
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the demo

Open the Jupyter notebook:

```bash
jupyter notebook notebooks/house_price_fhe_demo.ipynb
```

---

## 🔐 About FHE

**Fully Homomorphic Encryption (FHE)** allows computation on encrypted data without the need to decrypt it. This enables secure data processing in privacy-sensitive environments.

We use **Concrete-ML** to perform encrypted inference on house price prediction models.

---

## 📈 Example Usage

```python
# Encrypt user input
encrypted_input = fhe_model.encrypt([num_rooms, location_score, age])

# Perform encrypted inference
encrypted_prediction = fhe_model.predict(encrypted_input)

# Decrypt result
price = fhe_model.decrypt(encrypted_prediction)
```

---

## 🙌 Acknowledgements

* the Concrete-ML library
* Scikit-learn for machine learning algorithms

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
