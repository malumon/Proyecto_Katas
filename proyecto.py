# # PROYECTO LOGICA: KATAS DE PYTHON

# ## 1. Función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados. 

def frecuencias_letras(cadena_texto):
    """Función para contar caracteres de una cadena de texto
    
    Args:
        cadena _texto (str): cadena de texto con caracteres 

    Returns:
        diccionario: resultado tipo diccionario con las letras como key y la frencuencia como value
    """
    diccionario_frecuencias = {}

    for letra in cadena_texto:
        if letra !=  " ":
            letra = letra.lower()
            if  letra  in diccionario_frecuencias:
                diccionario_frecuencias[letra] = diccionario_frecuencias[letra]+ 1
            else:
                diccionario_frecuencias[letra] = 1

    return diccionario_frecuencias
   
texto = "Este es mi primer proyecto de Python con The Power"
resultado = frecuencias_letras(texto)
print(resultado)

### 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

def doble_valor(numeros):
    """Obtener una lista con el doble del valor de la lista inicial

    Args:
        lista_numeros (_type_): _description_
    """
    return numeros * 2

lista_numeros = [1,2,3,4,5]
print(f"La lista de números antes de duplicar el valor es: {lista_numeros}")

resultado_map = list(map(doble_valor, lista_numeros))
print(f"La lista de números una vez duplicada es: {resultado_map}")

### 3. Función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

lista_palabras = ["bricolaje", "hola", "holanda", "jardin", "granola", "paisaje", "frutas", "caracola"]
palabra_objetivo = "ola"

def palabra_contiene(lista_palabras, palabra_objetivo):
    """Función que permite encontrar palabras que contengan una palabra objetivo dentro de una lista de palabras.

    Args:
        lista_palabras (list): Lista con palabras que pueden contener o no, la palabra objetivo
        palabra_objetivo (str):  Palabra objetivo a encontrar dentro de las palabras de la lista
    
    Returns:
        list: Lista de palabras que contienen la palabra objetivo.
    """
    lista_resultado = []

    for palabra in lista_palabras:
        if palabra_objetivo in palabra:
            lista_resultado.append(palabra.lower())

    return lista_resultado

resultado_palabra_contiene = palabra_contiene(lista_palabras, palabra_objetivo)
print(resultado_palabra_contiene)
    
### 4. Función que calcula la diferencia entre los valores de dos listas, usando map()

Lista1 = [10, 20, 30, 40, 50, 60]
Lista2 = [2, 4, 6, 8, 10, 15]

def diferencia_listas(a, b):

    return a - b

map_diferencia = list(map(diferencia_listas,Lista1, Lista2))
print(map_diferencia)

### 5. Función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado.

lista_notas = [4, 6, 5, 8, 9, 2, 10]

def media_notas (lista_notas, nota_aprobado=5):
    """La función calcula la media de los valores de la lista, y compara con la nota minima de aprobación para determinar el estado del estudiamte.

    Args:
        lista_notas (list): Lista de enteros con las notas del etudiante.
        nota_aprobado (int, optional): Parámetro por defecto con valor 5.

    Returns:
        tupla: tupla con la media de las notas y el estado.
    """
    promedio = sum(lista_notas) / len(lista_notas)

    if promedio >= nota_aprobado:
        estado = "Aprobado"
            
    else:
        estado = "Suspenso"

    return promedio, estado

estado_final = media_notas(lista_notas)
print(estado_final)

### 6. Función que calcule el factorial de un número de manera recursiva

def funcion_factorial(n):

    """Función que calcula el factorial de un número

    Args:
        n (int): Valor al que se le calcula el factorial

    Returns:
        int: valor resultado de aplicar el factorial a n
    """
    if n==1 or n==0:
        return 1    
    return n * funcion_factorial(n-1)
    
resultado_factorial = funcion_factorial(5)
print (resultado_factorial)

### 7. Función que convierta una lista de tuplas a lista de strings usando map()

def funcion_tuplas(tupla):
    """Función que convierte una lista de tuplas a una lista de strings

    Args:
        tupla (tuple): Parámetro de tipo tupla

    Returns:
        str: Devuelve una tupla convertida en string
    """
    tuplas_str = str(tupla)
    return tuplas_str

lista_tuplas= [("Juan", "Enrique"), ("Laura", "Ines", "Sandra")]
tuplas_convertidas = list(map(funcion_tuplas, lista_tuplas))
print(tuplas_convertidas)

### 8. Programa que pide al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.

