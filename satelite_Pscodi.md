INICIO

    Leer  Altitud_inicial, coeficiente_arrastre_inicial, altitud_minima_segura

    altitud_actual = alt_inicial 

    coeficiente_arraste = coeficiente_arraste_inicial

    orbitas = 0


    imprimimos ("simulando la desintegracion orbital: ")


    mientras altitud_actual > altitud_min_segura

        altitud_perdida = coeficiente_arraste * altitud_actual 

        altitud_actual -= altitud_perdida 

        coeficiente_arrastre += 0.0001

        orbitas += 1 

        altitud_perdida < 0.001

    Fin mientras

    Imprimimos ("El satélite se ha estabilizado en una órbita baja después de {orbitas} órbitas a una altitud de {altitud_actual} km.")
    
FIN
