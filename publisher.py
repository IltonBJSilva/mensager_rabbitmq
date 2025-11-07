import pika
import json
from typing import Dict

class RabbitmqPublisher:
    def __init__(self) -> None:
        self.__host = "localhost"
        self.__port = 5672
        self.__username = "guest"
        self.__passwrod = "guest"
        self.__routing_key = "RK"
        self.__exchange = "data_exchange"
        self.__channel = self.__create_channel()
    
    def __create_channel(self):
        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(
                username=self.__username,
                password=self.__passwrod
            )
        )

        channel = pika.BlockingConnection(connection_parameters).channel()
        return channel
    
    def send_menssage(self, body: Dict):
        self.__channel.basic_publish(
            exchange=self.__exchange,
            routing_key=self.__routing_key,
            body=json.dumps(body, ensure_ascii=False).encode("utf-8"),
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )
    


rabbitmq_publisher = RabbitmqPublisher()





while True:
    mensagem_enviar = str(input("Qual Mensagem deseja enviar: "))
    try:
        payload = json.loads(mensagem_enviar)

    except:
        #rabbitmq_publisher.send_menssage({"mensagem": mensagem_enviar})
        payload = {"mensagem": mensagem_enviar}
    
    rabbitmq_publisher.send_menssage(payload)