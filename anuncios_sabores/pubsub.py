class PubSub:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        print(f"{subscriber.name} se inscreveu para receber anúncios de novos sabores.")

    def publish(self, message):
        print(f"[Sorveteria] Anunciando: {message}")
        for subscriber in self.subscribers:
            subscriber.receive(message)

class Subscriber:
    def __init__(self, name):
        self.name = name

    def receive(self, message):
        print(f"{self.name} recebeu: {message}")
