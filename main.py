continuar = "s"
 
inventario = []
continuar = input("Bienvenidos/as a Empire Inventory, desea continuar(s/n): ")

    
def mostrar_menu(menu: int) -> str:
    menu = print('''
        Menu:
          1. Cargar producto.
          2. Buscar producto.
          3. Ordenar inventario.
          4. Mostrar producto mas caro y mas barato.
          5. Mostrar productos con precio mayor a 15000.
          6. Salir
          elija una opcion: 
          
''')
    opcion = input("Elija una opcion: ")
    match opcion:
        case "1":
            cargar_producto(inventario)
        case "2":
            buscar_producto(inventario)
        case "3":
            ordenar_inventario(inventario)
        case "4":
            producto_mas_caro_barato(inventario)
        case "5":
            precio_mayor_15000(inventario)
        case "6":
            salir()
        case _:
            print("Incorrecto, elija una opcion valida")

def cargar_producto(inventario: list) -> list:
    continuar = "s"
    
    while continuar == "s":
        nombre_producto = input("Ingrese nombre de producto: ")
        precio = float(input("Ingrese el precio en pesos: "))
        cantidad = int(input("Ingrese la cantidad: "))
        
        inventario.append([nombre_producto, precio, cantidad])
        print(f"Producto agregado: {nombre_producto}, precio: ${precio:.2f}, cantidad: {cantidad}")
        
        continuar = input("¿Desea ingresar más productos? (s/n): ").lower()

    return inventario

def buscar_producto(inventario: list) -> str:
    print(inventario)
    
    continuar = "s"
    
    while continuar == "s":
        producto_buscado = input("Seleccione el producto que desea buscar: ").lower()
        
        for i in range(len(inventario)):
            if inventario[i][0].lower() == producto_buscado: 
                precio = inventario[i][1]
                cantidad = inventario[i][2]
                print(f"El producto ingresado es: {producto_buscado}, el precio es '$ {precio}' y el stock de ese producto es {cantidad}.")
                break
        else:
            print("Producto no encontrado en el inventario.")
        
        continuar = input("¿Desea continuar buscando productos? s/n: ").lower()

        resultado = print(f"El prodcuto ingresado es: {producto_buscado} el precio es '$ {precio}' y el stock de ese producto es {cantidad}.")
        continuar = input("¿Desea continuar buscando productos? s/n: ")
    return resultado

def ordenar_inventario(inventario: list) -> str:
    n = len(inventario)
    intercambiado = True  
    
    while intercambiado:
        intercambiado = False  
        for i in range(n - 1):
            if inventario[i][1] > inventario[i + 1][1]:  
                inventario[i], inventario[i + 1] = inventario[i + 1], inventario[i]  
                intercambiado = True  
        n -= 1  
    
    print("Inventario ordenado:")
    for producto in inventario:
        print(f"Producto: {producto[0]}, Precio: ${producto[1]:.2f}, Cantidad: {producto[2]}")

def producto_mas_caro_barato(inventario: list) -> str:
    if len(inventario) > 0:  
        producto_mas_caro = inventario[0]  
        producto_mas_barato = inventario[0]  

        for producto in inventario:
            if producto[1] > producto_mas_caro[1]:
                producto_mas_caro = producto
            if producto[1] < producto_mas_barato[1]:
                producto_mas_barato = producto

        print(f"Producto más caro: {producto_mas_caro[0]}, Precio: ${producto_mas_caro[1]:.2f}, Cantidad: {producto_mas_caro[2]}")
        print(f"Producto más barato: {producto_mas_barato[0]}, Precio: ${producto_mas_barato[1]:.2f}, Cantidad: {producto_mas_barato[2]}")
    else:
        print("El inventario está vacío.")

def precio_mayor_15000(inventario: list) -> str:
    productos_encontrados = 0  
    
    for producto in inventario:
        if producto[1] > 15000:
            print(f"Producto: {producto[0]}, Precio: ${producto[1]:.2f}, Cantidad: {producto[2]}")
            productos_encontrados += 1  
            
    if productos_encontrados == 0:  
        print("No hay productos con precio mayor a 15000.")

def salir():
    print("saliendo de Empire Inventory, hasta pronto.")

while continuar.lower() == "s":
    mostrar_menu(mostrar_menu)