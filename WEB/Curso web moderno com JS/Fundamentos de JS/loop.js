//			Loops
//01 loop com var 
for (var i = 0; i <= 10; i++) 
{
	console.log(i)
}
console.log("o numero é :",i)// o que ele imprimir o valor fora do laço
//loop2
 for (let num=0; num <=10; num++)
 {
 	console.log(num)
 }
 //console.log(num) Ele sendo executado por fora da erro visto que o let so pega no scopo dentro do for dele 
 // diferende do var que pega dentro e fora do scopo 

 //loop 03
 const lala =[]
 for (let i = 0 ; i < 10 ; i++)
 {
 	lala.push(function(){
 		console.log(i)
 	})
 }
 lala[3]()// quando o  for ser com let ele "salva" o numero como fosse uma retirada de uma list 
 lala[5]()// a variavel não é respeitada visto que quando ta em var ele sobre escreve */

