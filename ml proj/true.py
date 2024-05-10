import tkinter as tk
from tkinter import ttk
from sklearn import tree
from sklearn.preprocessing import OneHotEncoder
import joblib

class WeatherPredictionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Prediction App")

        # Load the trained model
        self.encoder = OneHotEncoder()
        self.clf = tree.DecisionTreeClassifier()
        self.load_model()

        # Create input widgets
        self.label_weather = ttk.Label(root, text="Weather:")
        self.entry_weather = ttk.Entry(root)

        self.label_humidity = ttk.Label(root, text="Humidity:")
        self.entry_humidity = ttk.Entry(root)

        self.label_storm = ttk.Label(root, text="Storm:")
        self.entry_storm = ttk.Entry(root)

        self.label_wind = ttk.Label(root, text="Wind:")
        self.entry_wind = ttk.Entry(root)

        # Create predict button
        self.predict_button = ttk.Button(root, text="Predict", command=self.predict)

        # Create prediction label
        self.label_prediction = ttk.Label(root, text="Prediction:")

        # Grid layout
        self.label_weather.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_weather.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
        self.label_humidity.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_humidity.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)
        self.label_storm.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_storm.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)
        self.label_wind.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_wind.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)
        self.predict_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.label_prediction.grid(row=5, column=0, columnspan=2, pady=10)

    def load_model(self):
        # Assuming the model is already trained and saved as clf.pkl
        self.clf = tree.DecisionTreeClassifier()
        self.encoder = OneHotEncoder()
        self.clf = joblib.load('clf.pkl')

    def predict(self):
        try:
            # Get input values from entry widgets
            weather = self.entry_weather.get()
            humidity = self.entry_humidity.get()
            storm = self.entry_storm.get()
            wind = self.entry_wind.get()

            # Make a prediction using the ML model
            input_data = [[weather, humidity, storm, wind]]
            input_encoded = self.encoder.transform(input_data).toarray()
            prediction = self.clf.predict(input_encoded)

            # Update the prediction label
            self.label_prediction.config(text=f"Prediction: {prediction[0]}")
        except ValueError:
            self.label_prediction.config(text="Invalid input. Please enter values.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherPredictionApp(root)
    root.mainloop()
