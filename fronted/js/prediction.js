const BASE_URL = "https://ai-healthcare-api.onrender.com";

// =============================
// Heart Disease Prediction
// =============================

document.getElementById("predictionForm").addEventListener("submit", async function (e) {

    e.preventDefault();

    const predictionData = {

        patient_id: Number(document.getElementById("patient_id").value),

        age: Number(document.getElementById("age").value),

        sex: Number(document.getElementById("sex").value),

        cp: Number(document.getElementById("cp").value),

        trestbps: Number(document.getElementById("trestbps").value),

        chol: Number(document.getElementById("chol").value),

        fbs: Number(document.getElementById("fbs").value),

        restecg: Number(document.getElementById("restecg").value),

        thalach: Number(document.getElementById("thalach").value),

        exang: Number(document.getElementById("exang").value),

        oldpeak: Number(document.getElementById("oldpeak").value),

        slope: Number(document.getElementById("slope").value),

        ca: Number(document.getElementById("ca").value),

        thal: Number(document.getElementById("thal").value)

    };

    try {

        const response = await fetch(`${BASE_URL}/predict/heart`, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(predictionData)

        });

        const result = await response.json();

        if (response.ok) {

            // Prediction
            document.getElementById("predictionResult").innerHTML =
                result.prediction;

            // Risk
            document.getElementById("riskLevel").innerHTML =
                result.risk_level;

            // Confidence
            document.getElementById("confidence").innerHTML =
                result.confidence + "%";

            // High Risk
            if (result.risk_level === "High") {

                document.getElementById("predictionResult").style.color = "red";

                document.getElementById("riskLevel").style.color = "red";

                document.getElementById("recommendation").innerHTML =
                    "Please consult a Cardiologist immediately.";

            }

            // Low Risk
            else {

                document.getElementById("predictionResult").style.color = "green";

                document.getElementById("riskLevel").style.color = "green";

                document.getElementById("recommendation").innerHTML =
                    "Maintain a healthy lifestyle and regular exercise.";

            }

        }

        else {

            alert(result.detail);

        }

    }

    catch (error) {

        console.log(error);

        alert("Prediction Failed");

    }

});