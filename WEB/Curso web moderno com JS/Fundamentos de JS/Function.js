//função 00 - se o JS fosse um pais a Função seria o presidente - os objetos os "vice presidente"
console.log(typeof Object)
class Comida {}
console.log(typeof Comida)

//função 01

function ImprimirSoma (a,b)
{
	console.log(a + b)
}
ImprimirSoma(4,5)//imprimi dois numeros
ImprimirSoma(55)//ele vai somar 55 + indefine 
ImprimirSoma(55,1,44,55,33,44,55)// ele so vai somar os dois primeiros para imprimir na tela 
ImprimirSoma()//nao da erro , so vai da NaN
//Função retorno 
function soma (a,b = 0) // ele coloca b = 0 , quando não nao é definido o valor de b no final do programa .
{
	return a+b
}
console.log(soma(2,4))
console.log(soma(2))

//função 02

//armazenar uma função  em uma variavel 
const ImprimirSoma2 = function(a,b)
{
	console.log(a*b)
}
ImprimirSoma2 (2,3)

//Armazena uma função  arrow  em uma  varivel 

const Soma = (a,b) =>{
	return a+a+b
}
console.log(soma(2,4))

// retorno implicito 
const  subtração = (a,b) => a - b
console.log(subtração(5,2))

const imprimir3 = a => console.log(a)
imprimir3('laallala')