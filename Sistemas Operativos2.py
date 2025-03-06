import threading  # Importamos el módulo threading para trabajar con hilos

# Creamos una barrera para sincronizar dos hilos
barrera = threading.Barrier(2)  # La barrera espera a que 2 hilos lleguen a este punto

# Función que ejecuta la tarea de imprimir un mensaje y esperar en la barrera
def tarea():
    print("Hilo iniciado")  # Mensaje que indica que el hilo ha comenzado.
    # Esperamos en la barrera
    barrera.wait()  # El hilo se bloquea aquí hasta que el número de hilos (2) haya llamado a la función wait.
    print("Hilo continuando")  # Mensaje que indica que el hilo puede continuar después de que ambos hilos han llegado a la barrera

# Creamos dos hilos que ejecutarán la misma tarea
hilo1 = threading.Thread(target=tarea)  # Hilo 1
hilo2 = threading.Thread(target=tarea)  # Hilo 2

# Iniciamos los hilos
hilo1.start()  # Se ejecuta el hilo 1
hilo2.start()  # Se ejecuta el hilo 1

# Esperamos a que ambos hilos terminen
hilo1.join()  # Esperamos a que el hilo 1 termine
hilo2.join()  # Esperamos a que el hilo 2 termine

print("Programa terminado")  # Mensaje que indica que el programa ha finalizado