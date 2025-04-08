destino = input("¿A donde querés viajar? \n\nBariloche\nMar del Plata\nCataratas\n\n").lower()

match destino: #Tambien se puede hacer con un IF, para comprobar que el destino sea válido
    case "bariloche" | "mar del plata" | "cataratas":
        estacion = input("\n¿En qué estación?\n").lower()

        match estacion:
            case "invierno":
                if destino == "bariloche":
                    print("Se viaja")
                else:
                    print("No se viaja")
            case "verano" | "primavera":
                if destino != "bariloche":
                    print("Se viaja")
                else:
                    print("No se viaja")
            case "otoño":
                print("Se viaja")
            case _:
                print("Ingrese una estación válida")
    case _:
        print("Ingrese un destino valido")