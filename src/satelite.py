
def main():

    # 1. Descripción:
    # - El satélite comienza a una altitud inicial específica y orbita la Tierra en una trayectoria circular.
    # - La fuerza de arrastre que actúa sobre el satélite aumenta a medida que desciende, lo que provoca una pérdida de altitud más rápida con el tiempo.
    # - El programa debe simular el descenso del satélite hasta que se estabilice en una órbita baja o reingrese en la atmósfera terrestre.
    
    def simulacion_desintegracion_orbital(altitud_inicial, coeficiente_arrastre_inicial, altitud_minima_segura):
        # Datos de entrada:
        # - Altitud inicial: La altitud inicial del satélite (en kilómetros).
        # - Coeficiente de arrastre: Factor que determina la rapidez con la que el satélite pierde altitud.
        # - Altitud mínima de seguridad: Altitud por debajo de la cual se considera que el satélite ha reingresado en la atmósfera terrestre y se ha desintegrado.
        
        altitud_actual = altitud_inicial
        coeficiente_arrastre = coeficiente_arrastre_inicial
        orbitas = 0
        
        print("Simulando la desintegración orbital...")
    
        # 2. Proceso:
        # - Utiliza un bucle para simular cada órbita.
        while altitud_actual > altitud_minima_segura:
            # Para cada órbita:
            
            # - Calcula la pérdida de altitud debido al arrastre
            altitud_perdida = coeficiente_arrastre * altitud_actual
            
            # - Resta la pérdida de altitud a la altitud actual
            altitud_actual -= altitud_perdida
            
            # - Aumenta ligeramente el coeficiente de arrastre
            coeficiente_arrastre += 0.0001
            
            # - Incrementa el número de órbitas
            orbitas += 1
    
            print(f"Órbita {orbitas}: Altitud actual = {altitud_actual:.4f} km, Coeficiente de arrastre = {coeficiente_arrastre:.4f}")
            
            # - Detén el bucle si el satélite se estabiliza (la pérdida de altitud es muy pequeña)
            if altitud_perdida < 0.001:
                # 3. Salida:
                # - Si el satélite se estabiliza en órbita
                print(f"El satélite se ha estabilizado en una órbita baja después de {orbitas} órbitas a una altitud de {altitud_actual:.4f} km.")
                return
    
        # - Si el satélite reingresa en la atmósfera terrestre
        print(f"El satélite ha reingresado en la atmósfera terrestre después de {orbitas} órbitas.")
    
    # Solicitar datos al usuario
    altitud_inicial = float(input("Ingrese la altitud inicial del satélite (en kilómetros): "))
    coeficiente_arrastre_inicial = float(input("Introduzca el coeficiente de arrastre inicial: "))
    altitud_minima_segura = float(input("Ingrese la altitud mínima segura (en kilómetros): "))
    
    # Ejecutar la simulación
    simulacion_desintegracion_orbital(altitud_inicial, coeficiente_arrastre_inicial, altitud_minima_segura)



if __name__ == "__main__":
    main()
