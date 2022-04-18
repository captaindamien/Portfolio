pass1 = document.getElementById('id_password1')
pass2 = document.getElementById('id_password2')
alert_p = document.getElementById('alert')
reg_submit = document.getElementById('reg_submit')

reg_submit.disabled = true;
$('input#id_password1').on('input', validPassword);
$('input#id_password2').on('input', compare_pass)


function validPassword() {
    if (pass1.value != pass2.value) {
        reg_submit.disabled = true;
    } else {
        reg_submit.disabled = false;
    }
    let re = new RegExp(/^.*[a-zA-Z]+.*$/, "g");
    let digts = new RegExp(/^.*[0-9]+.*$/, "g");
    let symbls = new RegExp(/^.*[!@#$%^&*()_§]+.*$/, "g");
    let pv = pass1.value
    if (re.test(pv) && digts.test(pv) && symbls.test(pv) && pv.length > 7) {
        alert_p.innerHTML = ""
    } else {
        alert_p.innerHTML = "password is not valid"
    }
    console.log(pv)

}


function compare_pass() {
    if (pass1.value != pass2.value) {
        alert_p.innerHTML = "passwords are different";
    } else {
        alert_p.innerHTML = "";
        reg_submit.disabled = false;
    }
}