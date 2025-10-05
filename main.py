from fastapi import FastAPI, UploadFile, File ,Form
from pydantic import BaseModel
import pandas as pd
from clustersting_pipeline import (
    scale_data,
    apply_kmeans,
    apply_pca,
    attach_labels,
    cluster_summary
)

app = FastAPI(title="University Clustering API", description="Modular clustering pipeline with PCA visualization", version="1.0")

class InputData(BaseModel):
    data: list[list[float]]
    columns: list[str]
    n_clusters: int = 3

@app.post("/cluster/raw")
def cluster_raw(input: InputData):
    """
    Accepts raw numerical data and returns cluster labels and PCA components.
    """
    df = pd.DataFrame(input.data, columns=input.columns)
    scaled = scale_data(df)
    model = apply_kmeans(scaled, input.n_clusters)
    components = apply_pca(scaled)
    labeled_df = attach_labels(df, model)
    summary = cluster_summary(labeled_df)
    return {
        "labels": model.labels_.tolist(),
        "components": components.values.tolist(),
        "summary": summary.to_dict()
    }

@app.post("/cluster/file")
async def cluster_file(
    file: UploadFile = File(...),
    n_clusters: int = Form(3)
):
    """
    Accepts an Excel file, runs full clustering pipeline, and returns results.
    """
    df = pd.read_excel(file.file)
    if "Univ" in df.columns:
        df.drop("Univ", axis=1, inplace=True)
    scaled = scale_data(df)
    model = apply_kmeans(scaled, n_clusters)
    components = apply_pca(scaled)
    labeled_df = attach_labels(df, model)
    summary = cluster_summary(labeled_df)
    return {
        "labels": model.labels_.tolist(),
        "components": components.values.tolist(),
        "summary": summary.to_dict()
    }
