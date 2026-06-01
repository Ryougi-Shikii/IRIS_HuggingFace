from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)
model = load_model("ok.keras")

def iris_pre(sepal_length, sepal_width, petal_length, petal_width):
    output = ['Setosa', 'Versicolor', 'Virginica']
    inp = np.array([[
        float(sepal_length),
        float(sepal_width),
        float(petal_length),
        float(petal_width)
    ]])
    result = model.predict(inp, verbose=0)
    return output[np.argmax(result, axis=1)[0]]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    prediction = iris_pre(
        data["sepal_length"],
        data["sepal_width"],
        data["petal_length"],
        data["petal_width"]
    )
    return {"prediction": prediction}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    