'''
# 1. La Fábrica de Chocolates El Tesoro de los Dulces requiere realizar un aumento a sus
colaboradores según el tiempo de antigüedad en la empresa. Para ello utiliza los siguientes
criterios:
        Antigüedad % Aumento
        ▪ De 0 a 5 años 10%
        ▪ De 6 a 9 años 15%
        ▪ De 10 a 15 años 25%
        ▪ Más de 15 años 30%

Cree un programa que solicite el salario actual y el tiempo de laborar en años, calcule el
aumento y el nuevo salario y muestre la información calculada. '''
print("\nEjercicio 1\n")
salario_actual = float(input("Ingrese el salario actual: "))
antiguedad = int(input("Ingrese el tiempo de laborar en años: "))

if antiguedad >= 0 and antiguedad <= 5:
    aumento = salario_actual * 0.1
elif antiguedad >= 6 and antiguedad <= 9:
    aumento = salario_actual * 0.15
elif antiguedad >= 10 and antiguedad <= 15:
    aumento = salario_actual * 0.25
else:
    aumento = salario_actual * 0.3

nuevo_salario = salario_actual + aumento

print("El aumento salarial es de:", aumento)
print("El nuevo salario es de:", nuevo_salario)


'''
# 2. Permita calcular el total a pagar por la compra de pantalones de vestir. Si se compran
entre 1 a 5 pantalones se aplica un descuento del 12.5%, si se compra una cantidad
comprendida entre 5 y 8 pantalones se aplica un descuento del 20% y si se compran
cantidades mayores, se aplica un descuento del 31.5% sobre el total de la compra. Debe
imprimirse en pantalla la compra final sin descuento, monto del descuento y la compra
con descuento. 
'''
print("\nEjecicio 2\n")
precio_unitario = 50.0  # Precio de cada pantalón de vestir
cantidad = int(input("Ingrese la cantidad de pantalones de vestir a comprar: "))

total_sin_descuento = precio_unitario * cantidad

if cantidad >= 1 and cantidad <= 5:
    descuento = total_sin_descuento * 0.125
elif cantidad >= 6 and cantidad <= 8:
    descuento = total_sin_descuento * 0.2
else:
    descuento = total_sin_descuento * 0.315

total_con_descuento = total_sin_descuento - descuento

print("El total sin descuento es de:", total_sin_descuento)
print("El monto del descuento es de:", descuento)
print("El total con descuento es de:", total_con_descuento)


'''
# 3. El Hotel El Sol Naciente cuenta con un precio por noche de 100 dólares. Si el usuario se
hospeda más de 3 noches se le aplica un porcentaje de descuento del 5% y si no se aplica
un porcentaje de descuento del 0%. Devuelva el monto total que debe pagar el cliente,
sabiendo que él indica cuántas noches se va a hospedar. 
# '''

print("\nEjercicio 3\n")
precio_noche = 100.0  # Precio por noche
num_noches = int(input("Ingrese el número de noches que se va a hospedar: "))

if num_noches > 3:
    descuento = precio_noche * num_noches * 0.05
else:
    descuento = 0.0

total_a_pagar = precio_noche * num_noches - descuento

print("El monto total a pagar es de:", total_a_pagar)


