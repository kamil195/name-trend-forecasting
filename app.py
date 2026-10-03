import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from statsmodels.tsa.arima.model import ARIMA

st.set_page_config(page_title="Name Trend Forecasting | Muhammad Kamil Shah", page_icon="📈", layout="wide")
st.title("Name Trend Forecasting Explorer")
st.caption("Explore historical name popularity and compare a linear baseline with an ARIMA forecast.")

uploaded=st.file_uploader("Upload name_trends.csv",type=["csv"])
st.caption("Required columns: Year, Name, Count. Optional: Gender.")
if uploaded is None:
    st.info("Add a permitted CSV dataset to run the forecasting workflow.")
    st.stop()
df=pd.read_csv(uploaded)
required={"Year","Name","Count"}
if not required.issubset(df.columns):
    st.error("CSV must contain Year, Name and Count columns."); st.stop()
df["Year"]=pd.to_numeric(df["Year"],errors="coerce"); df["Count"]=pd.to_numeric(df["Count"],errors="coerce")
df=df.dropna(subset=["Year","Name","Count"]); df["Year"]=df["Year"].astype(int)
names=sorted(df["Name"].astype(str).unique())
name=st.selectbox("Name",names)
series=df[df["Name"].astype(str)==name].groupby("Year")["Count"].sum().sort_index()
if len(series)<8:
    st.warning("This name has too few yearly observations for a useful demo."); st.stop()

years=series.index.to_numpy(); values=series.to_numpy()
split=max(3,int(len(series)*.8))
lr=LinearRegression().fit(years[:split].reshape(-1,1),values[:split])
pred=lr.predict(years[split:].reshape(-1,1))
mae=mean_absolute_error(values[split:],pred); rmse=np.sqrt(mean_squared_error(values[split:],pred))
m1,m2,m3=st.columns(3); m1.metric("Years",len(series)); m2.metric("Baseline MAE",f"{mae:.1f}"); m3.metric("Baseline RMSE",f"{rmse:.1f}")

horizon=st.slider("Forecast horizon (years)",3,15,10)
fit=ARIMA(series.astype(float),order=(1,1,1)).fit()
forecast=fit.get_forecast(steps=horizon)
future=np.arange(years.max()+1,years.max()+1+horizon)
mean=forecast.predicted_mean.to_numpy()
ci=forecast.conf_int().to_numpy()

fig,ax=plt.subplots(figsize=(10,5)); ax.plot(years,values,label="Historical"); ax.plot(future,mean,label="ARIMA forecast"); ax.fill_between(future,ci[:,0],ci[:,1],alpha=.2,label="Confidence interval"); ax.set_title(f"Popularity trend: {name}"); ax.set_xlabel("Year"); ax.set_ylabel("Count"); ax.legend(); st.pyplot(fig); plt.close(fig)
st.info("This is an educational baseline. Naming trends can shift for social and cultural reasons that historical models cannot anticipate.")
st.caption("Muhammad Kamil Shah · time series · regression · ARIMA · model evaluation")
