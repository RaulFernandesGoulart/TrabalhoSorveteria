# TrabalhoSorveteria

Estrutura:

/ProjetoSorveteria
│
├── pedidos_sorvete
│   ├── consumidor.py         # Atendente que processa os pedidos de sorvete
│   └── produtor.py           # Cliente que envia os pedidos de sorvete
│
├── anuncios_sabores
│   ├── consumidor.py         # Clientes inscritos que recebem anúncios de novos sabores
│   |└── produtor.py           # Sorveteria que anuncia novos sabores
│   |____ pubsub.py             #config
├── README.md                 # Instruções sobre como rodar o projeto
└── requirements.txt          # Dependências do projeto (bibliotecas)



Este projeto contém duas aplicações para a comunicação entre clientes e sorveteria utilizando RabbitMQ:

1. **Fila de Mensagens (Pedidos de Sorvete)**: Um sistema de pedidos onde os clientes enviam seus pedidos e o atendente processa um por vez.
2. **Pub/Sub (Anúncios de Sabores)**: Um sistema onde a sorveteria anuncia novos sabores e todos os clientes inscritos recebem a notificação.

## Como rodar o projeto

### Requisitos:
- Python 3.x
- RabbitMQ instalado e rodando na máquina
- Instalar as dependências listadas em `requirements.txt`:
  ```bash
  pip install -r requirements.txt

  
Execução:
Em cada Aplicação deve ser executado primeiramente o produtor depois o executor