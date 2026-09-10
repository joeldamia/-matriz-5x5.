#Definición de la función para aplicar el descuento
#Deber Semana 13
#Joel Guanoluisa

def calcular_precio_con_descuento(precio_original, porcentaje_descuento):
    descuento = precio_original * (porcentaje_descuento / 100)
    precio_final = precio_original - descuento
    return precio_final


if __name__ == "__main__":
    
    # Definición de variables con los valores del producto y el descuento
    
    precio_producto = 80.0 # Precio original del producto
    descuento_tienda = 15.0 # Porcentaje de descuento
    
    total_a_pagar = calcular_precio_con_descuento(precio_producto, descuento_tienda)
    
    # Muestra del resultado en la consola
    print("_____________________________")
    print("CONCEPTO      |       DETALLE")
    print("_____________________________")
    print(f"Precio original:         ${precio_producto:.2f}")
    print("_____________________________")
    print(f"Descuento aplicado:       {descuento_tienda}%")
    print("_____________________________")
    print(f"El total neto a pagar es:${total_a_pagar:.2f}")
    print("_____________________________")
