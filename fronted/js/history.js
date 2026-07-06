const BASE_URL = "https://ai-healthcare-api.onrender.com";

// =============================
// Load Prediction History
// =============================

async function loadHistory() {

    try {

        const response = await fetch(
            `${BASE_URL}/predict/history`
        );

        const data = await response.json();

        let rows = "";

        data.forEach(item => {

            rows += `

            <tr>

                <td>${item.id}</td>

                <td>${item.patient_id}</td>

                <td>${item.prediction}</td>

                <td>${item.risk_level}</td>

                <td>${item.confidence}%</td>

                <td>${new Date(item.created_at).toLocaleString()}</td>

            </tr>

            `;

        });

        document.getElementById("historyTable").innerHTML = rows;

    }

    catch (error) {

        console.log(error);

        alert("Unable to Load Prediction History");

    }

}

// =============================
// Load on Page Open
// =============================

loadHistory();