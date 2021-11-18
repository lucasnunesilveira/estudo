let isAtivo = false 
console.log(isAtivo);
isAtivo = true
console.log(isAtivo);
isAtivo = 1
console.log(!!isAtivo)
console.log(!isAtivo)
console.log(!true)//quando voce coloca o  {!} ele fica a negação da linguagem 

console.log("Os valores em baixo serão verdadeiros :")
console.log(!!3)
console.log(!!-1)// qualquer numero menos o numero 0 que se torna verdadeiro  ( negação duas vezes se torna verdadeiro )
console.log(!![]) //arrey ( para o python seria a lista )
console.log(!!{}) // objeto logico (para o python seria dicionario)
console.log(!!Infinity)// quando o valor se torna infinito 
console.log(!!(isAtivo = true))

console.log("Os valores seral falsos :")
console.log(!!0)
console.log(!!'')
console.log(!!null)
console.log(!!NaN)
console.log(!!undefined)
console.log(!!(isAtivo=false))// pra atribuição 

console.log("Os conceito de valores logicos (fraco )")
console.log(!!(''|| null || 0 || '  ')) // o valor || significa  V ( ou ) , quando coloca o valor do cada || X || ...
                                       // ... o X sera o objeto de analise( ou o prmeiro valor verdadeiro )

let idade = ""
console.log(idade || "sem idade")
