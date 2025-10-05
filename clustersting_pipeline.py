import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# 1. Load and clean data
def load_data(path: str) -> pd.DataFrame:
    """
    Load Excel file and drop non-numeric identifier columns.
    """
    df = pd.read_excel(path)
    if "Univ" in df.columns:
        df.drop("Univ", axis=1, inplace=True)
    return df

# 2. Scale features
def scale_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize features using StandardScaler.
    """
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df)
    return pd.DataFrame(scaled, columns=df.columns)

# 3. Compute WCSS for Elbow Method
def compute_wcss(data: pd.DataFrame, max_clusters: int = 8) -> list:
    """
    Calculate Within-Cluster Sum of Squares for cluster counts 1 to max_clusters.
    """
    wcss = []
    for k in range(1, max_clusters):
        model = KMeans(n_clusters=k, random_state=42)
        model.fit(data)
        wcss.append(model.inertia_)
    return wcss

# 4. Apply KMeans clustering
def apply_kmeans(data: pd.DataFrame, n_clusters: int = 3) -> KMeans:
    """
    Fit KMeans model and return trained model.
    """
    model = KMeans(n_clusters=n_clusters, random_state=42)
    model.fit(data)
    return model

# 5. Apply PCA for dimensionality reduction
def apply_pca(data: pd.DataFrame, n_components: int = 3) -> pd.DataFrame:
    """
    Reduce data to n_components using PCA.
    """
    pca = PCA(n_components=n_components, random_state=42)
    components = pca.fit_transform(data)
    return pd.DataFrame(components, columns=[f"PC{i+1}" for i in range(n_components)])

# 6. Attach cluster labels to original data
def attach_labels(original_df: pd.DataFrame, model: KMeans) -> pd.DataFrame:
    """
    Add cluster labels to original DataFrame.
    """
    df = original_df.copy()
    df["Cluster"] = model.labels_
    return df

# 7. Get cluster-wise summary
def cluster_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return mean values of numeric features grouped by cluster.
    """
    numeric_cols = df.select_dtypes(include="number").columns
    return df.groupby("Cluster")[numeric_cols].mean()

# 8. Export results (optional)
def export_results(df: pd.DataFrame, path: str) -> None:
    """
    Save clustered DataFrame to Excel.
    """
    df.to_excel(path, index=False)