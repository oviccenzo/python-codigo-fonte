import tensorflow as tf
from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

# Carrega SavedModel
model = tf.saved_model.load("model/iris_saved_model")

# Função de inferência
infer = model.signatures["serving_default"]

classes = ["Setosa", "Versicolor", "Virginica"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    sepal_length = float(request.form["sepal_length"])
    sepal_width = float(request.form["sepal_width"])
    petal_length = float(request.form["petal_length"])
    petal_width = float(request.form["petal_width"])

    X = np.array([[sepal_length, sepal_width, petal_length, petal_width]], dtype=np.float32)

    # Inferência via SavedModel
    outputs = infer(tf.constant(X))

    # Pega o primeiro tensor de saída
    prediction = list(outputs.values())[0].numpy()

    predicted_class = classes[np.argmax(prediction)]

    return render_template(
        "index.html",
        prediction=f"A espécie prevista é: {predicted_class}"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)