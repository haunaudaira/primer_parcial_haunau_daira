
# #GENERAL
# def mostrar_matriz(matriz:list) -> None:
#     """ funcion que nos permite visualizar los datos de la matriz de forma ordenada. Reutilizable

#     Args:
#         matriz (list): el parametro matriz indica que devuelve una lista
#     """
#     for fil in range(len(matriz)):
#         for col in range(len(matriz[fil])):
#             print(f"{matriz[fil][col]}",end=" ")
#         print("")

# ---------------------------------

# def mostrar_participantes_promedio_menor_cuatro(array_nombres:list, matriz_puntos:list) -> None:
#     """ función específica utilizada para mostrar los nombres de los participantes con un promedio de puntuación menor a 4.
#     Args:
#         array_nombres (list): lista de nombres de los participantes
#         matriz_puntos (list): matriz de puntuaciones de los jurados
#     Returns:
#         None: no devuelve nada, solo imprime los datos en pantalla
#     """
#     for i in range(len(array_nombres)):
#         promedio = calcular_promedio(matriz_puntos[i])
#         if promedio < 4:
#             print(f"Nombre: {array_nombres[i]}, Promedio: {promedio:.2f}")

#--------------------------

# def mostrar_participantes_promedio_menor_ocho(array_nombres:list, matriz_puntos:list) -> None:
#     """ función específica utilizada para mostrar los nombres de los participantes con un promedio de puntuación menor a 8.
#     Args:
#         array_nombres (list): lista de nombres de los participantes
#         matriz_puntos (list): matriz de puntuaciones de los jurados
#     Returns:
#         None: no devuelve nada, solo imprime los datos en pantalla
#     """
#     for i in range(len(array_nombres)):
#         promedio = calcular_promedio(matriz_puntos[i])
#         if promedio < 8:
#             print(f"Nombre: {array_nombres[i]}, Promedio: {promedio:.2f}")


#-------------

# GENERAL 
# def cargar_array_string(array:list,mensaje:str) -> None:
#     """ cumple la misma función que cargar_nombres_alumnos, pero es más genérica y reutilizable.

#     Args:
#         array (list): _description_
#         mensaje (str): _description_
#     """
#     for i in range(len(array)):
#         #Pido el dato
#         nombre = input(f"{mensaje} {i+1}: ")
#         #Lo guardo en el array
#         array[i] = nombre


#______________________


# elif opcion == 11:  # top 3 participantes
#         if not datos_cargados:
#             print("Debe cargar los participantes y su puntuación correspondiente primero.")
#         else:
#             mostrar_top_3_participantes(array_nombres, array_jurados)

# def mostrar_top_3_participantes(array_nombres: list, matriz_puntos: list) -> None:
#     """muestra los nombres y promedios de los 3 participantes con mayor promedio. recibe una lista de nombres y una matriz de puntuaciones. calcula el promedio de cada participante, ordena los participantes por promedio de forma descendente y muestra los nombres y promedios de los 3 participantes con mayor promedio. si hay menos de 3 participantes, muestra solo los que existan. hace un intercambio manual de los participantes para ordenarlos, en lugar de usar funciones de ordenamiento predefinidas. si no hay participantes, no realiza ningún cálculo.
#     Args:
#         array_nombres (list): lista de nombres de los participantes
#         matriz_puntos (list): matriz de puntuaciones de los participantes por jurados
#     """
#     #inicializamos arrays de nombre y promedio
#     nombres = []
#     promedios = []
    
#     for i in range(len(array_nombres)):
#         promedio = calcular_promedio(matriz_puntos[i]) 
#         nombres = nombres + [array_nombres[i]]
#         promedios = promedios + [promedio]

#     #ordenamiento manual de los participantes por promedio (algo similar a bubble sort)
#     for i in range(len(promedios)-1):
#         for j in range(i+1, len(promedios)):
#             if promedios[j] > promedios[i]:
#                 # intercambio de promedio
#                 aux_prom = promedios[i]
#                 promedios[i] = promedios[j]
#                 promedios[j] = aux_prom
#                 # intercambio de nombre
#                 aux_nom = nombres[i]
#                 nombres[i] = nombres[j]
#                 nombres[j] = aux_nom

#     print("\nTop 3 participantes con mayor promedio: ")
#     maximo = 3
#     if len(nombres) < 3:
#         maximo = len(nombres)
#     for i in range(maximo):
#         print(f"{i+1}. {nombres[i]} - Promedio: {promedios[i]:.2f}")
