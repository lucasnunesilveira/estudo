//Novo recuso do ES2015
// destructuring 
// operador de destruturação  01
const cliente = {
	nome:'Renata',
	idade:333,
	endereço: {
		lougradouro:'Rua joaquinas',
		numero:3000 ,
		cidade:'Camaragibe'
	}
}
const {nome,idade} = cliente
console.log(nome,idade, "\n")

const {nome: n, idade: i } = cliente
console.log(n,i,"\n")

const {sexo,filme = true} = cliente
console.log(sexo,filme)//udefined ( nao existe )

const { endereço :{lougradouro,numero, cep}} = cliente
console.log(lougradouro,numero,cep,"\n")
// quando o  pai não existe logo vc querer ver um filho que nao existe logo da erro

//destruturação  02 - operadores
const [a] = [10]// criação de array 
//tem que saber o que ta colocando pra saber se ta definindo um arrey ou usando o operado destrution 

console.log(a)

const[n1,n2,n3,n4,n5 = 0] = [10,3,4,5]//usando operado destrution 
console.log(n1,n2,n3,n4,n5)

const [ , [ ,  nota ]] = [[3,4,5,10] ,[2,3,5,2 ]] // não vale apena usar no dia a dia do trabalho 
console.log(nota)


//destruion 03 - Destruition
function rand ({min = 0 , max = 333}) { 
	const  valor = Math.random() * (max - min) + min 
	return Math.floor(valor)

}
const ob = {max :30 , min : 200 } // prestar atenção que aqui é ':'
console.log(rand(ob))

console.log(rand({min:220}))
console.log(rand({}))
//console.log(rand()) ele ta erro visto que so tem o argumento sem o objeto


//destructuring 04 
function rand2 ([min = 0 , max = 1000]){
	if (min > max)[min,max] = [max,min] 
		const valor  = Math.random() * (max - min) + min 
		return Math.floor(valor)
}

console.log(rand2([50 ,30]))
console.log(rand2([700]))
console.log(rand2([,5]))
console.log(rand2([]))

// na declaração do argumentod a função é  '='


