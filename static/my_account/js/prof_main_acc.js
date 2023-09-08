var my_email = document.getElementById('email').innerText; // Получить текстовое содержимое элемента email
var my_email_text = document.getElementById('email');
var email_length = my_email.length;

var stroka = "";
for (let i = 0; i < email_length; i++) {
  stroka = stroka + "*";
}
my_email_text.innerText = stroka;

function clickemail_1(obj) {
  var eyeIcon = document.getElementById("icon1");
  if (eyeIcon.src.includes("eye-0.svg")) {
    eyeIcon.src = "/static/my_account/img/eye-1.svg";
    my_email_text.innerText = my_email;
  } else {
    eyeIcon.src = "/static/my_account/img/eye-0.svg";
    my_email_text.innerText = stroka;
  }
}
