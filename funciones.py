#solo incluye lógica de procesamiento

#General 
def crear_array(cantidad_elementos:int,valor_inicial:any) -> list:
    """crea una lista simple unidimensional y devuelve una lista con un número específico de elementos inicializados con el mismo valor. La función recibe dos argumentos:
    Args:
        cantidad_elementos (int): entero que indica cuantos elementos tendrá el array
        valor_inicial (any): el valor que tendrá cacda elemento
    Returns:
        list: devuelve la lista creada
    """
    array = [valor_inicial] * cantidad_elementos 
    return array

#GENERAL
def crear_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    """crea una lista bidimensional que guarda datos más complejos o estructurados, donde cada elemento es una lista que representa una fila de la matriz. La función recibe tres argumentos:
    Args:
        cantidad_filas (int): cantidad de filas que tendrá la matriz
        cantidad_columnas (int): cantidad de columnas que tendrá la matriz
        valor_inicial (any): valor que tendrá cada elemento de la matriz
    Returns:
        list: devuelve la matriz creada
    """
    matriz = []
    for i in range(cantidad_filas): #bucle for, repite la creación de filas según la cantidad de filas especificada
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila] #agrega la fila creada a la matriz
    
    return matriz

def es_entero(cadena:str) -> bool:
    """verifica si una cadena de texto representa un número entero válido. La función recibe un argumento:
    Args:
        cadena (str): cadena de texto que se desea verificar si es un número entero
    Returns:
        bool: devuelve True si la cadena representa un número entero válido, False en caso contrario
    """
    if len(cadena) > 0: # comprueba que el largo de la cadena mayor a 0
        retorno = True
        for i in range(len(cadena)):
            valor_ascii = ord(cadena[i])
            if valor_ascii > 57 or valor_ascii < 48:
                retorno = False
                break
    else:
        retorno = False 
    
    return retorno

def ingresar_entero(mensaje:str) -> int:
    """de interacción con el usuario. solicita que se ingrese un dato desde consola mostrando un mensaje. tiene un manejo de error donde va continuar solicitando el dato hasta que se ingrese un número entero válido.
    Args:
        mensaje (str): mensaje que se mostrará al usuario para solicitar el dato
    Returns:
        int: devuelve el número entero ingresado por el usuario
    """
    numero = input(mensaje)
    while not es_entero(numero):
        print("ERROR NO ES UN NUMERO") #si no es un numero
        numero = input(mensaje)
    numero = int(numero)
    return numero

def ingresar_entero_rango(mensaje:str,mensaje_error:str,minimo:int,maximo:int) -> int:
    """ solicita un número entero dentro de un rango específico. Si el número ingresado no está dentro del rango, solicita nuevamente el dato hasta que se ingrese un número válido.

    Args:
        mensaje (str): mensaje que se mostrará al usuario para solicitar el dato
        mensaje_error (str): mensaje que se mostrará al usuario si el número ingresado no está dentro del rango.
        minimo (int): numero mínimo permitido
        maximo (int): numero maximo permitido

    Returns:
        int: devuelve el número entero ingresado por el usuario que está dentro del rango especificado
    """
    numero = ingresar_entero(mensaje)
    while numero > maximo or numero < minimo:
        numero = ingresar_entero(mensaje_error) #si no esta en el rango especificado

    return numero


def es_alfabetico(cadena:str) -> bool:
    """verifica si una cadena de texto contiene solo letras del alfabeto.
    Args:
        cadena (str): cadena de texto que se desea verificar si contiene solo letras del alfabeto
    Returns:
        bool: devuelve True si la cadena contiene solo letras del alfabeto, False en caso contrario
    """
    if len(cadena) > 0: #longitud. si la cadena no está vacía, entonces...
        retorno = True
        for i in range(len(cadena)):
            valor_ascii = ord(cadena[i])
            if (valor_ascii < 65 or valor_ascii > 90) and (valor_ascii < 97 or valor_ascii > 122):
                retorno = False
                break
    else:
        retorno = False 
    return retorno


def cargar_nombres_participantes(array_nombres:list) -> None:
    """rellena la lista preexistente (array_nombres) con los nombres de los participantes ingresados por el usuario. para cada posicion en la lista solicita un nombre, valida: que sea alfabético, que tenga al menos 3 caracteres y que no este vacío. si el dato ingresado no cumple, solicita nuevamente el dato hasta que se ingrese un nombre válido.
    esta función no retorna nada, ya que modifica directamente la lista pasada como argumento.

    Args:
        array_nombres (list): lista donde se guardarán los nombres de los participantes
    """
    for i in range(len(array_nombres)): 
        while True:
            #solicita dato
            nombre = input(f"Ingrese el nombre del participante #{i+1}: ")
            #valida (no vacío)
            if not es_alfabetico(nombre):
                print("ERROR: El nombre debe contener solo letras y no puede estar vacío. Intente nuevamente.")
                continue
            if len(nombre) < 3:
                print("Error: El nombre debe tener al menos 3 caracteres")
                continue
            #si cumple, se guarda
            array_nombres[i] = nombre   
            break
        

