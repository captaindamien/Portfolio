radio_1 = document.getElementById('radio_1')
radio_2 = document.getElementById('radio_2')
next = document.getElementById('next')
before = document.getElementById('before')


next.onclick = function () {
    radio_2.style.display = 'block';
    radio_1.style.display = 'none';
    next.style.display = 'none';
    before.style.display = 'block'
}
before.onclick = function () {
    radio_2.style.display = 'none';
    radio_1.style.display = 'block';
    next.style.display = 'block';
    before.style.display = 'none'
}




