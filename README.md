
# Credit Scoring

This project implements a machine learning model to determine the creditworthiness of individuals based on several predetermined features. A User Interface is provided for interacting with the model.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Data](#data)
- [Technical Description](#technical-description)

## Installation

**Requirements:**

- Python 3.12
- Anaconda or Conda [link](https://github.com/conda/conda)

**Installation steps using conda and the configuration file:**

1. Clone the repository:
   ```bash
   git clone https://github.com/lpestov/credit_scoring.git
   ```
2. Change to the project directory:
   ```bash
   cd credit_scoring/env
   ```
3. Create and activate a conda environment using the configuration file `environment.yml`:
   ```bash
   conda env create --file environment.yml
   conda activate credit-scoring
   ```
4. Change to the project directory:
   ```bash
   ..
   cd credit_scoring/src
   ```
5. Launch the User Interface:
   ```bash
   streamlit run UI.py
   ```
6. Make sure that the installed scikit-learn version is correct (recommended scikit-learn 1.6.1). If necessary, update it:
   ```bash
   conda install scikit-learn=1.6.1
   ```

## Usage

This project is intended for assessing the creditworthiness of individuals. Once the Streamlit interface is launched, the user will be presented with a form to input the required parameters. The model will then output a prediction indicating whether the credit is approved or not.

## Examples

Below is a demonstration of how the User Interface works:

- [project_demo.mp4](project_demo.mp4) (Soon)

## Data

The dataset `german_credit_data.csv` [Kaggle](https://www.kaggle.com/datasets/uciml/german-credit) containing information about 1000 individuals is used for training and testing the model. The following features are used for the analysis:
- Age (numeric)
- Sex (text: male, female)
- Job (numeric: 0 - unskilled and non-resident, 1 - unskilled and resident, 2 - skilled, 3 - highly skilled)
- Saving accounts (text - little, moderate, quite rich, rich)
- Checking account (text - little, moderate, rich)
- Credit amount (numeric, in Deutsch Mark)
- Duration of credit (numeric, in month)
- Purpose (text: car, furniture/equipment, radio/TV, domestic appliances, repairs, education, business, vacation/others)

## Technical Description

### Main Project Files:
- [UI.py](src/UI.py)  
  Implements a web interface using Streamlit for collecting user input and displaying the prediction, which is executed by the `predict` function.

- [input_processing.py](src/input_processing.py)  
  Contains the function for preprocessing the user input data before it is passed to the model for prediction.

- [one_hot_encoder.joblib](models/one_hot_encoder.joblib)  
  Saved one-hot encoder used for categorical features.

- [ordinal_encoder.joblib](models/ordinal_encoder.joblib)  
  Ordinal encoder for the "Saving accounts" feature.

- [scaler.joblib](models/scaler.joblib)  
  Saved scaler for data standardization.

### Solution Description:
- One-hot encoding is applied to the categorical features (`Sex`, `Housing`, `Checking account`, `Purpose`).
- The `Saving accounts` feature is processed using ordinal encoding.
- Two models, Random Forest Classifier and Gradient Boosting Classifier, were compared to determine creditworthiness. Hyperparameter tuning was performed using GridSearch.
- The best results were achieved with the Gradient Boosting model (ROC AUC: 0.764 on the test dataset).

Data analysis, model training, and testing are detailed in the [Credit_scoring_final.ipynb](notebooks/Credit_scoring_final.ipynb) notebook.