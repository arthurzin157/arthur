nome = input("qual eo seu nome? ")
temperatura = float(input("qual e a temperatura? "))


if 20 <= temperatura <= 40:
   print(f"{nome} Quente")

elif 20>temperatura <=40:
   print(f"{nome} frio")

elif 0< temperatura <5:
   print(f"{nome} gelado") 

else:
   print("noix morre")

if temperatura >=20 and temperatura<=40:
   print("esta quente ")

