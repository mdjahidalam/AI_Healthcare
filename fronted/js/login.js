const form = document.getElementById("loginForm");

form.addEventListener("submit", async (e) => {

    e.preventDefault();

    const email = document.getElementById("email").value;

    const password = document.getElementById("password").value;

    const response = await fetch(
        "https://ai-healthcare-api.onrender.com/auth/login",
        {

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({

                email,

                password

            })

        }
    );

    const data = await response.json();

    if(response.ok){

        localStorage.setItem(
            "token",
            data.access_token
        );
        localStorage.setItem(
            "user_id",
            data.user_id
        );
        localStorage.setItem(
            "name",
            data.name
        );

        window.location.href="dashboard.html";

    }

    else{

        document.getElementById(
            "message"
        ).innerHTML=data.detail;

    }

});