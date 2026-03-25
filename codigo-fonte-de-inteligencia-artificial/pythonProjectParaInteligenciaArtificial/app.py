import tensorflow as tf
from flask import Flask, render_templates, request
import numpy as np

app = Flask(__name__)
model = tf.keras.models.load_model('model/iris_saved_model')

classes = ['Setosa', 'Versicolor','Virginica']

@app.route("/predict" , methods=["POST"])
def predict():
    sepal_length = float(request.form["sepal_length"])
    sepal_width = float(request.form["sepal_width"])
    petal_length = float(request.form["sepal_length"])
    petal_width = float(request.form["sepal_width"])

    X = np.array([[sepal_length, sepal_width ,petal_length,petal_width]], dtype=np.float32)

    #Inferência via SavedModel
    outputs = infer(tf.constant(X))

    #Pega o primeiro tensor de saída
    prediction = list(outputs.values())[0].numpy()

    predict_class = classes[np.argmax(prediction)]

    return render_templates(
        "index.html"
        , prediction = f"A especie prevista é: {predict_class}"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", post=5000, debug=False)