try:

    numerador = int(input("Elige un numerador de tipo entero para la división"))
    denominador = int(input("Eligen un denominador entero mayor que 0 para la división"))

    division = numerador/denominador
    print(f"La división ha sido exitosa y su resultado es: {division}")

except ValueError:
        print("Debes ingresar valores numéricos")

except ZeroDivisionError:
        print("El denominador introducido no debe ser 0")

### 9. Función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. 
# La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

lista_mascotas = ["Perro", "Gato", "Raton", "Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso", "Huron", "Cobaya", "Lagarto", "Gallina", "Conejo"]

def filtrar_mascotas(lista_mascotas):
    """Función para filtrar mascotas prohibidas de una lista de mascotas.

    Args:
        lista_mascotas (list): Lista de mascotas

    Returns:
        list: Lista generada tras filtrar de la lista de mascotas, las mascotas prohibidas
    """

    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

    return list(filter(lambda mascota: mascota not in mascotas_prohibidas, lista_mascotas))

resultado_filter = filtrar_mascotas(lista_mascotas)
print(resultado_filter)

### 10. Función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

class EmptyListError(Exception):
    pass

def promedio_lista (lista_promedio):
    """Función que calcula el promedio de una lista siempre y cuando no este vacia.

    Args:
        lista_promedio (list): Lista de números

    Raises:
        EmptyListError: Lanza la excepción personalizada para cuando la lista está vacía

    Returns:
        float: Valor numérico del promedio de los números de la lista.
    """

    if not lista_promedio:
        raise EmptyListError ("La lista está vacía")

    return sum(lista_promedio) / len(lista_promedio)

try:
    lista_promedio = []
    resultado_promedio = promedio_lista(lista_promedio)
    print (f"El promedio de los números de la lista es: {resultado_promedio}")

except EmptyListError:
    print("La lista está vacía, no se puede calcular promedio")

### 11. Programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120)

try:

    edad = int(input("Ingrese su edad: "))
    
    if edad<0 or edad>120:
        print("Edad fuera de rango")
    else:
        print(f"La edad del usuario es: ",{edad})

except ValueError:
    print("Debe ingresar un número válido")

    ### 12. Función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def lista_longitudes(frase):
    """Función que separa una frase en cada espacio, y calcula la longitud de cada palabra.

    Args:
        frase (str): Frase tipo string.

    Returns:
        list: lista con las longitudes de cada palabra de la frase.
    """
    return list(map(len, frase.split()))

frase = "Este es mi primer proyecto de Python con The Power"
print(lista_longitudes(frase))

### 13. Función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

def mayus_minus(caracteres):
    """Función para convertir las letras de un texto o conjunto de caracteres, en una tupla de mayuscula y minuscula, que no tenga en cuenta duplicados.

    Args:
        caracteres (str): Caracteres o letras que componen un texto

    Returns:
        list: Lista de tuplas con los caracteres de un texto en mayuscula y minuscula.
    """
    caracteres_unicos = set(caracteres.lower().replace(" ", ""))

    return list(map(lambda caracter: (caracter.upper(), caracter.lower()), caracteres_unicos))
    
caracteres = "Este es mi primer proyecto de Python con The Power"
map_caracteres = mayus_minus( caracteres)
print(map_caracteres)

### 14. Función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

def palabras_inicio (lista_palabras, letra):
    """Función para filtrar de una lista, solo las palabras que comiencen por una letra especifica.

    Args:
        lista_palabras (list): Lista de palabras
        letra (str): Letra con la que inicia las palabras que queremos filtrar

    Returns:
        list: Lista de palabras que cumplen con la condición de la letra de inicio.
    """
    
    return (list(filter(lambda palabra: palabra.lower().startswith(letra.lower()), lista_palabras)))

lista_palabras = ("Amarillo", "Banana", "Casa", "Camión", "Iguana", "Cristal")
print(palabras_inicio( lista_palabras, "C"))

### 15. Función lambda que sume 3 a cada número de una lista dada.

numeros = [1, 2, 3, 4, 5]

lambda_sum3 = list(map((lambda num : num + 3), numeros))
print(lambda_sum3)

### 16. Función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()

def palabras_largas (textos, n):
    """Función que  toma las palabras de longitud mayor que n, de una cadena de texto

    Args:
        textos (str): Texto de donde se deben filtrar las palabras
        n (int): Entero que indica la condición pra filtrar

    Returns:
        list: Lista de palabras de la cadena de texto que cumplen la condición de longitud
    """
    return list(filter((lambda longitud: len(longitud) > n) , textos.split()))

textos = "Este es mi primer proyecto de Python con The Power"
print(palabras_largas(textos, 4))

