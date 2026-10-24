import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
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

    model = GaussianNB()

    model.fit(
        X_train,
        y_train
    )
    result = model.predict(
        X_test
    )
    probability = model.predict_proba(
        X_test
    )

    accuracy = accuracy_score(
        y_test,
        result
    )*100  

    output = pd.DataFrame({
        "Actual":y_test.values,
        "Predicted":result
    })

    for i, class_name in enumerate(
        model.classes_
    ):
        output[
            class_name + "_Probability"
        ]=(
            probability[:,1]*100
        ).round(2)

    return{
        "data":output,
        "accuracy":accuracy,
        "classes":list(model.classes_)
    }