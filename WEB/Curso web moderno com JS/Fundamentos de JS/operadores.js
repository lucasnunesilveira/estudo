
							//Operadores matematica js
const a = 7 // o = fazendo o valor de atribuição 
let d = 34 
d += a // d = d+a (34 +7)
console.log(d)
d -= a // (41-7)
console.log(d)
d *= a // b = b*d (34*7)
console.log(d)
d /= 2 // d = d/2 (238 / 2 )
console.log(d)
d %= 2 // d = d % 2 ( resto da divisão por dois ) (119/2)
console.log(d)
	
							// operador Aritmeticos 
const [e,f,g,h] = [2,5,65,32]
const soma = e +f+ g +h
const sub = e - f - g - h 
const mult = e * f * g * h 
const rest = f % 2 
console.log("A soma foi : ", soma,"\nA subtração : " ,sub,"\nA multiplicação : ",mult, "\n O resto da divisão por dois é : ",rest)

							// Operadores Relacionais 
// operadores que so da duas resposta verdadeiro ou falso , 
console.log('1)' , '1'  == 1 ) // ele ta comparando o valor e nao o tipo do numero 1 
console.log('2)' , '1' === 1 ) // ele ta comparando o valor e o tipo da variavel , no caso ai seria um String e outro seria um numb
console.log('3)' , '3' != 3 ) // ele nesse caso nao ta comparando o tipo  , so o valor numerico , visto que os tipos são diferentes 
console.log('4)' , '3' !== 3)// nesse caso ele analisa o valor numerico como o tipo da variavel 

console.log('5)', 5<2) 
console.log('6)', 4>1)
console.log('7)', 3<=2)
console.log('8)', 3 >=2)

const d1 =  new Date(0)
const d2 = new Date(0)
console.log('9)', d1 === d2 ) //nao faz diferença usar o = ou == os pois ele ta comparando a referencia de memoria 
console.log('10)' , d1 == d2)
console.log('11)',d1.getTime() === d2.getTime()) // os dois sao numbs mesmo tipo e mesmo valor 
console.log('12)', undefined == null)
console.log('13)', undefined === null)

// 				Operadores logicos , Verdadeiro , FAlso ( bolean )
function compras (trabalho1,trabalho2){
		const ComprarMc = trabalho1  ||  trabalho2 // operador ou ( se for usando | ele comparar bit a bit )
		const Tv70 = trabalho1 && trabalho2 // operador E ( so é verdadeiro se os dois forem verdadeiros )
		//const Tv30 = !!(trabalho1 ^ trabalho2)//operador bit a bit 
		const  compraTv32 = trabalho1 != trabalho2 // operador exclusivo xor
		const  manterSaudavel = !ComprarMc // operador unario 
		return { ComprarMc , compraTv32 , Tv70 , manterSaudavel }
}
console.log(compras(true,true))
console.log(compras(true, false))
console.log(compras(false,false))
console.log(compras(false,true))

					//Operadores Unitario 
let num1 = 1
let num2 = 2
num1 ++  //pos fixada
console.log(num1)
--num1
console.log(num1)

console.log(++num1 === num2--) // verdadeiro pois ele foi analisado antes do decremento 
console.log(num1 === num2)


					// Operadores ternarios 
const resultado = nota => nota >= 7 ? 'Aprovado' : 'Reprovado'

console.log(resultado(7.6))
console.log(resultado(3.0))	