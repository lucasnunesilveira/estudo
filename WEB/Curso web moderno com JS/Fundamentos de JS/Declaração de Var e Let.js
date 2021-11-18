//aulas de variavel 
// Declaração de variaveis com uma Var 01
{
	{
		{
			{
				{
					{
						{
							{
								var o_que = 'sera?'
							}
						}
					}
				}
			}
		}
	}
}
console.log(o_que)
function analise()
{
	var local=123
}
//console.log(analise) quando for declarado dentro da função  fica dentro da função fora da função nao pega 

// usando Var 02

// uma substituir a outra , isso faz com que a global pegue a interna , uma sub escreve a outra 
var number = 3
{
	var number =13
	console.log("dentro =",number)
}
console.log('fora =', number)

// 			usando o let

//01
var numero = 4
{
	let numero =2
	console.log("dentro => ",numero)
}
console.log("fora => ", numero)
//ele analise o scopo mais proximo a ele , visto que nao tem 
// ele pega o mais externo e se tiver ele pega o mais interno 
