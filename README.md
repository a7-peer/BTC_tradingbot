# Bitcoin Price Prediction Project

## Overview

This project aims to predict the next-day price change of Bitcoin using historical market data and technical indicators. The workflow includes extracting data from the Binance API, cleaning and processing the data, calculating technical indicators, performing exploratory data analysis (EDA), and training a machine learning model to predict Bitcoin price movements.

---

## Project Workflow

### 1. Data Extraction

- Data is pulled using the **Binance API** with a Python client.
- The raw OHLCV data (Open, High, Low, Close, Volume) is collected for the Bitcoin trading pair.
- An API key is used for authenticated access.

### 2. Data Cleaning and Feature Engineering

- The dataset columns include:
```

Date, open, high, low, close, volume, rsi, ema\_long, ema\_short, obv

````
- Calculated the **target variable** as the next day's closing price:
```python
btc_df["close_nextday"] = btc_df.close.shift(-1)
````

* Additional technical indicators such as RSI, EMA (long and short), and OBV were computed.
* The dataset was cleaned and saved to a CSV file for further use.

### 3. Exploratory Data Analysis (EDA)

* Performed EDA to understand the distribution, trends, and correlations in the data.
* Visualized key indicators and price movement relationships.

### 4. Model Training

* Selected relevant features for training, including technical indicators and lagged values.
* Split the data into training and testing sets using a time-based split (80% train, 20% test).
* Implemented a **Random Forest Regressor** pipeline with feature scaling (`StandardScaler`).
* Evaluated the model using regression metrics:

  * Mean Absolute Error (MAE)
  * Root Mean Squared Error (RMSE)
  * R² Score

---

## Results

The model achieved the following performance metrics on the test set:

* **MAE:** Approximately \$1622.71
* **RMSE:** Approximately \$2193.09
* **R² Score:** -0.18

These results show that predicting Bitcoin’s next-day price changes remains challenging due to high volatility.

---

## Requirements

To install all required Python packages, run the following command in your project directory:

```bash
pip install -r requirements.txt
```

This will install:

* `pandas` for data manipulation
* `numpy` for numerical operations
* `scikit-learn` for machine learning modeling
* `python-binance` to access Binance API
* `matplotlib` for plotting and visualization

---

## Future Improvements

* Explore predicting returns instead of absolute price changes.
* Incorporate more advanced technical indicators.
* Experiment with other machine learning models such as XGBoost or LightGBM.
* Use time-series cross-validation for more robust evaluation.
* Consider classification approaches for price direction prediction.

---