def cargar_puntuacion_participantes(array_jurados:list) -> None:
    """rellena la matriz preexistente (array_jurados) con las puntuaciones de los participantes por jurados. itera sobre la celda de la matriz solicitando una puntuación y valida que sea un entero entre 1 y 10. modifica la matriz directamente, no retorna nada.
    Args:
        array_jurados (list): matriz donde se guardarán las puntuaciones de los participantes por jurados
    Returns:
        None
    """
    for fil in range(len(array_jurados)):
        for col in range(len(array_jurados[fil])):
            while True:
                #solicita dato
                puntuacion = ingresar_entero(f"Ingrese la puntuación del jurado #{col+1} para el participante #{fil+1} (1-10): ")
                #validacion de datos ingresados (entre 1 y 10)
                if 1 <= puntuacion <= 10:
                    #si cumple, se guarda
                    array_jurados[fil][col] = puntuacion 
                    break
                else:
                    print("ERROR: La puntuación debe ser un número entre 1 y 10. Intente nuevamente.")


def calcular_promedio(puntajes:list) -> float:
    """calcula el promedio de una lista de numeros (puntajes). recibe una lista de puntajes y devuelve el promedio que se utiliza más adelante
    Args:
        puntajes (list): lista de números (enteros o flotantes) de la cual calcular el promedio.
    Returns:
        float: el promedio de los números en la lista, o 0.0 si la lista está vacía
    """
    suma = 0
    for puntaje in puntajes:
        suma += puntaje
    promedio = suma / len(puntajes)
    return promedio

#se modificó a la realizada por el profesor para que se visualicen todos los participantes y cumpla con las validaciones
def mostrar_puntuaciones(array_nombres:list,array_jurados:list) -> None:
    """muestra los nombres de los participantes y sus puntuaciones por jurado. recibe dos listas: una con los nombres de los participantes y otra con las puntuaciones de cada jurado. imprime el nombre del participante, las puntuaciones de cada jurado y el promedio de las puntuaciones. si no hay participantes o puntuaciones, muestra un mensaje indicando que no hay datos para mostrar.

    Args:
        array_nombres (list): lista de nombres de los participantes
        array_jurados (list): matriz de puntuaciones de los participantes por jurados
    """
    for i in range(len(array_nombres)):
        print(f"\nNombre: {array_nombres[i]}")
        print(f"Nota jurado 1: {array_jurados[i][0]}")
        print(f"Nota jurado 2: {array_jurados[i][1]}")
        print(f"Nota jurado 3: {array_jurados[i][2]}")
        print(f"Promedio: {calcular_promedio(array_jurados[i]):.2f}")

def obtener_promedios_por_jurado(array_jurados: list) -> list:
    """calcula el promedio de las puntuaciones otorgadas por cada jurado. Maneja errores. crea una lista para almacenar los puntajes de cada jurado y luego calcula el promedio de cada uno. si la matriz está vacía, no realiza ningún cálculo y retorna una lista vacía.
    Args:
        array_jurados (list): matriz de puntuaciones de los participantes por jurados
    Returns:
        list: retorna una lista con los promedios de cada jurado
    # """
    promedios = []
    for col in range(len(array_jurados[0])):  # iterar sobre las columnas (jurados)
        suma = 0
        for fil in range(len(array_jurados)):  # iterar sobre las filas (participantes)
            suma += array_jurados[fil][col]  # sumar las puntuaciones del jurado
        promedio = suma / len(array_jurados)  # calcular el promedio
        promedios += [promedio]  #actualiza
    
    return promedios

def mostrar_promedio_jurados(array_jurados: list) -> list: 
    """calcula el promedio de las puntuaciones otorgadas por cada jurado. si la matriz está vacía, no realiza ningún cálculo.
    Args:
        array_jurados (list): matriz de puntuaciones de los participantes por jurados
    Returns:
        float: retorna una lista con los promedios de cada jurado
    """
    promedios = obtener_promedios_por_jurado(array_jurados) #llama a la función y le pasa el argumento
    print("\nPromedio de cada jurado:")
    if promedios: 
        for i in range(len(promedios)):
            print(f"Jurado {i + 1}: {promedios[i]:.2f}") 
    else:
        print("No se pudieron calcular promedios de jurados (matriz vacía o incorrecta).")
    return promedios # retorna los promedios calculados
    