### 17. Función que tome una lista de dígitos y devuelva el número correspondiente. Usa la función reduce()

from functools import reduce

def lista_a_numero(lista_digitos):
    """Función para convertir una lista de dígitos en un número

    Args:
        lista_digitos (list): Lista de digitos a convertir

    Returns:
        int: Número resultado de convertir los dígitos a número
    """
    return reduce(lambda x, y: x * 10 +y, lista_digitos)

print(lista_a_numero( [1, 2, 3]))

### 18. Programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter() 

estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 22, "calificacion": 85},
    {"nombre": "Marta", "edad": 19, "calificacion": 92}
]

def calificaciones_90 (estudiantes):
    """Función que filtra los diccionarios de estdiantes con calificación mayor o igual que 90

    Args:
        estudiantes (list): Lista de diccionarios de los datos de estudiantes

    Returns:
        list: Lista de diccionarios de estudiantes filtradas por la condición
    """
    return list(filter(lambda estudiante: estudiante["calificacion"] >= 90, estudiantes))

print (calificaciones_90(estudiantes))

### 19. Función lambda que filtre los números impares de una lista dada.

def filtrar_impares(lista_num):
    """Función de tipo lambda que filtra los número impares de una lista de números

    Args:
        lista_num (list): Lista con números pares e impares
    
    Returns:
        list:  Lista de números impares filtrada
    """
    return(list(filter(lambda x: x % 2 != 0, lista_num)))

print(filtrar_impares([1,2,3,4,5,6,7,8,9,10]))

### 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

def filtrar_enteros(lista_mixta):
    """Función para filtrar de una lista de valores variados, los que son extrictamente enteros

    Args:
        lista_mixta (list): Lista con valores de tipo int, str, bool

    Returns:
        list: Lista filtrada con valores solo de tipo entero
    """
    return(list(filter(lambda x : type(x) == int, lista_mixta)))

datos_mixtos = [1, "Hola", 7, "Alegria", 5.3, False, 9]
lista_filtrada = filtrar_enteros(datos_mixtos)
print(lista_filtrada)

### 21. Función que calcule el cubo de un número dado mediante una función lambda

calcular_cubo = lambda x: x ** 3
print(calcular_cubo(5))

### 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce().

from functools import reduce

def producto_valores(lista_producto):
    """Función para calcular elproducto de los valores de una lista

    Args:
        lista_producto (list): Valores numericos
    """
    return(reduce(lambda x, y: x*y, lista_producto))

print(producto_valores([1,2,3,4,5]))

### 23. Concatena una lista de palabras. Usa la función reduce()

from functools import reduce

def concatenar_lista(lista_concatenar):
    """Función para concatenar palabras de una lista mediante reduce()

    Args:
        lista_concatenar (list): Lista de string 

    Returns:
        str: Texto conformado al concatenar las palabras de la lista
    """
    return reduce(lambda x,y: x + " " + y, lista_concatenar)

palabras_concatenar = ["Este", "es", "mi", "primer", "proyecto", "de", "Python"]
print(concatenar_lista(palabras_concatenar))

### 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce()

from functools import reduce

def diferencia_total(lista_diferencia):
    """Función que usa reduce para calcular la diferencia entre los valores de una lista

    Args:
        lista_diferencia (list): Lista de enteros

    Returns:
        int: Número que corresponde a la diferencia entre los valores de la lista
    """
    return reduce(lambda x,y: x - y, lista_diferencia)

valores_diferencia = [2, 4, 6, 8, 10]
print(diferencia_total(valores_diferencia))

### 25. Función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres(texto):
    """Función que cuenta los caracteres de una cadena d etexto excluyendo los espacios.

    Args:
        texto (str): Frase de tipo texto (str)

    Returns:
        int: Número resultado de la cuenta de caracteres
    """
    return len(texto.replace(" ", ""))

frase = "Este es mi primer proyecto de Python con The Power"
print(contar_caracteres(frase))

### 26. Función lambda que calcule el resto de la división entre dos números dados.

resto_division = lambda x, y: x % y

print (resto_division(10,3))
print (resto_division(17,5))

### 27. Función que calcule el promedio de una lista de números.

def promedio_numeros(promedio_num):
    """Función para calcular el promedio de una lista de números,

    Args:
        promedio_num (list): Lista de int o vacía

    Returns:
        float: Valor rsultado de calcular el promedio
    """
    if len(promedio_num) == 0  :
        return 0
        # Manejo de posible error donde se ejecute la función en una lista vacía

    return sum(promedio_num) / len(promedio_num)

nums = []
print(promedio_numeros(nums))




