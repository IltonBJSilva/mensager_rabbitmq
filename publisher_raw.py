import pika

def my_callback(ch, method, properties, body):
    print(body)


connection_parameters = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest"
    )
)

while True:
    mensagem_enviar = str(input("Qual Mensagem deseja enviar: "))
    channel = pika.BlockingConnection(connection_parameters).channel()
    channel.basic_publish(
        exchange="data_exchange",
        routing_key="",
        body=mensagem_enviar,
        properties=pika.BasicProperties(
            delivery_mode=2
        )
    )


