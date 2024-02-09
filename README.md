# Bem-vindo ao repositório do Kafka, ou melhor, Carlos-kafka!

Neste repositório, você encontrará os arquivos necessários para configurar nossa infraestrutura utilizando as seguintes tecnologias:

- Kafka 3.4.0
- Zookeeper 7.6.0 (latest)
- Prometheus 2.4.9 (latest)
- Grafana 10.3.1 (latest)
- Python 3.12.1


# Referencias Utilizadas:

Kafka-python Lib
https://kafka-python.readthedocs.io/en/master/

Confluent
https://docs.confluent.io/platform/current/installation/docker/operations/monitoring.html

Wurstmeister Kafka Repository:
https://github.com/wurstmeister/kafka-docker

Chat GPT 3.5
https://chat.openai.com/


# Instruções Gerais:      

Essas aplicações são executadas usando um arquivo compose do Docker.

Antes de clonar o repositório, certifique-se de ter instalado o Docker for Desktop. Se ainda não o fez, você pode baixá-lo no link abaixo:

[Download Docker Desktop](https://www.docker.com/products/docker-desktop/)

Para iniciar a aplicação, basta clonar o repositório usando o seguinte comando:

```bash
git clone https://github.com/cduarte91/itau-case.git
```

Em seguida, acesse a pasta do repositório clonado e execute o seguinte comando:

```bash
docker-compose up
```

E magicamente tudo estará funcionando.


Para executar os testes da aplicação, basta conectar no container do kafka (de preferência em dois terminais diferentes) e executar os comandos abaixo:


Conectar no container kafka:
```bash
docker exec -it kafka /bin/bash
```

Após conectar no container nos dois terminais, executar os comandos abaixo para validar:

No terminal 1 executar:

Criar o tópico.
```bash
python3 create-topic.py
```

Iniciar o Cosumidor.
```bash
python3 consumer.py
```

No terminal 2 executar:

```bash
python3 producer.py
```


Após isso, já teremos as mensagens sendo entregues no terminal 1.



Para acessar o Prometheus, basta utilizar a seguinte URL:

[Prometheus - https://localhost:9090](https://localhost:9090)

Para acessar o Grafana:

[Grafana - https://localhost:3000](https://localhost:3000)


## Observações:

No arquivo `Docker-compose.yml`, o serviço "Kafka" está configurado para baixar a imagem "cduarte91/carlos-kafka-3.4" de um repositório público.

Se você preferir construir a imagem localmente, basta navegar até o diretório da aplicação e executar o seguinte comando:

```bash
docker build -t carlos-kafka-3.4 .
```

Além disso, é necessário alterar a linha 13 do arquivo `Docker-compose.yml`, substituindo "cduarte91/carlos-kafka-3.4" por apenas "carlos-kafka-3.4".





