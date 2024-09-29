import time
import random
from pubsub import PubSub  # Importa a classe PubSub

def producer(pubsub):
    flavors = ['pistache', 'morango', 'chocolate', 'baunilha']
    
    # Publicar apenas 5 anúncios
    for _ in range(5):
        time.sleep(random.randint(2, 5))  # Espera aleatória entre anúncios
        flavor = random.choice(flavors)
        pubsub.publish(f"Novo sabor de sorvete: {flavor} disponível!")
    
    print("[Produtor] Todos os anúncios foram publicados.")

if __name__ == "__main__":
    pubsub = PubSub()
    producer(pubsub)
