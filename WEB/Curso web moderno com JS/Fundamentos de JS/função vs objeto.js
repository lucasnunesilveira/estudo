// função vs obejto ( comparativo )
console.log(typeof Object) // ele não estar estanciado 
console.log(typeof new Object) // aqui ele ta estanciado , ele ja mudar o type , criando objeto 


const User = function(){}
console.log(typeof User)
console.log(typeof new User)

class Preco{} // ES 2015 (ES6)
console.log(typeof Preco)
console.log(typeof new Preco)