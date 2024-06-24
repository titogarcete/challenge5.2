# Solicitar al usuario que ingrese la temperatura en grados Celsius
celsius = float(input("Introduce la temperatura en grados Celsius: "))

# Convertir la temperatura a grados Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Mostrar el resultado
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit")
