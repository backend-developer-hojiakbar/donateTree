let tekst;
let btn1 = document.getElementById('inlineRadio1')
let btn2 = document.getElementById('inlineRadio2')
let btn3 = document.getElementById('inlineRadio3')
let checked = document.getElementById('checked1')
let checked2 = document.getElementById('checked2')
let count = document.getElementById('countTree')

document.getElementById('totalCost').textContent = document.getElementById('price-cost').textContent
checked.addEventListener('click', alerting1)
checked2.addEventListener('click', alerting1)
btn1.addEventListener('click', alerting)
btn2.addEventListener('click', alerting)
btn3.addEventListener('click', alerting)

function alerting() {
    tekst = parseFloat(document.getElementById('totalCost').textContent)
    tekst += 10000;
    document.getElementById('totalCost').textContent = tekst
}

function alerting1() {
    tekst = parseFloat(document.getElementById('totalCost').textContent)
    tekst += 30000;
    document.getElementById('totalCost').textContent = tekst
}