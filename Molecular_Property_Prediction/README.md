# Molecular Property Prediction

This project focuses on predicting the **aqueous solubility (LogS)** of small drug-like molecules using **machine learning (ML)** models trained on experimental data and computed molecular descriptors. The goal is to build reliable predictive models using **Multiple Linear Regression (MLR)** and **Random Forest (RF)**, compare their performance, and interpret the role of molecular features using statistical coefficients and SHAP values. The project further aims to visualize feature importance, helping to identify key descriptors that influence solubility.

## Tools Used

- `RDKit`: for generating Mol objects used for descriptor calculations
- `Mordred`: for computing a wide range of molecular descriptors
- `Statsmodels`: for variance inflation factor (VIF) analysis
- `Scikit-learn`: for traning and evaluation of ML models (MLR and RF)
- `SHAP` (SHapley Additive exPlanations): for interpreting feature importance in the RF model
- `Matplotlib`: Visualization of model performance and feature importance

## Workflow Summary

1. **Data Retrieval**: SMILES strings retrieved from PubChem using the PUG REST API
2. **Data Cleaning**: Removal of invalid entries, missing values, and duplicates
3. **Descriptor Calculation**: Mordred descriptors computed, followed by filtering steps:
   - Removal of categorical, low-variance, and highly correlated descriptors
4. **Model Training**: 
   - MLR and RF models using 80:20 train-test split
   - Model improvement using VIF and outlier detection
5. **Model Evaluation**: using R², RMSE, and MAE
6. **Feature Importance Interpretation**: Coefficient plot and SHAP value plots

## Files Included

- `Molecular_Property_Prediction.ipynb` – Main notebook with all code and analysis
- `logS_dataset.csv` – Original dataset from Source 1
- `logS_dataset_updated.csv` – Cleaned dataset from Source 1
- `logS_dataset2.csv` – Original dataset from Source 2
- `logS_dataset_new.csv` – Combined cleaned dataset from Source 1 and 2
- `desc_reduced.csv` – Filtered descriptors for Source 1
- `desc_new.csv` – Filtered descriptors for combined dataset
