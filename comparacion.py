#GALLEGOS LIZARRAGA RUDY ALEX
import threading
import multiprocessing
import random
import time

#ALEATORIO CONCU

#wolker es operac
#tdi es seleccionador
def worker(tid, a, b, c):
    c[tid] = a[tid] * b[tid]

if __name__ == "__main__":
    # aqi as aleatorias  para a y b
    a = [random.randint(1, 3) for _ in range(5)]
    b = [random.randint(1, 10) for _ in range(5)]
    c = [0] * 5  #aqui almacena

    start_time = time.time()  # esto inicia time

    threads = []
    for tid in range(5):
        thread = threading.Thread(target=worker, args=(tid, a, b, c))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()  # para acabar time

    # Imprime !!!
    print("Buenos dias este es el primer aleatorio:", a)
    print("el segundo:", b)
    print("la multiplicacion es:", c)
    print("Tiempo de ejecución :", end_time - start_time, "segundos")


#ALEATORIO PARAL

def worker(tid, a, b, c):
    c[tid] = a[tid] * b[tid]

if __name__ == "__main__":
    # Genera aleatorio
    a = [random.randint(1, 3) for _ in range(5)]
    b = [random.randint(1, 10) for _ in range(5)]
    c = multiprocessing.Array('i', 5)  # Array compartido para resultados

    start_time = time.time()

    processes = []
    for tid in range(5):
        process = multiprocessing.Process(target=worker, args=(tid, a, b, c))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()

    # Imprim
    print("Aleatorio a:", a)
    print("Aleatorio b:", b)
    print("MULTPLICACION:", list(c))
    print("Tiempo de ejecución :", end_time - start_time, "segundos")

    #añade diferencia de timpo de a y b
    print(">> La diferencia de timpo de ambos es:aqui pones la resta¡¡¡¡")

