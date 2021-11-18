#3.9
import os
dias = int(input("Quantos dias : "))
horas = int(input("Quantas horas:"))
minutos = int(input("Quantos minutos:"))
segundos = int(input("Quantos segundos:"))
segundos_total = (dias*86.400) + (horas*3600) + (minutos*60) + segundos
print("O total de segundos são :{:.4f}".format(segundos_total))
