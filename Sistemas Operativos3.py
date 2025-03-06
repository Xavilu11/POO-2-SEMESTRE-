import threading  # Importamos el módulo threading para trabajar con hilos
import time  # Importamos el módulo time para usar funciones relacionadas con el tiempo

# Creamos un objeto evento
evento = threading.Event()  # Este objeto se utilizará para la sincronización entre hilos

# Función que espera a que se active el evento
def esperar_evento():
    print("Esperando al evento...")  # Mensaje que indica que el hilo está esperando
    # Esperamos a que el evento se active
    evento.wait()  # El hilo se bloquea aquí hasta que el evento sea activado
    print("El evento ha sido activado!")  # Mensaje que indica que el evento ha sido activado
    # Función esperar_evento:
    # - Imprime un mensaje indicando que está esperando el evento.
    # - Llama a evento.wait(), lo que hace que el hilo se bloquee hasta que el evento sea activado por otro hilo.

# Función que activa el evento después de un cierto tiempo
def activar_evento():
    print("Esperando 5 segundos antes de activar el evento...")  # Mensaje que indica que se está esperando
    time.sleep(5)  # Pausa la ejecución durante 5 segundos
    # Activamos el evento
    evento.set()  # Esto activa el evento, permitiendo que los hilos que están esperando continúen
    print("El evento ha sido activado después de 5 segundos")  # Mensaje que indica que el evento ha sido activado
    # Función activar_evento:
    # - Imprime un mensaje indicando que esperará 5 segundos antes de activar el evento.
    # - Utiliza time.sleep(5) para pausar la ejecución durante 5 segundos.
    # - Luego, llama a evento.set(), que activa el evento y permite que cualquier hilo que esté esperando en evento.wait() continúe su ejecución.

# Creamos dos hilos que ejecutarán las funciones
hilo1 = threading.Thread(target=esperar_evento)  # Hilo que espera el evento
hilo2 = threading.Thread(target=activar_evento)  # Hilo que activa el evento

# Iniciamos los hilos
hilo1.start()  # Comenzamos la ejecución del hilo que espera el evento
hilo2.start()  # Comenzamos la ejecución del hilo que activa el evento

# Esperamos a que ambos hilos terminen
hilo1.join()  # Esperamos a que el hilo que espera el evento termine
hilo2.join()  # Esperamos a que el hilo que activa el evento termine
# Esperar a que Terminen: Se utiliza join() para esperar a que ambos hilos terminen su ejecución antes de continuar con el programa principal.

print("Programa terminado")  # Mensaje que indica que el programa ha finalizado
# Impresión del Resultado: Finalmente, se imprime un mensaje indicando que el programa ha terminado.