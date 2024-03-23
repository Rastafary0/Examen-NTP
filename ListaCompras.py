lista_compras = []
while True: 
    producto = input("Ingrese el nombre del producto o 'terminar' para finalizar la lista de compras): ").strip().lower() 
    if producto == "terminar":
        break
    else:      
        lista_compras.append(producto)
print("\nLista de compras:")
for producto in lista_compras:
    print(producto.capitalize())