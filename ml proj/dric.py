import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# Your data
weather = [
    ['Sunny', 'Hot', 'High', 'Weak'],
    # ... rest of the data
]

labels = ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes','Yes','No']

# One-hot encode the categorical features
encoder = OneHotEncoder()
weather_encoder = encoder.fit_transform(weather).toarray()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(weather_encoder, labels, test_size=0.2, random_state=42)

# Train the Decision Tree model
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)

# Predict on the test set
predictions = clf.predict(X_test)

# Check accuracy
accuracy = (predictions == y_test).mean()
print(f'Accuracy: {accuracy}')
