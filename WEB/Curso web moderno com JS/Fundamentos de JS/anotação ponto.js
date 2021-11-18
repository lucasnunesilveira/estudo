//notação ponto Js 
// algo de acessar membro de uma função e de um objeto 
console.log(typeof console)
console.log(Math.ceil(3.4))//usando a anotação ponto pra definir pegar o pegar comparação ao objeto 
const objt1 = {}
objt1.nome = 'casa'
//objt2['nome'] = 'comida'
console.log(objt1)

function Obj(nome){
	this.nome = nome// pra criar um atributo publico usando do this. 
	this.exec = function(){
		console.log('Excccc')
	}
}

const objt2 = new Obj('cadeira')
const objt3 = new Obj('mesa')
console.log(objt2.nome)
console.log(objt3.nome)
objt3.exec()

// vc acessa o membro e objetos atraves do ponto  
