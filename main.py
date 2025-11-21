"""
Simple Random Forest Classifier on Iris Dataset
"""

# imports
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# load the iris dataset
data = load_iris()

print(type(data))

X = data.data
y = data.target

# split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# initialize the RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
# train the model
clf.fit(X_train, y_train)
# make predictions
y_pred = clf.predict(X_test)
# evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

joblib.dump(clf, "random_forest_model.joblib")
