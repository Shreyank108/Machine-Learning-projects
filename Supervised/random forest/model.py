import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

def ml():
    # LabelEncoder for each categorical feature
    label_encoders = [LabelEncoder() for _ in range(4)]

    # Apply label encoding to each column in the entry fields
    a, b, c, d = a0.get(), a1.get(), a2.get(), a3.get()
    input_values = [a, b, c, d]
    input_encoded = [label_encoders[i].transform([input_values[i]])[0] for i in range(len(input_values))]

    # Transpose the input_encoded list for proper format
    input_encoded = list(map(list, zip(*input_encoded)))

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
        ["Rainy", "Mild", "High", "Strong"]
    ]

    # Apply label encoding to the sample data
    weather_encoded = []
    for i in range(len(weather[0])):
        weather_encoded.append(label_encoders[i].fit_transform([row[i] for row in weather]))

    # Transpose the weather_encoded list for proper format
    weather_encoded = list(map(list, zip(*weather_encoded)))

    # LabelEncoder for labels
    label_encoder_labels = LabelEncoder()
    labels = ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
    labels_encoded = label_encoder_labels.fit_transform(labels)

    # Random Forest Classifier
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=101)
    rf_classifier.fit(weather_encoded, labels_encoded)

    # Predict using the Random Forest Classifier
    prediction_encoded = rf_classifier.predict(input_encoded)

    # Convert prediction back to original label using inverse_transform
    prediction = label_encoder_labels.inverse_transform(prediction_encoded)

    label_prediction.config(text=f"Prediction: {prediction[0]}")

window = tk.Tk()
window.geometry("400x360")
window.title("ML Project")

animated_gif = Image.open("random forest\true.gif")
animated_gif_frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(animated_gif)]

canvas = tk.Canvas(window, width=800, height=600)
canvas.pack()

# Entry widgets
label1 = tk.Label(canvas, text="Weather", bg="white")
label1.place(x=50, y=50)
a0 = tk.Entry(canvas)
a0.place(x=150, y=50)

label2 = tk.Label(canvas, text="Humidity", bg="white")
label2.place(x=50, y=100)
a1 = tk.Entry(canvas)
a1.place(x=150, y=100)

label3 = tk.Label(canvas, text="Storm", bg="white")
label3.place(x=50, y=150)
a2 = tk.Entry(canvas)
a2.place(x=150, y=150)

label4 = tk.Label(canvas, text="Wind", bg="white")
label4.place(x=50, y=200)
a3 = tk.Entry(canvas)
a3.place(x=150, y=200)

label_prediction = tk.Label(canvas, text="Prediction: ", font=("Helvetica", 16), bg="white")
label_prediction.place(x=50, y=250)

button = tk.Button(canvas, text="Predict", command=ml)
button.place(x=150, y=300)

def update_frame(frame_index=0):
    frame = animated_gif_frames[frame_index]
    canvas.create_image(0, 0, anchor=tk.NW, image=frame)
    frame_index = (frame_index + 1) % len(animated_gif_frames)
    window.after(50, update_frame, frame_index)

update_frame()

window.mainloop()
