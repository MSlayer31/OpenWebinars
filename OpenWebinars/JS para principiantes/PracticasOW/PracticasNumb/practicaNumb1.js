/*let pagoTotal = 102;
let personas = 6;

pagoXPersona = pagoTotal / personas;

const resultado = "Cada persona debe pagar "+ pagoXPersona+ "€";

console.log(resultado)*/

var precioMovil = 300;
var precioCascos = 30;
var precioFunda = 10;

carritoCompra = precioMovil + precioCascos + precioFunda;

var descuento = carritoCompra * 0.1;

console.log("El carrito de la compra cuesta "+carritoCompra+"€");
console.log("Restando el decuento del 10%, es decir ("+descuento+"€)");

precioTotal = carritoCompra - descuento;

console.log("El precio total del carrito se queda en "+precioTotal+"€");