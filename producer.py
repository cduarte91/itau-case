from kafka import KafkaProducer


# Configurações do Kafka
bootstrap_servers = 'localhost:9092'
topic_name = 'test-topic'


# Cria um produtor Kafka
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)


# Envia mensagens para o tópico
for i in range(10):
   message = f'Mensagem de exemplo {i}'
   producer.send(topic_name, value=message.encode('utf-8'))
   print(f'Enviada mensagem: {message}')


producer.close()
