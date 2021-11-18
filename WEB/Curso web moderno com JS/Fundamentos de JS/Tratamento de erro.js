function trataerro (erro) {
	//throw new Erro('.....')
	throw {
		nome :erro.nome,
		msg : erro.message,
		date : new Date 
	}
}
function imprimirlala(obj)
{
	
	try{
		console.log(obj.name.toUpperCase() + '!!!!')
	} catch (e){
		trataerro (e)
	}finally {
		console.log("fim ")
	}

}
const obj = {nome : 'jubiluba '}
imprimirlala(obj) 