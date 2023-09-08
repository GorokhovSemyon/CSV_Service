const passInput = document.getElementById('pass');
const repeatpassInput = document.getElementById('repeat-pass');
const checkboxInput = document.getElementById('ckb1');

function clickPass_1(element) {
  var eyeIcon = document.getElementById("eye-icon1");
  var passInput = document.getElementById("pass");

  if (eyeIcon.src.includes("eye-0.svg")) {
    eyeIcon.src = "../static/registration/img/eye-1.svg";
    passInput.type = "text";
  } else {
    eyeIcon.src = "../static/registration/img/eye-0.svg";
    passInput.type = "password";
  }
}

function clickPass_2(element) {
  var eyeIcon = document.getElementById("eye-icon2");
  var repeatPassInput = document.getElementById("repeat-pass");

  if (eyeIcon.src.includes("eye-0.svg")) {
    eyeIcon.src = "../static/registration/img/eye-1.svg";
    repeatPassInput.type = "text";
  } else {
    eyeIcon.src = "../static/registration/img/eye-0.svg";
    repeatPassInput.type = "password";
  }
}

function clickCheckbox_1(obj){
    let source = obj.src;
    if (source[source.length - 5] == "0") {
        obj.src = "../static/registration/img/ok-1.svg";
    }
    else{
        obj.src = "../static/registration/img/ok-0.svg";
    }   
}