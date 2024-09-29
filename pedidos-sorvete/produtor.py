import pika

# Configurações de conexão
credentials = pika.PlainCredentials('iclzcyph', 'MuFk0EzKWjecVfPQ1i3YDimJEMU3DEmP')
parameters = pika.ConnectionParameters('jackal.rmq.cloudamqp.com', 5672, 'iclzcyph', credentials)

# Conectando ao RabbitMQ
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Declarando a fila
channel.queue_declare(queue='pedidos_sorvete')

# Exemplo de pedido de sorvete
pedido = "Sorvete de chocolate"

# Publicando o pedido na fila
channel.basic_publish(exchange='', routing_key='pedidos_sorvete', body=pedido)
print(f"[x] Pedido enviado: {pedido}")

# Fechando a conexão
connection.close()
