import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def run():
    data=pd.read_csv("data/student_data.csv")

    features = ["Study_Hours","Attendance","Assignment_Score","Internal_Marks","Previous_Score"]

    X=data[features]

    #Standardization

   
    X_scaled = StandardScaler().fit_transform(X)

#Kmeans
    
    k = 3
    model = KMeans(
        n_clusters=k,
        random_state= 42,
        n_init=10
    )
    
    data["Cluster"] = model.fit_predict(X_scaled)

    #Clustered Suimmary

    summary = data.groupby("Cluster")[features].mean().round(2)

   
    return{
        "data":data,
        "summary": summary,
        "cluster":k
    }