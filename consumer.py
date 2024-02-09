from kafka import KafkaConsumer


# Configurações do Kafka
bootstrap_servers = 'localhost:9092'
topic_name = 'test-topic'


# Cria um consumidor Kafka
consumer = KafkaConsumer(
   topic_name,
   bootstrap_servers=bootstrap_servers,
   auto_offset_reset='earliest', 
   group_id='test-group'
)


# Consome mensagens do tópico
for message in consumer:
   print(f'Mensagem recebida: {message.value.decode("utf-8")}')