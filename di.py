
# =====================================================================
# Programa: Gestión de Productos de una Tienda
# Descripción: Permite almacenar, organizar, buscar y mostrar 
#              productos usando un diccionario 
# Universidad estatal amazonica
# =====================================================================

def mostrar_menu():
    print("\n--- SISTEMA DE GESTIÓN DE TIENDA ---")
    print("1. Mostrar todos los productos")
    print("2. Agregar o actualizar un producto")
    print("3. Buscar un producto por nombre")
    print("4. Eliminar un producto")
    print("5. Salir")

def ejecutar_programa():
    # 1. Creación de la colección de datos  con datos iniciales
    inventario = {
        "Manzanas": 1.50,
        "Leche": 0.95,
        "Pan": 1.10
    }
    
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (1-5): ").strip()
        
        if opcion == "1":
            print("\n--- INVENTARIO ACTUAL ---")
            if not inventario:
                print("El inventario está vacío.")
            else:
                for producto, precio in inventario.items():
                    print(f"• {producto}: ${precio:.2f}")
                    
        
        elif opcion == "2":
            nombre = input("Ingresa el nombre del producto: ").capitalize().strip()
            try:
                precio = float(input(f"Ingresa el precio para '{nombre}': $"))
                if precio < 0:
                    print("El precio no puede ser negativo.")
                else:
                    inventario[nombre] = precio  # Agrega o actualiza
                    print(f"¡Producto '{nombre}' guardado exitosamente!")
                    
            except ValueError:
                print("Error: Por favor ingresa un número válido para el precio.")
                
        
        elif opcion == "3":
            nombre = input("Ingresa el nombre del producto a buscar: ").capitalize().strip()
            if nombre in inventario:
                print(f"\n🔍 Resultado: {nombre} cuesta ${inventario[nombre]:.2f}")
            else:
                print(f"\n❌ El producto '{nombre}' no se encuentra en el inventario.")
                
        #
        elif opcion == "4":
            nombre = input("Ingresa el nombre del producto a eliminar: ").capitalize().strip()
            if nombre in inventario:
                del inventario[nombre]
                print(f"🗑️ El producto '{nombre}' ha sido eliminado.")
            else:
                print(f"❌ No se pudo eliminar. '{nombre}' no existe.")
                
        elif opcion == "5":
            print("Saliendo del sistema. ¡Que tengas un excelente día!")
            break
            
        else:
            print("Opción no válida. Por favor, selecciona un número del 1 al 5.")


if __name__ == "__main__":
    ejecutar_programa()
