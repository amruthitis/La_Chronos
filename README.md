# La Chronos

> **Where time reveals the hidden state of the market.**

La Chronos is a financial intelligence platform that identifies hidden market regimes using deep representation learning. By combining historical financial indicators with a neural autoencoder and unsupervised clustering, it uncovers recurring market states and provides both historical and real-time market analysis.

---

## Features

* Historical market regime analysis (2010–Present)
* Live market analysis using Yahoo Finance
* Deep representation learning with a PyTorch Autoencoder
* Unsupervised regime detection using KMeans
* Automatic feature engineering
* High-performance FastAPI backend
* Redis caching for faster inference
* Modern React frontend
* Interactive and responsive user interface

---

## Demo

Frontend

https://YOUR-VERCEL-URL.vercel.app

Backend API

https://YOUR-RENDER-URL.onrender.com

API Documentation

https://YOUR-RENDER-URL.onrender.com/docs

---

## Screenshots

### Landing Page

*Add screenshot*

### Market Analysis

*Add screenshot*

### Historical Analysis

*Add screenshot*

---

# System Architecture

```
                    User
                      │
                      ▼
                React Frontend
                      │
                REST API (Axios)
                      │
                      ▼
                FastAPI Backend
                      │
        ┌─────────────┴─────────────┐
        │                           │
 Historical CSV             Yahoo Finance API
        │                           │
        └─────────────┬─────────────┘
                      ▼
            Feature Engineering
                      │
             StandardScaler
                      │
             PyTorch Encoder
                      │
                  KMeans
                      │
                      ▼
             Market Regime
```

---

# Machine Learning Pipeline

### Feature Engineering

The backend automatically computes:

* Daily Returns
* 20-Day Rolling Volatility
* Yield Spread (10Y - 3M Treasury)
* S&P 500 Volume
* VIX

---

### Representation Learning

Instead of clustering directly on raw financial indicators, La Chronos first compresses market behaviour into a lower-dimensional latent representation using a PyTorch Autoencoder.

This representation captures the underlying structure of market behaviour while reducing noise.

---

### Market Regime Detection

The encoded latent vectors are clustered using KMeans, allowing the system to identify recurring market regimes without requiring labeled training data.

Current supported regimes:

* Bullish
* Bearish
* Sideways
* Crisis

---

# Tech Stack

### Frontend

* React
* TypeScript
* Tailwind CSS
* Framer Motion
* Axios
* React Query

### Backend

* FastAPI
* Pydantic
* Pandas
* NumPy
* PyTorch
* Scikit-learn
* Redis
* yfinance

---

# Repository Structure

```
src/
│
├── api/
├── schemas/
├── services/
├── data/
├── models/
├── main.py
│
frontend/
│
└── React Application
```

---

# Running Locally

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/la-chronos.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the backend

```bash
uvicorn src.main:app --reload
```

Run the frontend

```bash
npm install
npm run dev
```

---

# API

## Predict Historical Market

```
POST /predict
```

Request

```json
{
  "date": "2023-10-15"
}
```

---

## Predict Current Market

```
POST /predict
```

Request

```json
{}
```

---

Example Response

```json
{
  "date": "2023-10-15",
  "regime": "Bullish"
}
```

---

# Design Philosophy

La Chronos is designed as a financial intelligence platform rather than a traditional machine learning demo.

The objective is to provide a clean, intuitive experience while exposing sophisticated backend architecture built on modern machine learning and software engineering principles.

---

# Future Improvements

* Confidence estimation
* Market timeline explorer
* Multi-index support
* Portfolio regime analysis
* Explainable AI
* Docker deployment
* CI/CD pipeline
* Cloud monitoring

---

# Author

**Amruth**

If you found this project interesting, feel free to connect or leave a ⭐ on the repository.
