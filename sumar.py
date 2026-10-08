def sumar_n_primeros_while(n: int) -> int:
    """Calcula la suma iterando con un bucle mientras (while)."""
    suma_total = 0
    contador = 1
    while contador <= n:
        suma_total += contador
        contador += 1

    return suma_total
#Primera Prueba
suma = 0
contador = 1

while contador <= 5:
    suma += contador
    contador += 1

print(f"La suma del 1 al 5 es: {suma}")

#Segunda Prueba
suma = 0
contador = 1

while contador <= 10:
   suma += contador
   contador += 1

print(f"La suma del 1 al 10 es: {suma}")