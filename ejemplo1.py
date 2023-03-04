import random 
#Represa Hidruituango

#Datos de entrada
nivelAgua=int(input("Digite el nivel maximo de agua:"))

#proceso
x=random.randint(0,1000)
while x<nivelAgua:
    x=random.randint(0,1000)
    if(x>=0 and x<=250):
        print(f"El nivel del agua es {x} y esta muy bajo")
    elif(x>250 and x <=nivelAgua):
        print(f"El nivel del gua es {x} y es un nivel normal")
else:
    print(f"Alerta maxima, el nivel del agua es {x}")
        