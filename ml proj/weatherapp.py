import numpy as np             
import pandas as pd 
from sklearn import tree              
from sklearn.preprocessing import OneHotEncoder 

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

encoder=OneHotEncoder() 
weather_encoder=encoder.fit_transform(weather)

clf=tree.DecisionTreeClassifier() 
clf=clf.fit(weather_encoder,labels)

a,b,c,d=input("weather"),input("humidity"),input("strom"),input("wind")

nc= [[a,b,c,d]]

nce=encoder.transform(nc)

pred=clf.predict(nce) 
pred[0]
