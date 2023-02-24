vuelta_tiempo = 0
pits_tiempo = 0

# Solcitar tiempos 
for i in range(5):
    tiempo_vuelta = float(input(f"Ingrese el tiempo de la vuelta {i+1}: "))
    vuelta_tiempo += tiempo_vuelta
    
    tiempo_pits = float(input(f"Ingrese el tiempo de PITS para la vuelta {i+1}: "))
    pits_tiempo += tiempo_pits
    
# Cálculo promedio
promedio_vuelta = vuelta_tiempo / 5
promedio_pits = pits_tiempo / 5

porcentaje_pits_vuelta = (pits_tiempo / vuelta_tiempo) * 100

# Mostrar resultados
print(f"\nEl tiempo promedio por vuelta es de: {promedio_vuelta:.2f} segundos")
print(f"El tiempo promedio por PITS es de: {promedio_pits:.2f} segundos")
print(f"El porcentaje del tiempo PITS respecto al tiempo de vuelta total es del: {porcentaje_pits_vuelta:.2f}%")
