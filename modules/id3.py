import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def run():
    data=pd.read_csv("data/student_data.csv")

    features = ["Study_Hours","Attendance","Assignment_Score","Internal_Marks","Previous_Score"]

    X=data[features]
    y=data["Result"]

    X_train,X_test,y_train,y_test =train_test_split(
        X,
        y,
        test_size=0.30,
        random_state=42
    )

    model = DecisionTreeClassifier(
        criterion="entropy",
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )
    result = model.predict(
        X_test
    )

    accuracy = accuracy_score(
        y_test,
        result
    )*100

    importance = pd.DataFrame({
        "Attribute":features,
        "Information_Gain_Importance":
        model.feature_importances_
    })

    importance[
        "Imformation_Gain_Importance"
    ] = importance[
        "Information_Gain_Importance"
    ].round(5)

    importance=importance.sort_values(
        "Information_Gain_Importance",
        ascending=False
    )

    root_index = model.tree_.feature[0]

    if root_index >= 0:
        root_attribute=features[root_index]
    else:
        root_attribute = "N/A"    

    output = pd.DataFrame({
        "Actual":y_test.values,
        "Predicted":result
    })

    return{
        "data":output,
        "accuracy":accuracy,
        "importance":importance,
        "root_attricute":root_attribute,
        "criterion":"Entropy"
    }