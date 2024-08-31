INICIO
    LEER título (Sr. o Sra.)
    LEER nombre
    LEER apellido
    IMPRIMIR saludo personalizado utilizando el título, nombre y apellido del usuario

    IMPRIMIR las ciudades disponibles (Medellín, Bogotá, Cartagena)
    LEER ciudad de origen
    LEER ciudad de destino

    LEER día de la semana en que desea viajar
    LEER día del mes en que desea viajar

    DETERMINAR la distancia entre la ciudad de origen y destino

    SI la distancia es menor a 400 km:
        SI el día de la semana es lunes, martes, miércoles o jueves:
            ESTABLECER el precio del billete en $79,900

        SI el día de la semana es viernes, sábado o domingo:
            ESTABLECER el precio del billete en $119,900

    SI la distancia es 400 km o más:

        SI el día de la semana es lunes, martes, miércoles o jueves:
            ESTABLECER el precio del billete en $156,900

        SI el día de la semana es viernes, sábado o domingo:
            ESTABLECER el precio del billete en $213,000

    LEER usuario que indique su preferencia de asiento (pasillo, ventana, sin preferencia)

    SI el usuario prefiere pasillo:
        ASIGNAR la letra de asiento "C"

    SI el usuario prefiere ventana:
        ASIGNAR la letra de asiento "A"

    SI el usuario no tiene preferencia:
        ASIGNAR la letra de asiento "B"

    GENERAR un número de asiento aleatorio entre 1 y 29
    CONCATENAR el número de asiento con la letra de asiento asignada

    IMPRIMIR un resumen del vuelo:
        - Ciudad de origen y destino
        - Día de la semana y día del mes
        - Precio del billete
        - Asiento asignado
FIN
