const passInput = document.getElementById('pass');

function clickPass_1(element) {
  var eyeIcon = document.getElementById("eye-icon1");
  var passInput = document.getElementById("pass");

  if (eyeIcon.src.includes("eye-0.svg")) {
    eyeIcon.src = "../static/registration/img/login_eye-1.svg";
    passInput.type = "text";
  } else {
    eyeIcon.src = "../static/registration/img/login_eye-0.svg";
    passInput.type = "password";
  }
}