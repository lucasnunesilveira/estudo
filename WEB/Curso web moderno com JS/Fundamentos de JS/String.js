const name = "lucas nunes"
console.log(name.charAt(4))
console.log(name.charAt(455))// quando ele passa dos indice existente no computador ele retorna zero 
console.log(name.charCodeAt(2)) // ele pegar o valor na tabela ASCII
console.log(name.indexOf('s'))// ele conta onde ta possição da primeira letra , como a primeiro 'S' foi no index 4

console.log(name.substring(3)) // ele coloca do indice 3 ate o final da palavra 
console.log(name.substring(0,3))// ele da um ranger de do 0 ao 3 

console.log('lalalalala  '.concat(name).concat(" bru bru "))// serve para concatenar
console.log('lalalalala  ' + name +" bru bru ")// concatena 
console.log(name.replace(2,'X'))//ele troca do index 2 coloca a letra A .
console.log('joao , maria , francisco'.split(','))// ele faz uma lista dos itens 
