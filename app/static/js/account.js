var Login = document.getElementById("LoginForm");
var Register = document.getElementById("RegForm");
var Indicator = document.getElementById("Indicator");

function register() {
    Login.style.transform = "translateX(0px)";
    Register.style.transform = "translateX(0px)";
    Indicator.style.transform = "translateX(100px)";
    
}
function login() {
    Login.style.transform = "translateX(300px)";
    Register.style.transform = "translateX(300px)";
    Indicator.style.transform = "translateX(0px)";
}