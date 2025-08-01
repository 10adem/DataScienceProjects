import streamlit as st
from datetime import datetime
import yfinance as yf
import matplotlib.pyplot as plt

symbol = st.sidebar.text_input("Hisse Senedi Sembolü", value="ASELS")

st.title(symbol + " Hisse Senedi Grafiği")

start_date = st.sidebar.date_input("Başlangıç Tarihi", datetime(2020, 1, 1))
end_date = st.sidebar.date_input("Bitiş Tarihi", datetime.now())

df = yf.download(symbol + '.IS', start=start_date, end=end_date)
df.columns = df.columns.droplevel(1)

st.subheader("Hisse Senedi Trend Grafiği")
st.line_chart(df['Close'])

st.subheader("Hisse Senedi Fiyatlar Tablosu")
st.write(df[['Open', 'High', 'Low', 'Close']])