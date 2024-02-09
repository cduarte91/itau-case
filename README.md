# Bem-vindo ao repositório do Kafka, ou melhor, Carlos-kafka!

Neste repositório, você encontrará os arquivos necessários para configurar nossa infraestrutura e executar as seguintes aplicações:

- Kafka
- Zookeeper
- Prometheus
- Grafana

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