# Name Trend Forecasting

A time-series and machine-learning project for exploring historical baby-name popularity and forecasting future naming trends.

## Project objective

Baby names can reflect cultural changes, generational preferences, and long-term social patterns. This project provides a reproducible notebook for examining name popularity over time and building baseline forecasts for selected names.

## Current features

- Loads historical name records from a CSV file
- Validates required columns
- Cleans year and count fields
- Selects and visualizes a name-popularity series
- Builds a linear-regression forecasting baseline
- Evaluates baseline predictions using MAE and RMSE
- Produces an ARIMA forecast for future years
- Provides a foundation for Prophet, clustering, and changepoint extensions

## Technologies used

- Python
- pandas
- NumPy
- matplotlib
- scikit-learn
- statsmodels
- Prophet and ruptures as optional extensions
- Jupyter Notebook

## Repository structure

```text
data/
  README.md
notebooks/
  name_trend_forecasting.ipynb
README.md
requirements.txt
LICENSE
.gitignore
```

## Dataset format

Add a permitted CSV file at:

```text
data/name_trends.csv
```

The notebook expects at least these columns:

- `Year`
- `Name`
- `Count`

A `Gender` column may also be added for extended analysis.

## How to run

```bash
pip install -r requirements.txt
jupyter notebook notebooks/name_trend_forecasting.ipynb
```

Run the cells from top to bottom after adding the dataset.

## Methodology

1. Load and validate the historical name data.
2. Clean missing or invalid values.
3. Aggregate counts by year and name.
4. Plot the historical popularity of a selected name.
5. Split the series into training and testing periods.
6. Fit a linear-regression baseline.
7. Calculate MAE and RMSE.
8. Fit an ARIMA model and forecast future values.

## Expected outputs

- Historical popularity line chart
- Baseline model evaluation values
- Ten-year ARIMA forecast
- A reusable framework for comparing more names and models

## Limitations

- The dataset is not currently included in the repository.
- The ARIMA configuration is an educational baseline and is not exhaustively tuned.
- Name popularity may be affected by social changes that historical patterns cannot predict reliably.
- The current notebook focuses on one selected name at a time.

## Future improvements

- Add a public example dataset
- Compare multiple names and gender groups
- Add Prophet forecasting
- Add rolling-origin cross-validation
- Add MAPE and confidence intervals
- Add clustering for names with similar trajectories
- Add changepoint detection
- Build a Streamlit interface

## Author

**Muhammad Kamil Shah**  
BS Data Science

## License

This project is licensed under the MIT License.
