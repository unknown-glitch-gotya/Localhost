import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def run():

    # 1. Load Multimedia Data
    data = pd.read_csv(
        "data/multimedia_data.csv"
    )

    features = [
        "Brightness",
        "Size",
        "Duration"
    ]

    X = data[features]

    # 2. Standardize Features
    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(
        X
    )

    # 3. Create Clustering Model
    model = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    # 4. Group Similar Resources
    result = model.fit_predict(
        X_scaled
    )

    data["Feature_Cluster"] = result

    # 5. Cluster Summary
    summary = data.groupby(
        "Feature_Cluster"
    )[features].mean().round(2)

    return {
        "data": data,
        "summary": summary
    }
