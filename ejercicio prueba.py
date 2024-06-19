
Nombres=[]
Cargo=[]
Sueldobruto=[]
descsalud=[]
descafp=[]
liquido=[]
tabla=""
impresion=[]
basededatos=[]
def validaciondedatos():
    while True:
        try:
            sueldobruentregado=float(input("ingrese los siguientes datos Sueldo bruto"))
        except ValueError:
            print("ingrese bien los datos solicitados")
        else:
            return Sueldobruto.append(round(sueldobruentregado,0))
        break
          
def descuentos():
    for plata in range(len(Sueldobruto)):
        descuentoafp=Sueldobruto[plata]*0.12
        descafp.append(round(descuentoafp,0))
        descuentosalud=Sueldobruto[plata]*0.07
        descsalud.append(round(descuentosalud,0))
        sueldoliquido=Sueldobruto[plata]-(descsalud[plata]+descafp[plata])
        liquido.append(round(sueldoliquido,0))
        
    
opcs=7  
while opcs!=4:     
    print("1.- Registrar trabajador")
    print("2.- Listar a todos los trabajadores")
    print("3.- Imprimir plantilla de sueldos")
    print("4.- Salir")
    opcs=int(input("ingrese unas de las siguientes opcione\n>>>"))
    match opcs:
        case 1:
            print(f"Ingrese los siguientes datos: Nombre y apellido / Cargo / Sueldo bruto")
            nombreyapellido=input("Ingrese el nombre y apellido:\n>>>")
            cargopingresado=input("Ingrese el Cargo:\n>>>")
            sueldoingresado=validaciondedatos()
            Nombres.append(nombreyapellido)
            Cargo.append(cargopingresado.upper())
            descuentos()
        
        case 2:
            print(f"Trabajador\tCargo\tSueldo bruto\tDesc. Salud\tDesc. AFP\tLiquido a pagar")
            for i in range(len(Sueldobruto)):
                print(f"{Nombres[i]}\t{Cargo[i]}\t{Sueldobruto[i]}\t\t{descsalud[i]}\t\t{descafp[i]}\t\t{liquido[i]}")
        
        case 3:
            #for cuchau in range(0,len(Cargo)):
                #"""if Cargo[cuchau]=="CEO" or Cargo[cuchau]=="DESARROLADOR" or Cargo[cuchau]=="ANALISTA":"""
            with open('plantilla.txt','w') as archivo:
                archivo.write(f"Trabajador\t|\tCargo\t|\tSueldo bruto\t|\tDesc. Salud\t|\tDesc. AFP\t|\tLiquido a pagar\n")
                for i in range(len(Cargo)):
                    if Cargo[i]=="CEO" or Cargo[i]=="DESARROLADOR" or Cargo[i]=="ANALISTA":
                        archivo.write(f"{Nombres[i]}\t|\t{Cargo[i]}\t|\t{Sueldobruto[i]}\t|\t{descsalud[i]}\t|\t{descafp[i]}\t|\t{liquido[i]}\n")
            print("archivo creado exitosamente")
                

        case 4:
            print("bye bye")