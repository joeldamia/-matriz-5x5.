#Deber: Crear una matriz de 3 filas por 4 columnas, pedir al usuario que ingrese la fila y la columna de un asiento que desea reservar, marcar ese asiento como reservado (asignándole el valor 1) y luego mostrar la matriz completa en formato de tabla usando bucles anidados.
#Semana 12
#UEA
#Joel Guanluisa

asientos = [[0 for _ in range(4)] for _ in range(3)]

f = int(input("Ingrese fila (0 a 2): "))
c = int(input("Ingrese columna (0 a 3): "))

if 0 <= f <= 2 and 0 <= c <= 3:
    
    asientos[f][c] = 1
    print("\n¡Asiento reservado con éxito!")
else:
    print("\nError: Índices fuera de rango (Fila 0-2, Columna 0-3).")
    

print("\nEstado de la sala:")
for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()

