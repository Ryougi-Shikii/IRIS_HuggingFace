document.getElementById("predict-btn").addEventListener("click", async () => {
    const sepal_length = parseFloat(document.getElementById("sepal_length").value);
    const sepal_width = parseFloat(document.getElementById("sepal_width").value);
    const petal_length = parseFloat(document.getElementById("petal_length").value);
    const petal_width = parseFloat(document.getElementById("petal_width").value);

    const response = await fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        })
    });

    const result = await response.json();

    document.getElementById("result").innerText =
        `Prediction: ${result.prediction}`;
});