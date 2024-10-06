// let hati = ['Titi', 'Saras', 'Purbalaksita', 'Agung','Herry', 'Sucipto']
// const newArray = hati.slice()
// newArray[6] = 'Argi'
// let nama = 'Purbalaksita'
// const Titi = hati.includes(nama)
// const posisiTiti = hati.indexOf(nama)
// let testing = document.createElement('h1')
// if (Titi) {
//     testing.innerHTML = `${nama} ada di nomor 
//     ${posisiTiti + 1}`
// }else {
//     testing.innerHTML = `${nama} tidak ada`
// }
// testing.style.fontSize = '50px'
// document.body.append(testing);
// console.log(hati)
// console.log(newArray)
// const arrayAwal = hati.shift()
// document.body.innerHTML = `Nama panggilannya ${arrayAwal}`

// const body = document.body
// body.append('SARAS')

// const h1 = document.createElement('h1')
// h1.textContent = 'i love you'

// const p = document.createElement('p')
// p.innerHTML = 'kamu cantik'

// const b = document.createElement('b')
// b.innerText = 'makasih Ti'

// body.append(h1)
// body.append(p)
// body.append(b)

// let budi = document.getElementById('budi')*/

// let btn1 = document.getElementById('btn1')
//  btn1.style.border = 'none';
//  btn1.style.fontSize = '100px'
// console.log(btn1)
// function gantiwarna () {
//     let x = document.createElement('p')
//     x.textContent = 'i love you'
//     document.body.append(x)
// }
// btn1.onmouseover = function () {
//     btn1.style.color ='black'
// }
// btn1.onmouseout = function () {
//     btn1.style.color ='red'
// }
// let x = document.createElement('h1')
// btn1.onmouseover = function () {
//     x.textContent = 'haloooooo bang'
//     document.body.append(x)
// }
// btn1.onmouseout = function () {
//     x.style.color = 'blue'
// }

// let argi = [
//     {
//         nama: 'Saras',
//         age : 17,
//     },
//     {
//         nama : 'Argi',
//         age : 18,
//     }
// ]

// argi.sort((a,b) => a.nama - b .nama).map((values) => console.log(values));


function multiplier (x) {
    return function(num) {
        return x * num;
    };
}

const jumlah = multiplier(2);
console.log(jumlah(10));

let x = (ayam) => {
    return ayam**ayam;
}


console.log(`ini adalh fungsi x ${x(10)}`)

