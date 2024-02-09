FROM bitnami/kafka:3.4


#cria o diretório para resolver o erro de rodar o apt install*
USER root
RUN mkdir -p /var/lib/apt/lists/partial


WORKDIR /app


# Instala o Python e outras dependências necessárias
RUN apt-get update && \
   apt-get install -y python3 python3-pip && \
   pip3 install --upgrade pip


RUN pip3 install confluent_kafka kafka-python


#copia os arquivos necessários para criar o tópico, rodar o consumer e o producer
COPY requirements.txt /app/
COPY consumer.py /app/
COPY producer.py /app/
COPY create-topic.py /app/


#Copia o arquivo server.properties e subistitui o original (apenas para ativar a config de jmx)
COPY server.properties /opt/bitnami/kafka/config/


#Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt


COPY . /app