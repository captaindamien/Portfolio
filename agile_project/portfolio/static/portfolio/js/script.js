radio_1 = document.getElementById('radio_1')
radio_2 = document.getElementById('radio_2')
radio_3 = document.getElementById('radio_3')
radio_1_r = document.getElementById('radio-1')
radio_2_r = document.getElementById('radio-2')
radio_3_r = document.getElementById('radio-3')

next = document.getElementById('next')
before = document.getElementById('before')

r_all = [radio_1, radio_2, radio_3]
r_all_r = [radio_1_r, radio_2_r, radio_3_r]

modal_w = document.getElementById('modal_w').addEventListener("click", check_first);

function check_first() {
    radio_1_r.checked = true;
}

let cnt = 0
next.onclick = function () {
    cnt++

    for (let i = 0; i < r_all.length; i++) {
        r_all[i].style.display = 'none';
    }

    r_all[cnt].style.display = "block";

    for (let i = 0; i < r_all_r.length; i++) {
        r_all_r[i].checked = false;
    }

    r_all_r[cnt].checked = true;

    if (cnt == 2) {
        next.style.display = 'none';
        before.style.display = 'block'
    }

}

before.onclick = function () {
    cnt--
    for (let i = 0; i < r_all.length; i++) {
        r_all[i].style.display = 'none';
    }

    r_all[cnt].style.display = "block";

    for (let i = 0; i < r_all_r.length; i++) {
        r_all_r[i].checked = false;
    }

    r_all_r[cnt].checked = true;

    if (cnt == 0) {
        next.style.display = 'block';
        before.style.display = 'none'
    }

}


// next.onclick = function () {
//     radio_2.style.display = 'block';
//     radio_2_r.checked = true;
//     radio_1_r.checked = false;
//     radio_1.style.display = 'none';
//     next.style.display = 'none';
//     before.style.display = 'block'
// }
// before.onclick = function () {
//     radio_2.style.display = 'none';
//     radio_1.style.display = 'block';
//     radio_1_r.checked = true;
//     radio_2_r.checked = false;
//     next.style.display = 'block';
//     before.style.display = 'none'
// }




