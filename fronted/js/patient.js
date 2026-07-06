const BASE_URL = "https://ai-healthcare-api.onrender.com";

// ===============================
// Add Patient
// ===============================

document.getElementById("patientForm").addEventListener("submit", async function(e){

    e.preventDefault();

    const patient = {

        age: Number(document.getElementById("age").value),

        gender: document.getElementById("gender").value,

        blood_pressure: document.getElementById("blood_pressure").value,

        cholesterol: Number(document.getElementById("cholesterol").value),

        glucose: Number(document.getElementById("glucose").value),

        heart_rate: Number(document.getElementById("heart_rate").value)

    };

    try{

        const response = await fetch(`${BASE_URL}/patient/`,{

            method:"POST",

            headers:{

                "Content-Type":"application/json",
                "Authorization": `Bearer ${localStorage.getItem("token")}`

            },

            body:JSON.stringify(patient)

        });

        const data = await response.json();

        alert(data.message);

        document.getElementById("patientForm").reset();

        loadPatients();

    }

    catch(error){

        console.log(error);

        alert("Unable to Add Patient");

    }

});


// ===============================
// Get All Patients
// ===============================

async function loadPatients(){

    try{

        const response = await fetch(`${BASE_URL}/patient/`);

        const data = await response.json();

        let rows="";

        data.forEach(patient=>{

            rows+=`

            <tr>

                <td>${patient.id}</td>

                <td>${patient.user_id}</td>

                <td>${patient.age}</td>

                <td>${patient.gender}</td>

                <td>${patient.blood_pressure}</td>

                <td>${patient.cholesterol}</td>

                <td>${patient.glucose}</td>

                <td>${patient.heart_rate}</td>

                <td>

                    <button

                        class="delete-btn"

                        onclick="deletePatient(${patient.id})">

                        Delete

                    </button>

                </td>

            </tr>

            `;

        });

        document.getElementById("patientTable").innerHTML=rows;

    }

    catch(error){

        console.log(error);

    }

}


// ===============================
// Delete Patient
// ===============================

async function deletePatient(id){

    if(!confirm("Delete this patient?")){

        return;

    }

    try{

        const response=await fetch(

            `${BASE_URL}/patient/${id}`,

            {

                method:"DELETE"

            }

        );

        const data=await response.json();

        alert(data.message);

        loadPatients();

    }

    catch(error){

        console.log(error);

    }

}


// ===============================
// Load Data
// ===============================

loadPatients();