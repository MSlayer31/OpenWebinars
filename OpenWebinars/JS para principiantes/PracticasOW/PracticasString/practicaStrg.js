/*var fraseSplit = "Pueblo: Castellón, Calle: La Senyera, Puerta: 12, Piso: 2B";
console.log(fraseSplit.split(", "));*/

const nombre = "Cristina"
const juego = "Link's Awakening"
const descuento = 20
const textoNewsLetter =     `Hola ${nombre}, te hacemos un descuento del ${descuento}% por el ${juego},
Un saludo crack`

document.querySelector('.textoNewsLetterHTML').innerHTML = textoNewsLetter;

