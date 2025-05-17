import pandas as pd
import numpy as np
from sklearn import pipeline, preprocessing, metrics, model_selection, ensemble
from sklearn_pandas import DataFrameMapper
import joblib

def train_and_save_model():
    data = pd.read_csv('./media/excel/datafinal1.csv')
    mapper = DataFrameMapper([
        (['UEY', 'Major', 'Interested', 'Courses'], preprocessing.OrdinalEncoder()),
        (['e-learning process'], preprocessing.OneHotEncoder())
    ])
    pipeline_obj = pipeline.Pipeline([
        ('mapper', mapper),
        ("model", ensemble.RandomForestClassifier())
    ])
    attribute_cols = ['e-learning process', 'UEY', 'Major', 'Interested', 'Courses']
    X = data[attribute_cols]
    y = data.Target
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    pipeline_obj.fit(X_train, y_train)
    y_pred = pipeline_obj.predict(X_test)
    accuracy = metrics.accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy}")
    joblib.dump(pipeline_obj, './savedModels/model.joblib')

if __name__ == "__main__":
    train_and_save_model()
