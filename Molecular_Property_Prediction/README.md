# Molecular Property Prediction

This project focuses on predicting the **aqueous solubility (LogS)** of small drug-like molecules using **machine learning (ML)** models trained on experimental data and computed molecular descriptors. The goal is to build reliable predictive models using **Multiple Linear Regression (MLR)** and **Random Forest (RF)**, compare their performance, and interpret the role of molecular features using statistical coefficients and SHAP values. The project further aims to visualize feature importance, helping to identify key descriptors that influence solubility.

## 🛠 Tools Used

- `RDKit`: for molecular structure handling and generating descriptors from SMILES strings
- `Mordred`: for computing a wide range of molecular descriptors
- `Statsmodels`: for MLR model and variance inflation factor (VIF) analysis
- `Scikit-learn`: for RF model and evaluation metrics
- `SHAP` (SHapley Additive exPlanations): for interpreting feature importance in the RF model
- `Matplotlib`: Visualization of model coefficients, SHAP values, and feature importance

## 📊 Workflow Summary

1. **Data Retrieval**: SMILES strings retrieved from PubChem using the PUG REST API
2. **Data Cleaning**: Removal of invalid entries, missing values, and duplicates
3. **Descriptor Calculation**: Mordred descriptors computed, followed by filtering steps:
   - Removal of categorical descriptors
   - Elimination of low-variance and highly correlated descriptors
4. **Model Training**: 80:20 train-test split
   - MLR model with VIF-based feature selection to mitigate multicollinearity
   - Random Forest model with hyperparameter tuning
5. **Model Evaluation**: Using R², RMSE, and MAE
6. **Feature Interpretation**:
   - MLR: Regression coefficients
   - RF: SHAP values and summary plots
7. **Visualization**: Bar charts, scatter plots, and SHAP plots to highlight important descriptors

## 📄 Files Included

- `Molecular_Property_Prediction.ipynb` – Main notebook with all code and analysis
- `logS_dataset.csv` – Original dataset from Source 1
- `logS_dataset_updated.csv` – Cleaned dataset from Source 1
- `logS_dataset2.csv` – Original dataset from Source 2
- `logS_dataset_new.csv` – Combined cleaned dataset from Source 1 and 2
- `desc_reduced.csv` – Filtered descriptors for Source 1
- `desc_new.csv` – Filtered descriptors for combined dataset
