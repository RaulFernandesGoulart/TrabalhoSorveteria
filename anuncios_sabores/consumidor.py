import threading
import time
from pubsub import PubSub, Subscriber  # Importa as classes PubSub e Subscriber

def consumer(pubsub, name):
    subscriber = Subscriber(name)
    pubsub.subscribe(subscriber)
    
    # Mantém o consumidor rodando
    try:
        while True:
            time.sleep(1)  # Mantém o loop ativo
    except KeyboardInterrupt:
        print(f"{name} parou de receber anúncios.")

if __name__ == "__main__":
    pubsub = PubSub()

    # Criação de threads para consumidores
    consumer_threads = []
    for i in range(3):  # 3 clientes
        name = f"Cliente-{i + 1}"
        thread = threading.Thread(target=consumer, args=(pubsub, name))
        consumer_threads.append(thread)
        thread.start()

    # Esperando o término dos threads de consumidores
    for thread in consumer_threads:
        thread.join()
