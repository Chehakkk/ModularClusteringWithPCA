
# 🧠 Modular Clustering Pipeline with FastAPI & PCA

A fully modular, API-ready clustering pipeline built for reproducibility, onboarding clarity, and infra-driven backend design.

---

## 🚀 Features

- 🔁 **Automated Clustering**: KMeans with configurable cluster count
- 📊 **PCA Visualization**: Dimensionality reduction for interpretable output
- 📂 **Excel Ingestion**: Upload `.xlsx` files via API
- ⚙️ **FastAPI Microservice**: Two endpoints (`/cluster/raw`, `/cluster/file`)
- 🧩 **Modular Pipeline**: Clean separation of logic for scaling and testing
- 🔐 **Infra-Aware Design**: Built for containerization, logging, and reproducibility

---

## 📦 Tech Stack

- FastAPI
- scikit-learn
- pandas
- openpyxl
- StandardScaler · KMeans · PCA


---

## 🧪 API Endpoints

### `/cluster/raw`  
- Accepts JSON payload with `data`, `columns`, and `n_clusters`  
- Returns cluster labels, PCA components, and summary

### `/cluster/file`  
- Accepts Excel file (`.xlsx`) and `n_clusters` via form-data  
- Returns same output as above

---

## 🧰 How to Run Locally

```bash
# Activate virtual environment
.\env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run FastAPI server
uvicorn main:app --reload





Visit: http://127.0.0.1:8000/docs for Swagger UI
 OUTPUT :
{
  "labels": [0, 1, 2, ...],
  "components": [[PC1, PC2, PC3], ...],
  "summary": {
    "0": {"SAT": ..., "Top10": ..., ...},
    "1": {...},
    "2": {...}
  }
}


