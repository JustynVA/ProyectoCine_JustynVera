#PROYECTO PEQUEÑO DE COMPRA DE ENTRADAS PARA UN CINE
cupos = 10
entradas_vendidas = 0
dinero_recaudado = 0
opcion = 0
pelicula = 0 

while opcion != 3:
    
    print("--Bienvendido a Supercines: Mucho mas que un cine--")
    print("1.Comprar entrada")
    print("2.Ver asientos disponibles")
    print("3.Salir")
    opcion = int(input("Escriba su opcion: "))
    
    if opcion == 1:
        print("--Cartelera--")
        print("GRAN RE-ESTRENO: AVENGERS ENDGAME")
        print("4.Avengers: Endgame Encore")
        print("5.Resident Evil: Noche Cero")
        print("6.Hechizada de amor")
        print("7.Volver al menu")
        pelicula = int(input("Escoga su pelicula: ")) 
        if pelicula == 4:
            edad = int(input("Escriba su edad: "))
            estudiante = str(input("Es estudiante? (si/no): "))
            entradas = int(input("Seleccione sus entradas a comprar: "))
            if entradas <= 0:
                print("Cantidad no valida, porfavor escoga correctamente")
            elif entradas > cupos:
                print("No hay asientos disponibles, solo hay ", cupos, "disponibles")
            else:
                precio = 8.00
                if edad < 12:
                    descuento = 0.50
                elif edad >= 12 and edad <= 17:
                    descuento = 0.25
                elif edad >= 18 and estudiante == "si":
                    descuento = 0.20
                else:
                    descuento = 0
            
                precio_final = precio * (1 - descuento)
                total = precio_final * entradas
                cupos = cupos - entradas
                entradas_vendidas = entradas_vendidas + entradas
                dinero_recaudado = dinero_recaudado + total
            
                print("--FACTURA SUPERCINES--")
                print("Entradas compradas: ", entradas)
                print("total a pagar: ", (total))
                print("Asientos: ", cupos)
                print("Pelicula: Avengers EndGame Encore")
        elif pelicula == 5:
            edad = int(input("Escriba su edad: "))
            estudiante = str(input("Es estudiante? (si/no): "))
            entradas = int(input("Seleccione sus entradas a comprar: "))
            if entradas <= 0:
                print("Cantidad no valida, porfavor escoga correctamente")
            elif entradas > cupos:
                print("No hay asientos disponibles, solo hay ", cupos, "disponibles")
            else:
                precio = 8.00
                if edad < 12:
                    descuento = 0.50
                elif edad >= 12 and edad <= 17:
                    descuento = 0.25
                elif edad >= 18 and estudiante == "si":
                    descuento = 0.20
                else:
                    descuento = 0
                    
                precio_final = precio * (1 - descuento)
                total = precio_final * entradas
                cupos = cupos - entradas
                entradas_vendidas = entradas_vendidas + entradas
                dinero_recaudado = dinero_recaudado + total
                    
                print("--FACTURA SUPERCINES--")
                print("Entradas compradas: ", entradas)
                print("total a pagar: ", (total))
                print("Asientos: ", cupos)
                print("Pelcula: Residente Evil: Noche Cero")
        elif pelicula == 6:
            edad = int(input("Escriba su edad: "))
            estudiante = str(input("Es estudiante? (si/no): "))
            entradas = int(input("Seleccione sus entradas a comprar: "))
            if entradas <= 0:
                print("Cantidad no valida, porfavor escoga correctamente")
            elif entradas > cupos:
                print("No hay asientos disponibles, solo hay ", cupos, "disponibles")
            else:
                precio = 8.00
                if edad < 12:
                    descuento = 0.50
                elif edad >= 12 and edad <= 17:
                    descuento = 0.25
                elif edad >= 18 and estudiante == "si":
                    descuento = 0.20
                else:
                    descuento = 0
                    
                precio_final = precio * (1 - descuento)
                total = precio_final * entradas
                cupos = cupos - entradas
                entradas_vendidas = entradas_vendidas + entradas
                dinero_recaudado = dinero_recaudado + total
                    
                print("--FACTURA SUPERCINES--")
                print("Entradas compradas: ", entradas)
                print("total a pagar: ", (total))
                print("Asientos: ", cupos)
                print("Pelicula: Hechizada de Amor")
    elif opcion == 2:
        print("Asientos disponibles", cupos)
    elif opcion == 3:
        print("Saliendo, regrese pronto")
    else:
        print("Error")
        
print("--RESUMEN--")
print("total de entradas vendidas", entradas_vendidas)
print("Dinero recaudado",(dinero_recaudado))