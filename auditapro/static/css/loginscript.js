var username = document.getElementById("username").value;
var password = document.getElementById("password").value;
function submitinfo(){
    username = document.getElementById("username").value;
    password = document.getElementById("password").value;
    if (username == "Nombre" && password=="12345"){
        alert("Access Granted");
        window.location.replace("MainMenu.html");
    } else{
        alert("Access Denied");
    }
}
