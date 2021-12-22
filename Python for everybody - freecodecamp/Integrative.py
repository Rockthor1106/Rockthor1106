#This is a python version of my first integrative taks at APO 1

LABOR = 4880000

def getData():
    try:
        amount = int(input("¿Cuántos materiales desea ingresar? "))
    except:
        print("Entrada inválida")
    name_material = [None] * amount #it looks like list = [None,None,None,...], amount times
    amount_material = [None] * amount
    prices = [None] * amount
    hardware_store = [None] * amount
    category1 = []
    category2 = []
    category3 = []

    for i in range(amount):
        name_material[i] = input("Nombre del material ")
        amount_material[i] = input("Cantidad del material ")
        try:
            utilization = int(input("Uso del material. Presione 1 para obra negra, 2 para obra blanca y 3 para pintura "))
        except:
            print("Entrada inválida")
        if utilization == 1:
            category1.append(name_material[i])
        elif utilization == 2:
            category2.append(name_material[i])
        elif utilization == 3:
            category3.append(name_material[i])
        else:
            print("No hay una opción válida para el valor introducido")
        try:
            home_center = int(input("Ingrese el precio en Home Center "))
            neighborhood = int(input("Ingrese el precio en la ferretería del barrio "))
            center = int(input("Ingrese el precio en la ferretería del centro "))
        except:
            print("Entrada inválida")
        if home_center < neighborhood:
            if home_center < center:
                prices[i] = home_center
                hardware_store[i] = "Home Center"
        if neighborhood < home_center:
            if neighborhood < center:
                prices[i] = neighborhood
                hardware_store[i] = "Ferretería del barrio"
        if center < home_center:
            if center < neighborhood:
                prices[i] = center
                hardware_store[i] = "Ferretería del centro"
    print("El total de la lista con los mejores precios SIN mano de obra es: ", calculateTotalPrice(prices))
    print("El total con mano de obra y mejores precios es: ", calculateTotalPrice(prices)+LABOR)
    displayBestPricesList(amount, name_material, prices, hardware_store)
    displayCategory1(category1)
    displayCategory2(category2)
    displayCategory3(category3)
    
def calculateTotalPrice(prices):
    total = 0
    for price in prices:
        total = total + price
    return total

def displayBestPricesList(amount, name_material, prices, hardware_store):
    print("*****LISTA CON LOS MEJORES PRECIOS*****")
    for i in range(amount):
        print(name_material[i], "a un precio de", prices[i], "en", hardware_store[i])
    print("***************************************")

def displayCategory1(category1):
    print("*****OBRA NEGRA*****")
    for material in category1:
        print(material)
    print("********************")

def displayCategory2(category2):
    print("*****OBRA BLANCA*****")
    for material in category2:
        print(material)
    print("*********************")

def displayCategory3(category3):
    print("*****PINTURA*****")
    for material in category3:
        print(material)
    print("*****************")

getData()