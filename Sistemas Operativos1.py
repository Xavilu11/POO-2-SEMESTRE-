# Explicación del código:
# 1. Importación: Se importa el módulo necesario para trabajar con hilos.
# 2. Variable Global: Se define una variable que será compartida entre los hilos.
# 3. Mutex: Se crea un objeto mutex para controlar el acceso a la sección crítica.
# 4. Función `incrementar`: Se asegura que solo un hilo pueda incrementar el contador a la vez.
# 5. Función `tarea`: Se define la tarea que cada hilo ejecutará.
# 6. Creación y Ejecución de Hilos: Se crean e inician dos hilos que ejecutan la misma tarea.
# 7. Esperar a que Terminen: Se espera a que ambos hilos terminen su ejecución antes 
# de imprimir el resultado.
# 8. Impresión del Resultado: Se muestra el valor final del contador global, 
# que debe ser correcto gracias al uso del mutex.


import threading  # Se importa el módulo threading para trabajar con hilos

# Definimos una variable global compartida
contador_global = 0  # Esta variable se comparte entre los hilos

# Creamos un objeto mutex
mutex = threading.Lock()  # Este objeto se va a utilizar para asegurar el acceso exclusivo 
                            #a la sección crítica

# Función que incrementa el contador global de forma segura utilizando un mutex
def incrementar():
    global contador_global  # Indicamos que vamos a usar la variable global
    mutex.acquire()  # Adquirimos el mutex para asegurar que solo un hilo acceda 
                        #a la sección crítica
    try:
        # Sección crítica: Incrementamos el contador
        contador_global += 1  # Indicamos que solo un hilo puede ejecutar esta línea a la vez
    finally:
        # Liberamos el mutex (Esto se hace para que otros hilos puedan acceder a la función)
        mutex.release()  # Con esto se asegura que el mutex se libere incluso si ocurre un error

# Función que ejecuta la tarea de incrementar el contador un número determinado de veces
def tarea():
    for _ in range(100000):  # Esto sirve para que el contador se ejecute 100,000 veces
        incrementar()  # Llama a la función que incrementa el contador de forma segura

# Creamos dos hilos que ejecutarán la misma tarea
hilo1 = threading.Thread(target=tarea)  # Hilo 1
hilo2 = threading.Thread(target=tarea)  # Hilo 2

# Iniciamos los hilos
hilo1.start()  # Comienza a ejecutar el hilo 1
hilo2.start()  # Comienza a ejecutar el hilo 2

# Esperamos a que ambos hilos terminen
hilo1.join()  # Esperamos a que el hilo 1 termine
hilo2.join()  # Esperamos a que el hilo 2 termine

# Imprimimos el valor final del contador global
print("El valor final del contador global es:", contador_global)  
# Debería ser 200000 si todo funciona correctamente

