import pandas as pd

from sklearn.ensemble import RandomForestRegressor


class SepalWidthPredictor:
    TARGET = "SEPAL_WIDTH"
    FEATURES = ["SEPAL_LENGTH", "PETAL_LENGTH", "PETAL_WIDTH"]

    def fit(self, training):
        features = training[self.__class__.FEATURES]
        target = training[self.__class__.TARGET]
        predictor = RandomForestRegressor().fit(features, target)
        self.predictor = predictor
        return predictor

    
    def predict(self, test):
        return self.predictor.predict(test)

