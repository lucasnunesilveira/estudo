                                        //Aula 17 (tipos = Number)
console.log('32' + 4) // ele vai concatenar pois o String ganhar do numerico

const idade = 34
const idade2 = Number('30')
console.log(idade,idade2)
console.log(Number.isInteger(idade))
console.log(Number.isInteger(idade2))
const altura1 = 30
const altura2 = 2 
const total = altura1 * idade + altura2 *idade2 
const media = total / (idade+idade2)

console.log(media.toFixed(4))
console.log(media.toString())
console.log(media.toString(2)) // passar para o binario 
console.log(media.toString(16)) //passa pro hexadecimal
console.log(media.toString(4))  // quartedo
console.log(media.toString(8)) //octardecimal
console.log(typeof media)
console.log(typeof Number)

                                                        //Aula 18
                                
console.log(7 / 0)
console.log("30" / 3 )
console.log(!"show!!" *4)
console.log(0.1+0.4)
//console.log(10.toString())    // vai da erro pq ele  nao condiz com a função 
console.log((10.443).toFixed(1))

                                                        //aula 19 Math
 const raio = 2 
 const area = Math.PI * Math.pow(raio , 2)
 console.log(area.toFixed(2))
 console.log(typeof Math)