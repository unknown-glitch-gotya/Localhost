import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

def run():
    data=pd.read_csv("data/student_data.csv")

    features = ["Study_Hours","Attendance","Assignment_Score","Internal_Marks","Previous_Score"]

    X=data[features]
    y=data["Result"]

    X_train,X_test,y_train,y_test, id_train, id_test = train_test_split(X, y,data["Student_ID"],
        test_size=0.30,
        random_state=42
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
#KNN
    k = 3
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train,y_train)
    prediction = model.predict(X_test)

    #Accuracy

    accuracy = accuracy_score(y_test,prediction)*100

#Neighbors

    distances , indexes = model.kneighbors(X_test)
    neighbours = []
    for i in range (len(X_test)):
        for j in range (k):
            neighbours.append({
                "Student" : id_test.iloc[i],
                "Neighbour" : id_train.iloc[indexes[i][j]],
                "Distance" : round (distances[i][j],2),
                "Result": y_train.iloc[indexes[i][j]]

        })

    output = pd.DataFrame({
        "Studernt_ID" : id_test.values,
        "Actual":y_test.values,
        "Predicted":prediction
    })

    return{
        "data":output,
        "accuracy":accuracy,
        "neighbors" : k,
        "neighbours": pd.DataFrame(neighbours)
    }