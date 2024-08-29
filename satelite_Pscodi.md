INICIO

    //Definimos los datos iniciales (Km)

    // Solicitar datos al usuario
    altitud_inicial (Km)
    coeficiente_arrastre_inicial (un valor decimal pequeño, como 0.01)
    altitud_minima_segura (Km)

    Leer  Altitud_inicial, coeficiente_arrastre_inicial, altitud_minima_segura


    (altitud_inicial, Coeficiente_arraste_inicial, altitud_min_segura)

    altitud_actual = alt_inicial 

    coefciente_arraste = coeficiente_arraste_inicial

    orbitas = 0


    //imprimimos El texto 
    "simulando la desintegracion orbital: "


    //Utilizamos un bucle para simular la orbita 

        mientras altitud actual > altitud min segura

            # Calcula la pérdida de altitud debido al arrastre
            altitud perdida = coeficiente de arraste * altitud actual 

            # Resta la pérdida de altitud a la altitud actual
            altitud actual -= altitud perdida 

            # Aumenta ligeramente el coeficiente de arrastre
            coeficiente_arrastre += 0.0001


            # Incrementa el número de órbitas
            orbitas += 1 

        Fin mientras

    // Detenemos el bucle al alcanzar la altitud_min_segura 
    altitud_perdida < 0.001

    //Al estabilizarce 
    Imprimimos = ("El satélite se ha estabilizado en una órbita baja después de {orbitas} órbitas a una altitud de {altitud_actual} km.")

FIN
