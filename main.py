#Estacion meteorologica
import random

Mas_Alta = -100

#Creo la matriz [24 x 31] y lleno los espacios de 24 horas con valores aleatorios entra 15 a 44
Temps = [[(random.randint(15.0, 44.0)) for h in range(24)]for d in range(31)]

suma = 0.0
i = 0
#Bucle para obtener las temperaturas de los 31 dias del mes a las 12 del mediodia y saco promedio
for day in Temps:
   
   suma += day[12]
   
promedio = suma / 31

#Bucle para obtener la temperatura mas alta del mes
for day in Temps:
  for i in day:
    if i > Mas_Alta:
      Mas_Alta = i

#Bucle para obtener la cantidad de dias calurosos al mediodia derante todo el mes
hot_days = 0

for day in Temps:
  if day[12] > 20.0:
    hot_days += 1


print(f"Tuvimos {hot_days} dias calurosos.")
print(f"La temperatura mas alta registrada fue: {Mas_Alta}")
print(f"Temperatura promedio al mediodía: {promedio}")
