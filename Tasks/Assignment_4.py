import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix
import warnings
warnings.filterwarnings('ignore')

# Load dataset
cars_ds = pd.read_csv('cars.csv', delimiter=';')  # Adjust the delimiter as needed
print("Initial data preview:")
print(cars_ds.head())

# Assume the last column is the target and the rest are features
X = cars_ds.iloc[:, :-1]  # Features
y = cars_ds.iloc[:, -1]   # Target

# Identify categorical columns (exclude numeric columns)
categorical_features = X.select_dtypes(include=[object]).columns.tolist()

# Create a column transformer with OneHotEncoder for categorical data
column_transformer = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), categorical_features)
    ],
    remainder='passthrough'
)

# Apply transformation to feature data
X_encoded = column_transformer.fit_transform(X)

# Convert sparse matrix to dense if necessary for GaussianNB
X_dense = X_encoded.toarray()

# Count each class frequency and filter out classes with less than 2 instances
class_counts = pd.value_counts(y)
y = pd.Series(y)
X_filtered = X_dense[y.isin(class_counts[class_counts > 1].index)]
y_filtered = y[y.isin(class_counts[class_counts > 1].index)]

# Splitting the filtered data with stratification if possible
if len(y_filtered.unique()) > 1:  # Ensure there are at least two classes for stratification
    X_train, X_test, y_train, y_test = train_test_split(X_filtered, y_filtered, test_size=0.20, random_state=0, stratify=y_filtered)
else:
    X_train, X_test, y_train, y_test = train_test_split(X_filtered, y_filtered, test_size=0.20, random_state=0)

# Decision Tree Classifier
dt_classifier = DecisionTreeClassifier()
dt_classifier.fit(X_train, y_train)
dt_pred = dt_classifier.predict(X_test)
dt_accuracy = accuracy_score(y_test, dt_pred)
print("\nDecision Tree Classifier:")
print("Accuracy:", dt_accuracy)
print("Confusion Matrix:\n", confusion_matrix(y_test, dt_pred))

# K-Nearest Neighbors Classifier
knn_classifier = KNeighborsClassifier()
knn_classifier.fit(X_train, y_train)
knn_pred = knn_classifier.predict(X_test)
knn_accuracy = accuracy_score(y_test, knn_pred)
print("\nK-Nearest Neighbors Classifier:")
print("Accuracy:", knn_accuracy)
print("Confusion Matrix:\n", confusion_matrix(y_test, knn_pred))

# Gaussian Naive Bayes Classifier
nb_classifier = GaussianNB()
nb_classifier.fit(X_train, y_train)
nb_pred = nb_classifier.predict(X_test)
nb_accuracy = accuracy_score(y_test, nb_pred)
print("\nGaussian Naive Bayes Classifier:")
print("Accuracy:", nb_accuracy)
print("Confusion Matrix:\n", confusion_matrix(y_test, nb_pred))
