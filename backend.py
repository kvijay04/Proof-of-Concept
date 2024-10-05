import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings

#Code adapted from https://www.datacamp.com/tutorial/understanding-logistic-regression-python

with warnings.catch_warnings():
    warnings.filterwarnings("ignore")
    # Create and split X and y into training and testing sets
    X = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]])

    X = np.array(X).reshape((-1, 2))

    y = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]])

    y = np.array(y).reshape((-1, 1))

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=16)

    # instantiate the model (using the default parameters)
    logreg = LogisticRegression(random_state=16)

    # fit the model with data
    logreg.fit(X_train, y_train)

    y_pred = logreg.predict(X_test)
    print(y_pred)