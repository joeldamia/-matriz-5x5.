#Descuento y el precio total de un prodructo

def calcular_total (precio,descuento):
    
    ahorro=precio*(descuento/100)
    
    total=precio-ahorro
    
    return total

precio=150
descuento=15
    
resultado=calcular_total(precio,descuento)
    
print("El precio total a pagar del producto es: $",resultado )
