#GALLEGOS LIZARRAGA RUDY ALEX
#array aleatorio concurrente
import threading
#para num aleatorio
import random

def worker(tid, a, b, c):
    c[tid] = a[tid] * b[tid]

if __name__ == "__main__":
    # Generar ALEATORIOS
    a = [random.randint(1, 3) for _ in range(5)]
    b = [random.randint(1, 10) for _ in range(5)]
    c = [0] * 5  # ALMACENA

    threads = []
    for tid in range(5):
        thread = threading.Thread(target=worker, args=(tid, a, b, c))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Imprimw
    print("Aleatorio a:", a)
    print("Aleator b:", b)
    print("GUarda c (resultado):", c)

