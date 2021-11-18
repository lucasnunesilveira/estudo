//chave e valor 
// par name and value 
const boas = 'ola jovem' // contexto lexico -> sao  ligação entre dois valores 
function Exec(){
	const boas = 'lalalla ' // constexto lexico 02 , o valores fica dentro da chave da função 
	return boas
}
//Objetos são grupos aninhados de pares nome / valor
const Cliente = // contexto lexico 03
{
	nome: 'João',
	idade : 33,
	peso : 90,
	endereco :{
		loucadorou :'Rua francisco pereira',
		numero: 332,
		tipo: 'casa',
		empresa: 'notavel'
	}
}
console.log(boas)
console.log(Exec())
console.log(Cliente)