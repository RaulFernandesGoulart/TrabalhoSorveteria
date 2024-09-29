import pika

# Configurações de conexão
credentials = pika.PlainCredentials('iclzcyph', 'MuFk0EzKWjecVfPQ1i3YDimJEMU3DEmP')
parameters = pika.ConnectionParameters('jackal.rmq.cloudamqp.com', 5672, 'iclzcyph', credentials)

# Conectando ao RabbitMQ
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Declarando a fila
channel.queue_declare(queue='pedidos_sorvete')

def callback(ch, method, properties, body):
    print(f"[x] Pedido recebido: {body.decode()}")
    print("[x] Preparando sorvete...")
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Consumindo as mensagens da fila
channel.basic_consume(queue='pedidos_sorvete', on_message_callback=callback)

print(' [*] Esperando pedidos de sorvete...')
channel.start_consuming()
