# Name Trend Forecasting

A time-series and machine-learning project that analyzes historical U.S. baby-name popularity and forecasts future naming trends.

![Name trend visualization](assets/name-trends.png)

## Project overview

Baby names often reflect cultural shifts, generational preferences, and changing social patterns. This project analyzes historical U.S. baby-name data, explores long-term popularity trends, and compares several forecasting and pattern-discovery techniques.

## Key features

- Identifies popular names overall and by decade
- Visualizes long-term trends for selected names
- Compares naming patterns by gender
- Forecasts future popularity using Linear Regression, ARIMA, and Prophet
- Groups names with similar trajectories using K-Means clustering
- Detects structural changes using changepoint detection

## Repository structure

```text
.
├── assets/
│   ├── name-trends.png
│   ├── arima-forecast.png
│   ├── prophet-forecast.png
│   └── changepoint-example.png
├── notebooks/
│   └── name_trend_forecasting.ipynb
├── reports/
│   ├── name_trend_forecasting_report.pdf
│   └── name_trend_forecasting_report.docx
├── .gitignore
├── AUTHORS.md
├── CITATION.cff
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── requirements.txt
```

## Technologies

- Python
- pandas and NumPy
- matplotlib and seaborn
- scikit-learn
- statsmodels ARIMA
- Prophet
- ruptures
- Jupyter Notebook

## Getting started

```bash
git clone <repository-url>
cd name-trend-forecasting
python -m venv .venv
```

Activate the environment:

```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the notebook:

```bash
jupyter notebook notebooks/name_trend_forecasting.ipynb
```

Internet access is required the first time the dataset is downloaded.

## Methodology

1. Load and inspect the historical name dataset
2. Clean and aggregate records by year, name, and gender
3. Explore trends by year and decade
4. Build baseline forecasts
5. Apply ARIMA and Prophet
6. Cluster names with similar historical patterns
7. Detect changepoints in popularity trajectories

## Sample results

### ARIMA forecast

![ARIMA forecast](assets/arima-forecast.png)

### Prophet forecast

![Prophet forecast](assets/prophet-forecast.png)

### Changepoint detection

![Changepoint detection](assets/changepoint-example.png)

## Limitations

- Forecast parameters are educational rather than exhaustively optimized
- Sparse or irregular name histories can reduce forecast accuracy
- Results may vary slightly across package versions
- The project is intended as an academic data-science demonstration

## Future improvements

- Add train/test evaluation with MAE, RMSE, and MAPE
- Compare additional forecasting models
- Add an interactive Streamlit interface
- Refactor reusable functions into a `src/` package
- Add automated tests

## Author

**Kamil Shah**  
BS Data Science

## License

This project is licensed under the MIT License.
