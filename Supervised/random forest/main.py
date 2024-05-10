from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Weather data
weather = [
    ['Sunny', 'Hot', 'High', 'Weak'],
    ['Sunny', 'Hot', 'High', 'Strong'],
    ['Overcast', 'Hot', 'High', 'Weak'],
    ['Rainy', 'Mild', 'High', 'Weak'],
    ['Rainy', 'Cool', 'Normal', 'Weak'],
    ['Rainy', 'Cool', 'Normal', 'Strong'],
    ['Overcast', 'Cool', 'Normal', 'Strong'],
    ['Sunny', 'Mild', 'High', 'Weak'],
    ['Sunny', 'Cool', 'Normal', 'Weak'],
    ['Rainy', 'Mild', 'Normal', 'Weak'],
    ['Sunny', 'Mild', 'Normal', 'Strong'],
    ['Overcast', 'Mild', 'High', 'Strong'],
    ['Overcast', 'Hot', 'Normal', 'Weak'],
    ["Rainy", "Mild", "High", "Strong"]
]

# Corresponding labels
labels = ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']

# Convert the string labels to numerical labels
le = LabelEncoder()
encoded_labels = le.fit_transform(labels)

# Combine weather data and encoded labels
data = list(zip(*weather))
X = list(zip(*data[:-1]))
y = encoded_labels

# Create a RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
clf.fit(X, y)

# Make predictions for ['Sunny', 'Hot', 'High', 'Weak']
new_data = [['Sunny', 'Hot', 'High', 'Weak']]
encoded_data = [le.transform(features) for features in new_data[0]]
prediction = clf.predict([encoded_data])

# Decode the prediction
decoded_prediction = le.inverse_transform(prediction)

print("Prediction:", decoded_prediction[0])
