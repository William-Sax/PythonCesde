estaciones=["primavera","invierno","verano","otoño"]

meses=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]

pregunta=int(input("Digite el numero del año:"))

if(pregunta==1 or pregunta<=21):
    print(f"En el mes {meses[0]} la estacion es {estaciones[1]}")
    
elif(pregunta==21 or pregunta<=31):
    print(f"En el mes  {meses[0]} la estacion es {estaciones[1]}")
    
elif(pregunta==32 or pregunta<=59):
    print(f"En el mes {meses[1]} la estacion es {estaciones[1]}")
    
elif(pregunta==60 or pregunta<=71):
    print(f"En el mes {meses[2]} la estacion es {estaciones[1]}")
    
elif(pregunta==72 or pregunta<=90):
    print(f"En el mes {meses[2]} la estacion es {estaciones[0]}")
    
elif(pregunta==91 or pregunta <=120):
    print(f"En el mes {meses[3]} la estacion es {estaciones[0]}")
    
elif(pregunta==121 or pregunta <=151):
    print(f"En el mes {meses[4]} la estacion es {estaciones[0]}")
    
elif(pregunta==152 or pregunta <=172):
    print(f"En el mes {meses[5]} la estacion es {estaciones[0]}")
    
elif(pregunta==173 or pregunta <=181):
    print(f"En el mes {meses[5]} la estacion es {estaciones[2]}")
    
elif(pregunta ==182 or pregunta <=212):
    print(f"En el mes {meses[6]} la estacion es {estaciones[2]}")
    
elif(pregunta ==213 or pregunta <=243):
    print(f"En el mes {meses[7]} la estacion es {estaciones[2]}")
    
elif (pregunta==244 or pregunta <=264):
    print(f"En el mes {meses[8]} la estacion es {estaciones[2]}")
    
elif(pregunta ==265 or pregunta <=273):
    print(f"En el mes {meses[8]} la estacion es {estaciones[3]}")
    
elif(pregunta ==274 or pregunta<=304):
    print(f"En el mes {meses[9]} la estacion es {estaciones[3]}")
    
elif(pregunta ==305 or pregunta<=334):
    print(f"En el mes {meses[10]} la estacion es {estaciones[3]}")
    
elif(pregunta==335 or pregunta<=356):
    print(f"En el mes {meses[11]} la estacion es {estaciones[3]}")
    
elif(pregunta>=336 or pregunta<=365):
    print(f"En el mes {meses[11]} la estacion es {estaciones[1]}")
elif(pregunta >365):
    print("El numero digitado no fue el correcto")

