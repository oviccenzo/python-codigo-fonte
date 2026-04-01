from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "API funcionando!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    return jsonify({"mensagem": "Recebido com sucesso!", "dados": data})

if __name__ == "__main__":
    app.run(debug=True)