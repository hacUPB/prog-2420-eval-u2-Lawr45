# reservas.py

import random

# Problema 1: Sistema de Reservas de Aerolíneas

# Información del usuario: #Usamos strip, para eliminar espacios en blanco y lower para uniformar lo que el usuario le da, y capitalize para poner los nombres con la primera en mayuscula.
titulo = input("¿Es usted señor o señora? (sr./sra.): ").strip().lower()
nombre = input("Introduce tu nombre: ").strip().capitalize()
apellido = input("Introduce tu apellido: ").strip().capitalize()

# Muestra un saludo personalizado utilizando el nombre completo del usuario.
print(f"{titulo.capitalize()} {nombre} {apellido}, ¡Bienvenido a FastFast Airlines!")

# Selección de vuelo:
print("Ciudades disponibles: medellin, bogota, cartagena")
origen = input("Ingresa tu origen: ").strip().lower()
destino = input("Ingresa tu destino: ").strip().lower()

# Verificar si el origen y destino son válidos
if origen not in ["medellin", "bogota", "cartagena"] or destino not in ["medellin", "bogota", "cartagena"]:
    print("Ruta no válida. Asegúrate de elegir entre 'medellin', 'bogota' o 'cartagena'.")
    exit()

# Solicita al usuario que ingrese el día de la semana y el día del mes.
dia_semana = input("Ingrese el día de la semana (por ejemplo, lunes): ").strip().lower()
dia_mes = input("Introduzca el día del mes (1-30): ").strip()

# Calcula la distancia entre las ciudades usando condicionales.
if (origen == "medellin" and destino == "bogota") or (origen == "bogota" and destino == "medellin"):
    distancia = 240
elif (origen == "medellin" and destino == "cartagena") or (origen == "cartagena" and destino == "medellin"):
    distancia = 461
elif (origen == "bogota" and destino == "cartagena") or (origen == "cartagena" and destino == "bogota"):
    distancia = 657
else:
    print("La ruta seleccionada no está disponible.")
    exit()

# Calcula el precio del billete dependiendo de la distancia y el día de la semana.
if distancia < 400:
    if dia_semana in ["lunes", "martes", "miercoles", "jueves"]:
        precio = 79900
    else:
        precio = 119900
else:
    if dia_semana in ["lunes", "martes", "miercoles", "jueves"]:
        precio = 156900
    else:
        precio = 213000

# Asignación de asiento:
preferencia_asiento = input("¿Prefieres un asiento en el pasillo, junto a la ventana o no tienes preferencia? (pasillo/ventana/sin preferencia): ").strip().lower()

if preferencia_asiento == "pasillo":
    letra_asiento = "C"
elif preferencia_asiento == "ventana":
    letra_asiento = "A"
else:
    letra_asiento = "B"

# Selecciona aleatoriamente un número de asiento entre 1 y 29.
numero_asiento = random.randint(1, 29)
asiento_asignado = f"{numero_asiento}{letra_asiento}"

# Salida:
print(f"\nTu vuelo de {origen.capitalize()} a {destino.capitalize()} del {dia_semana.capitalize()} {dia_mes} está reservado.")
print(f"Precio del boleto: ${precio}")
print(f"Tu asiento es: {asiento_asignado}")
