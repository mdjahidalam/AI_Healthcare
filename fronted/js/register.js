const BASE_URL = "http://127.0.0.1:8000";

const form = document.getElementById("registerForm");

form.addEventListener("submit", async function(e){

    e.preventDefault();

    const password = document.getElementById("password").value;

    const confirmPassword = document.getElementById("confirmPassword").value;

    if(password !== confirmPassword){

        document.getElementById("message").innerHTML =
        "Passwords do not match";

        return;

    }

    const user = {

        name: document.getElementById("name").value,

        email: document.getElementById("email").value,

        password: password

    };

    try{

        const response = await fetch(

            `${BASE_URL}/auth/register`,

            {

                method:"POST",

                headers:{

                    "Content-Type":"application/json"

                },

                body:JSON.stringify(user)

            }

        );

        const data = await response.json();

        if(response.ok){

            alert(data.message);

            window.location.href="index.html";

        }

        else{

            document.getElementById("message").innerHTML =
            data.detail;

        }

    }

    catch(error){

        console.log(error);

        document.getElementById("message").innerHTML =
        "Server Error";

    }

});