// ===============================
// API BASE URL
// ===============================

const BASE_URL = "https://ai-healthcare-api.onrender.com";

// ===============================
// Dashboard Summary
// ===============================

async function loadDashboard() {

    try {

        const response = await fetch(
            `${BASE_URL}/dashboard/summary`
        );

        const data = await response.json();

        document.getElementById("users").innerHTML =
            data.total_users;

        document.getElementById("patients").innerHTML =
            data.total_patients;

        document.getElementById("predictions").innerHTML =
            data.total_predictions;

        document.getElementById("risk").innerHTML =
            data.high_risk;

    }

    catch (error) {

        console.log(error);

        alert("Dashboard Loading Failed");

    }

}

// ===============================
// Pie Chart
// ===============================

async function loadChart() {

    try {

        const response = await fetch(
            `${BASE_URL}/dashboard/statistics`
        );

        const data = await response.json();

        const ctx = document
            .getElementById("riskChart")
            .getContext("2d");

        new Chart(ctx, {

            type: "pie",

            data: {

                labels: [

                    "High Risk",

                    "Low Risk"

                ],

                datasets: [

                    {

                        data: [

                            data.high_risk,

                            data.low_risk

                        ],

                        backgroundColor: [

                            "#ff4d4d",

                            "#4CAF50"

                        ]

                    }

                ]

            },

            options: {

                responsive: true,

                plugins: {

                    legend: {

                        position: "bottom"

                    }

                }

            }

        });

    }

    catch (error) {

        console.log(error);

    }

}

// ===============================
// Recent Prediction Table
// ===============================

async function loadRecentPredictions() {

    try {

        const response = await fetch(
            `${BASE_URL}/dashboard/recent-predictions`
        );

        const data = await response.json();

        let rows = "";

        data.forEach((item) => {

            rows += `

            <tr>

                <td>${item.id}</td>

                <td>${item.patient_id}</td>

                <td>${item.prediction}</td>

                <td>${item.risk_level}</td>

                <td>${item.confidence}%</td>

            </tr>

            `;

        });

        document.getElementById(
            "predictionTable"
        ).innerHTML = rows;

    }

    catch (error) {

        console.log(error);

    }

}

// ===============================
// Logout
// ===============================

function logout() {

    localStorage.removeItem("token");

    window.location.href = "index.html";

}

// ===============================
// Load Everything
// ===============================

loadDashboard();

loadChart();

loadRecentPredictions();