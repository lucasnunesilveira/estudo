/*java script aula 50 */
let a = 40

console.log(this.a)
console.log(global.a) // varivavel global  é igual ao windows no cosole 

global.b = 444
this.c = 1323
this.d = false
this.e = 'lalalal'

console.log(global.b)
console.log(this.c) 
console.log(module.exports.c) // module.exports é proporcional ao This 
console.log(module.exports) // ele printa todos ligado ao This 

//module.exports = {c : 1323 , d : false  , e : 'lalalal'} <<== geralmente sao criado assim as variaveis do modo This 


// cria uma variavel global 
abb = 333 // modo errado de fazer  
console.log(abb)


