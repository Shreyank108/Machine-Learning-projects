# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import OneHotEncoder

# weather = [
#     ['Sunny', 'Hot', 'High', 'Weak'],
#     ['Sunny', 'Hot', 'High', 'Strong'],
#     ['Overcast', 'Hot', 'High', 'Weak'],
#     ['Rainy', 'Mild', 'High', 'Weak'],
#     ['Rainy', 'Cool', 'Normal', 'Weak'],
#     ['Rainy', 'Cool', 'Normal', 'Strong'],
#     ['Overcast', 'Cool', 'Normal', 'Strong'],
#     ['Sunny', 'Mild', 'High', 'Weak'],
#     ['Sunny', 'Cool', 'Normal', 'Weak'],
#     ['Rainy', 'Mild', 'Normal', 'Weak'],
#     ['Sunny', 'Mild', 'Normal', 'Strong'],
#     ['Overcast', 'Mild', 'High', 'Strong'],
#     ['Overcast', 'Hot', 'Normal', 'Weak'],
#     ["Rainy", "Mild", "High","Strong"]
# ]

# labels = ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes','Yes','No']


# encoder=OneHotEncoder(handle_unknown='ignore')
# weather_encoder=encoder.fit_transform(weather)


# weather_encoder

# rf_classifer=RandomForestClassifier(n_estimators=100,random_state=101)

# rf_classifer=rf_classifer.fit(weather_encoder,labels)

# a,b,c,d=input("weather,Humidity,Stom,Damp").split()

# new_condition=[[a,b,c,d]] 
# new_condition_encoded = encoder.transform(new_condition)

# prediction = rf_classifer.predict(new_condition_encoded)
# prediction[0]

# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# # Sample data
# weather = [
#     ['Sunny', 'Hot', 'High', 'Weak'],
#     ['Sunny', 'Hot', 'High', 'Strong'],
#     ['Overcast', 'Hot', 'High', 'Weak'],
#     ['Rainy', 'Mild', 'High', 'Weak'],
#     ['Rainy', 'Cool', 'Normal', 'Weak'],
#     ['Rainy', 'Cool', 'Normal', 'Strong'],
#     ['Overcast', 'Cool', 'Normal', 'Strong'],
#     ['Sunny', 'Mild', 'High', 'Weak'],
#     ['Sunny', 'Cool', 'Normal', 'Weak'],
#     ['Rainy', 'Mild', 'Normal', 'Weak'],
#     ['Sunny', 'Mild', 'Normal', 'Strong'],
#     ['Overcast', 'Mild', 'High', 'Strong'],
#     ['Overcast', 'Hot', 'Normal', 'Weak'],
#     ["Rainy", "Mild", "High","Strong"]
# ]

# labels = ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes','Yes','No']


# # OneHotEncoder
# encoder = OneHotEncoder(handle_unknown='ignore')
# weather_encoded = encoder.fit_transform(weather)

# # Convert OneHotEncoder output to LabelEncoder
# label_encoder = LabelEncoder()
# labels_encoded = label_encoder.fit_transform(labels)

# # Random Forest Classifier
# rf_classifier = RandomForestClassifier(n_estimators=100, random_state=101)
# rf_classifier.fit(weather_encoded, labels_encoded)

# # Input for prediction
# a, b, c, d = input("weather, Humidity, Stom, Damp").split()
# new_condition = [[a, b, c, d]]

# # Transform new condition using the same encoders
# new_condition_encoded = encoder.transform(new_condition)

# # Predict using the Random Forest Classifier
# prediction_encoded = rf_classifier.predict(new_condition_encoded)

# # Convert prediction back to original label using inverse_transform
# prediction = label_encoder.inverse_transform(prediction_encoded)

# print("Predicted Label:", prediction[0])


from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Sample data
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
    ["Rainy", "Mild", "High","Strong"]
]

labels = ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes','Yes','No']

# LabelEncoder for each categorical feature
label_encoders = [LabelEncoder() for _ in range(len(weather[0]))]
weather_encoded = []

# Apply label encoding to each column in weather
for i in range(len(weather[0])):
    weather_encoded.append(label_encoders[i].fit_transform([row[i] for row in weather]))

# Transpose the weather_encoded list for proper format
weather_encoded = list(map(list, zip(*weather_encoded)))

# LabelEncoder for labels
label_encoder_labels = LabelEncoder()
labels_encoded = label_encoder_labels.fit_transform(labels)

# Random Forest Classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=101)
rf_classifier.fit(weather_encoded, labels_encoded)

# Input for prediction
a, b, c, d = input("weather, Humidity, Stom, Damp").split()
new_condition = [a, b, c, d]

# Apply label encoding to the new condition
new_condition_encoded = [label_encoders[i].transform([new_condition[i]])[0] for i in range(len(new_condition))]

# Predict using the Random Forest Classifier
prediction_encoded = rf_classifier.predict([new_condition_encoded])

# Convert prediction back to original label using inverse_transform
prediction = label_encoder_labels.inverse_transform(prediction_encoded)

print("Predicted Label:", prediction[0])
