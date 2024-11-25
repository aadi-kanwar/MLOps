
# Necessary imports
from sklearn. linear_model import LogisticRegression
from sklearn. model_selection import GridSearchCV
import numpy as np
from sklearn. datasets import make_classification

X, y = make_classification (
    n_samples=1000, n_features=20, n_informative=10, n_classes=2, random_state=42)

# Creating the hyperparameter grid
c_space = np. logspace(-5, 8, 15)
param_grid = {'C': c_space}

# Instantiating logistic regression classifier
logreg = LogisticRegression ()

# Instantiating the GridSearchCV object
logreg_cv = GridSearchCV (logreg, param_grid, cv=5)

# Assuming X and y are your feature matrix and target variable
# Fit the GridSearchCV object to the data
logreg_cv.fit (X, y)

# Print the tuned parameters and score
print("Tuned Logistic Regression Parameters: {}".format(logreg_cv.best_params_))
print("Best score is {}".format(logreg_cv.best_score_))