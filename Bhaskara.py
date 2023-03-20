import math

#Inserir valores 
a = float(input("Entre com o valor de A:"))
b = float(input("Entre com o valor de B:"))
c = float(input("Entre com o valor de C:"))

#Calculando o valor de Delta 
delta = b**2-4*a*c

#Calculando o valor de Xone e Xtwo
if(delta>=0):
  xone = (-b+ math.sqrt(delta))/(2*a)
  xtwo = (-b- math.sqrt(delta))/(2*a)

#Imprindo o valor de Delta 
print("Delta:",delta)

#Imprindo o valores de xone e xtwo
if(delta==0):
  print("Xone é igual a Xtwo:", xone)

elif(delta<0):
  print("Nao possui raizes")

else:
  print("Xone:", xone)
  print("Xtwo:", xtwo)

  


