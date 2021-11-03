#Indice de IMC
peso = float(input("Indique su peso (kg): "))
altura = float(input("Indique su altura (mts): "))
imc = peso / altura**2
if imc < 18.5:
   print("Bajo peso")
elif imc >= 18.5 and imc < 25:
   print("Normal")
elif imc >=25 and imc < 30:
   print("Sobrepeso")
elif imc >=30 and imc < 35:
   print("Obesidad Leve")
elif imc >= 35 and imc < 40:
   print("Obesidad Media")
else:
   print("Obesidad Mórbida")