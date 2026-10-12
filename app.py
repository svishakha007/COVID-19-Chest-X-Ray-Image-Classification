from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from PIL import Image
import os

app = Flask(__name__)

# Load trained model
model = tf.keras.models.load_model("./covid19_model.keras")

# Class names
class_names = [
    "Covid",
    "Normal",
    "Viral Pneumonia"
]


def predict_image(image):
    image = image.convert("RGB")
    image = image.resize((128, 128))

    image_array = np.array(image)
    image_array = image_array / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    predictions = model.predict(image_array, verbose=0)

    predicted_index = np.argmax(predictions[0])
    predicted_class = class_names[predicted_index]
    confidence = predictions[0][predicted_index] * 100

    return predicted_class, confidence


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    confidence = None

    if request.method == "POST":

        if "image" not in request.files:
            return render_template(
                "index.html",
                error="Please upload an image."
            )

        file = request.files["image"]

        if file.filename == "":
            return render_template(
                "index.html",
                error="Please select an image."
            )

        try:
            image = Image.open(file)

            prediction, confidence = predict_image(image)

        except Exception as e:
            return render_template(
                "index.html",
                error=f"Error processing image: {str(e)}"
            )

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=False
    )
