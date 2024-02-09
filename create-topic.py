from confluent_kafka.admin import AdminClient, NewTopic


def create_topic(bootstrap_servers, topic_name, num_partitions, replication_factor):
   # Configurações para o AdminClient
   conf = {'bootstrap.servers': bootstrap_servers}
   # Cria um objeto AdminClient
   admin_client = AdminClient(conf)
   # Cria o tópico
   new_topic = NewTopic(topic_name, num_partitions=num_partitions, replication_factor=replication_factor)
   # Chama a API para criar o tópico
   admin_client.create_topics([new_topic])
   print("Tópico criado com sucesso:", topic_name)


if __name__ == "__main__":
   bootstrap_servers = 'localhost:9092'  # Endereço do servidor Kafka
   topic_name = 'test-topic'             # Nome do tópico que você deseja criar
   num_partitions = 3                    # Número de partições para o tópico
   replication_factor = 2                # Fator de replicação para o tópico


   create_topic(bootstrap_servers, topic_name, num_partitions, replication_factor)
