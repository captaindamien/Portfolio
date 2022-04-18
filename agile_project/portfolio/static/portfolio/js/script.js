radio_1 = document.getElementById('radio_1')
radio_2 = document.getElementById('radio_2')
radio_1_r = document.getElementById('radio-1')
radio_2_r = document.getElementById('radio-2')
next = document.getElementById('next')
before = document.getElementById('before')

modal_w = document.getElementById('modal_w').addEventListener("click", check_first);

function check_first() {
    radio_1_r.checked = true;
}

next.onclick = function () {
    radio_2.style.display = 'block';
    radio_2_r.checked = true;
    radio_1_r.checked = false;
    radio_1.style.display = 'none';
    next.style.display = 'none';
    before.style.display = 'block'
}
before.onclick = function () {
    radio_2.style.display = 'none';
    radio_1.style.display = 'block';
    radio_1_r.checked = true;
    radio_2_r.checked = false;
    next.style.display = 'block';
    before.style.display = 'none'
}




