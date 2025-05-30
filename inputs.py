# este archivo contiene todas las funciones o variables que gestionen la interacción con el usuario o la lectura de datos externos

# menú de opciones, importas las funciones de inputs.py y funciones.py. controla el flujo del programa

""" Una academia de baile organiza una competencia abierta para definir a su nuevo o nueva representante nacional. La competencia cuenta con un jurado compuesto por tres personas, cada una de las cuales puntúa a los participantes del 1 al 10. """
from funciones import * # importa las funciones
import os # módulo para limpiar la terminal

#incilizamos los datos
array_nombres = crear_array(5, "")  # reserva el valor de 5 participantes
array_jurados = crear_matriz(5, 3, 0)  # crea matriz 5x3 con cada elemento inicializado en 0 para guardar las puntuaciones para cada participante
datos_cargados = False  # controlar si se cargaron datos para poder avanzar

#iniciamos un bucle while para el menú
while True:
    print("\n--- COMPETENCIA DE BAILE ---")
    print("1. Cargar de participantes \n 2. Cargar puntuaciones de jurados \n 3. Mostrar participantes y puntuaciones \n 4. Mostrar participantes con promedio < 4 \n 5. Mostrar participantes con promedio < 8 \n 6. Promedio de cada jurado \n 7. Juado más estricto \n 8. Jurado más generoso \n 9. Participantes con puntuaciones iguales \n 10. Buscar participante por nombre \n 11. Salir")

    opcion = ingresar_entero_rango("\nIngrese una opción (1-13): ", "Opción no válida. Debe ingresar un número entre 1 y 13: ", 1, 13)

    #manejo de opciones
    if opcion == 1: # carga de participantes
        cargar_nombres_participantes(array_nombres)
        datos_cargados = True
    elif opcion == 2: # carga de puntuaciones
        if not datos_cargados:
            print("Debe cargar los participantes primero.")
        else:
            cargar_puntuacion_participantes(array_jurados)
    elif opcion == 3:
        if not datos_cargados: # mostrar participantes y puntuaciones
            print("Debe cargar los participantes primero.")
        else:
            mostrar_puntuaciones(array_nombres, array_jurados)  # muestra el primer participante
    elif opcion == 4:  # mostrar participantes con promedio < 4
        if not datos_cargados and not datos_cargados:   
            print("Debe cargar los participantes y su puntuación correspondiente primero.")
        else:
            mostrar_participantes_promedio_menor(array_nombres, array_jurados, 4)
    elif opcion == 5:  # mostrar participantes con promedio < 8
        if not datos_cargados and not datos_cargados:   
            print("Debe cargar los participantes y su puntuación correspondiente primero.")
        else:
            mostrar_participantes_promedio_menor(array_nombres, array_jurados, 8)
    elif opcion == 6:  # promedio de cada jurado
        if not datos_cargados:
            print("Debe cargar los participantes y su puntuación correspondiente primero.")
        else:
            calcular_promedio_jurados(array_jurados)
    elif opcion == 7:  # jurado más estricto
        if not datos_cargados:
            print("Debe cargar los participantes y su puntuación correspondiente primero.")
        else:
            promedios_por_jurado = obtener_promedios_por_jurado(array_jurados)
            mostrar_jurado_promedio_minimo(promedios_por_jurado)
    elif opcion == 8:  # jurado más generoso
        if not datos_cargados:
            print("Debe cargar los participantes y su puntuación correspondiente primero.")
        else:
            promedios_por_jurado = obtener_promedios_por_jurado(array_jurados)
            mostrar_jurado_promedio_maximo(promedios_por_jurado)
    elif opcion == 9:  # participantes con puntuaciones iguales
        if not datos_cargados:
            print("Debe cargar los participantes y su puntuación correspondiente primero.")
        else:
            mostrar_participantes_puntuaciones_iguales(array_nombres, array_jurados)
    elif opcion == 10:  # buscar participante por nombre
        if not datos_cargados:
            print("Debe cargar los participantes y su puntuación correspondiente primero.")
        else:
            nombre = input("Ingrese el nombre del participante a buscar: ")
            buscar_participantes_por_nombre(array_nombres, array_jurados, nombre)
    elif opcion == 11:  # salir
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Debe ingresar un número entre 1 y 11.")

    input("\nPresione Enter para continuar...")
    os.system("cls") #limpia la terminal (windows)
