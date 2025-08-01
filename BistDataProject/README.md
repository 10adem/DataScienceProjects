# BIST Hisse Senedi Analizi / BIST Stock Analysis

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![yfinance](https://img.shields.io/badge/yfinance-0.2+-green.svg)](https://pypi.org/project/yfinance/)

## 🇹🇷 Türkçe

### Proje Açıklaması
Bu proje, Borsa İstanbul (BIST) hisse senetlerinin fiyat verilerini görselleştiren interaktif bir web uygulamasıdır. Streamlit kullanılarak geliştirilmiş olup, kullanıcıların hisse senedi sembollerini girerek trend grafiklerini ve fiyat tablolarını görüntülemesini sağlar.

### Özellikler
-  **İnteraktif Grafikler**: Hisse senedi kapanış fiyatlarının zaman serisi grafikleri
-  **Tarih Aralığı Seçimi**: Başlangıç ve bitiş tarihlerini özelleştirme
-  **Gerçek Zamanlı Veri**: Yahoo Finance API'si ile güncel veriler
-  **Fiyat Tablosu**: Açılış, yüksek, düşük ve kapanış fiyatları
-  **Kullanıcı Dostu Arayüz**: Basit ve sezgisel tasarım

###  Kurulum

1. **Gereksinimleri yükleyin:**
```bash
pip install streamlit yfinance matplotlib pandas
```

2. **Uygulamayı çalıştırın:**
```bash
streamlit run app.py
```

3. **Tarayıcınızda açın:**
```
http://localhost:8501
```

###  Kullanım
1. Sol panelden hisse senedi sembolünü girin (örn: ASELS, THYAO, GARAN)
2. Başlangıç ve bitiş tarihlerini seçin
3. "Hisse Senedi Trend Grafiği" bölümünde mavi çizgi grafiğini görüntüleyin
4. "Hisse Senedi Fiyatlar Tablosu" bölümünde detaylı verileri inceleyin

###  Teknik Detaylar
- **Framework**: Streamlit
- **Veri Kaynağı**: Yahoo Finance (yfinance)
- **Görselleştirme**: Streamlit line_chart
- **Veri İşleme**: Pandas

---

## 🇺🇸 English

###  Project Description
This project is an interactive web application for visualizing Borsa Istanbul (BIST) stock price data. Developed using Streamlit, it allows users to input stock symbols and view trend charts and price tables.

###  Features
-  **Interactive Charts**: Time series charts of stock closing prices
-  **Date Range Selection**: Customizable start and end dates
-  **Real-time Data**: Current data via Yahoo Finance API
-  **Price Table**: Open, high, low, and closing prices
-  **User-friendly Interface**: Simple and intuitive design

###  Installation

1. **Install requirements:**
```bash
pip install streamlit yfinance matplotlib pandas
```

2. **Run the application:**
```bash
streamlit run app.py
```

3. **Open in your browser:**
```
http://localhost:8501
```

###  Usage
1. Enter stock symbol in the left panel (e.g., ASELS, THYAO, GARAN)
2. Select start and end dates
3. View the blue line chart in the "Stock Trend Chart" section
4. Examine detailed data in the "Stock Prices Table" section

###  Technical Details
- **Framework**: Streamlit
- **Data Source**: Yahoo Finance (yfinance)
- **Visualization**: Streamlit line_chart
- **Data Processing**: Pandas

---