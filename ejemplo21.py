estaciones=["primavera","invierno","verano","otoño"]

meses=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]

mes=str(input("Digite el nombre del mes:"))
dia=int(input("Digite el numero del año:"))

if(dia==1 or dia<=21 and mes ==meses[0]):
    print(f"En el mes de {meses[0]} la estacion es {estaciones[1]}")
     
elif(dia==21 or dia<=31 and mes ==meses[0]):
    print(f"En el mes de {meses[0]} la estacion es {estaciones[1]}")
    
elif(dia==32 or dia<=59 and mes ==meses[1]):
    print(f"En el mes de {meses[1]} la estacion es {estaciones[1]}")
    
elif(dia==60 or dia<=71 and mes ==meses[2]):
    print(f"En el mes de {meses[2]} la estacion es {estaciones[1]}")
    
elif(dia==72 or dia<=90 and mes ==meses[2]):
    print(f"En el mes de {meses[2]} la estacion es {estaciones[0]}")
    
elif(dia==91 or dia <=120 and mes ==meses[3]):
    print(f"En el mes de {meses[3]} la estacion es {estaciones[0]}")
    
elif(dia==121 or dia <=151 and mes ==meses[4]):
    print(f"En el mes de {meses[4]} la estacion es {estaciones[0]}")
    
elif(dia==152 or dia <=172 and mes==meses[5]):
    print(f"En el mes de {meses[5]} la estacion es {estaciones[0]}")
    
elif(dia==173 or dia <=181 and mes==meses[5]):
    print(f"En el mes de {meses[5]} la estacion es {estaciones[2]}")
    
elif(dia ==182 or dia <=212 and mes ==meses[6]):
    print(f"En el mes de {meses[6]} la estacion es {estaciones[2]}")
    
elif(dia ==213 or dia <=243 and mes ==meses[7]):
    print(f"En el mes de {meses[7]} la estacion es {estaciones[2]}")
    
elif (dia==244 or dia <=264 and mes ==meses[8]):
    print(f"En el mes de {meses[8]} la estacion es {estaciones[2]}")
    
elif(dia ==265 or dia <=273 and mes ==meses[8]):
    print(f"En el mes de {meses[8]} la estacion es {estaciones[3]}")
    
elif(dia ==274 or dia<=304 and mes ==meses[9]):
    print(f"En el mes de {meses[9]} la estacion es {estaciones[3]}")
    
elif(dia ==305 or dia<=334 and mes ==meses[10]):
    print(f"En el mes {meses[10]} la estacion es {estaciones[3]}")
    
elif(dia==335 or dia<=355 and mes ==meses[11]):
    print(f"En el mes de {meses[11]} la estacion es {estaciones[3]}")
    
elif(dia==356 or dia<=365 and mes ==meses[11]):
    print(f"En el mes de {meses[11]} la estacion es {estaciones[1]}")
    
else:
    print("Mes o numero del año  incorrecto")
    

    
    