def mostrar_participantes_promedio_menor(array_nombres:list, array_jurados:list, promedio_minimo:float) -> None:
    """muestra los nombres y promedios de los participantes que tienen un promedio menor al establecido. recibe una lista de nombres, una matriz de puntuaciones y un promedio mínimo. itera sobre los participantes, calcula su promedio y muestra el nombre y el promedio si es menor al promedio mínimo. si no hay participantes con un promedio menor al establecido, muestra un mensaje indicando que no hay participantes con ese criterio.
    Args:
        array_nombres (list): lista de nombres de los participantes
        array_jurados (list): matriz de puntuaciones de los participantes por jurados
        promedio_minimo (float): promedio mínimo establecido para filtrar participantes
    """
    existen_participantes = False 
    for i in range (len(array_nombres)):
        promedio = calcular_promedio(array_jurados[i])
        if promedio < promedio_minimo:
            existen_participantes = True
            print(f"Nombre: {array_nombres[i]}, Promedio: {promedio:.2f}")
    if not existen_participantes:
        print("No hay participantes con un promedio menor a {promedio_minimo}.")


     
def mostrar_jurado_promedio_minimo (array_jurados:list) -> float:
    """muestra el jurado que otorgó el promedio más bajo. busca el valor más bajo dentro de array_jurados recorriendo la lista y cuando lo encuentra actualiza y guarda su posición. 
    
    Args:
        array_jurados (list): lista de promedios de jurados
    
    Returns:
        float: retorna el promedio más bajo de los jurados
    """
    minimo = array_jurados[0]
    indice_minimo = 0
    for i in range(len(array_jurados)):
        if array_jurados[i] < minimo:
            minimo = array_jurados[i] 
            indice_minimo = i
    print(f"El jurado N {indice_minimo + 1} dio el promedio más bajo {minimo:.2f}")
    return minimo       

def mostrar_jurado_promedio_maximo (array_jurados:list) -> float:
    """muestra el jurado que otorgó el promedio más alto. busca el valor más alto dentro de array_jurados recorriendo la lista y cuando lo encuentra actualiza y guarda su posición. 
    
    Args:
        array_jurados (list): lista de promedios de jurados
    
    Returns:
        float:  retorna el promedio más alto de los jurados
    """
    maximo = array_jurados[0] #incializa posición
    indice_maximo = 0 #guarda
    for i in range(len(array_jurados)):
        if array_jurados[i] > maximo:
            maximo = array_jurados[i]
            indice_maximo = i
    print(f"El jurado N {indice_maximo + 1} dio el promedio más alto {maximo:.2f}")
    return maximo

def mostrar_participantes_puntuaciones_iguales(array_nombres:list, array_jurados:list) -> None:
    """muestra los nombres y puntuaciones de los participantes que tienen puntuaciones iguales en todos los jurados. recibe una lista de nombres y una matriz de puntuaciones. itera sobre los participantes y verifica si las puntuaciones de todos los jurados son iguales. si es así, muestra el nombre del participante y su puntuación. si no hay participantes con puntuaciones iguales, muestra un mensaje indicando que no hay participantes con ese criterio.

    Args:
        array_nombres (list): lista de nombres de los participantes
        array_jurados (list): matriz de puntuaciones de los participantes por jurados
    """
    existen_participantes = False # variable para controlar si existen participantes con puntuaciones iguales
    for i in range(len(array_nombres)): 
        if array_jurados[i][0] == array_jurados[i][1] == array_jurados[i][2]:
            existen_participantes = True
            print(f"Nombre: {array_nombres[i]}, Puntuación: {array_jurados[i][0]}") # si coinciden entonces se muestra solo 1

    if not existen_participantes:
        # si no existen participantes con puntuaciones iguales, se imprime un mensaje
        print("No hay participantes con puntuaciones iguales.")

def buscar_participantes_por_nombre(array_nombres:list, array_jurados:list, nombre_buscado:str) -> None:
    """busca un participante por su nombre en la lista de nombres y muestra sus puntuaciones y promedio. recibe una lista de nombres, una matriz de puntuaciones y el nombre del participante a buscar. itera sobre la lista de nombres, compara cada nombre con el nombre buscado y si encuentra una coincidencia, muestra el nombre, las puntuaciones de cada jurado y el promedio. si no encuentra al participante, muestra un mensaje indicando que no se encontró."
    Args:
        array_nombres (list): lista de nombres de los participantes
        array_jurados (list): matriz de puntuaciones de los participantes por jurados
        nombre_buscado (str): nombre del participante a buscar
    """
    encontrado = False  
    for i in range(len(array_nombres)):
        if array_nombres[i] == nombre_buscado:  
            encontrado = True
            print(f"\nNombre: {array_nombres[i]}") 
            print(f"Puntuación jurado 1: {array_jurados[i][0]}") 
            print(f"Puntuación jurado 2: {array_jurados[i][1]}")
            print(f"Puntuación jurado 3: {array_jurados[i][2]}")
            print(f"Promedio: {calcular_promedio(array_jurados[i]):.2f}")
    if not encontrado:
        print("Participante no encontrado")
