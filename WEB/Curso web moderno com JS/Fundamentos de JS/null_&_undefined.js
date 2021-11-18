let valor //O valor nao foi  inicializado , e foi declarado
console.log(valor)

valor = null 
// definiu mas como nulo , sem endereço de memoria , sem locação em nenhum ponto, usado quando quer zerar uma variavel tornando 
// ela "zero"
console.log(valor)
//console.log(valor.toString()) ele da erro pois quando to String vai ver a variavel ele retorna nulo 
const produto ={}
console.log(produto.preço)
console.log(produto)
produto.preço= 44.44
console.log(produto)
produto.preço = undefined // nao é uma ratic recomendada 
