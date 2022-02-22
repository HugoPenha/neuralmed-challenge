# Neuralmed Challenge

Objetivo:
Implemente uma API REST que recebe uma imagem e envie a imagem através de uma fila para uma segunda aplicação que a redimensione para o tamanho de 384x384.

## Features

- Endpoint para receber uma imagem e enviar para uma fila
- Consumir conteúdo da fila
- Redimensionar o tamanho do conteúdo para 384x384

## File Structure

- main - Requests do projeto e core da aplicação
- Services - Responsável por contes as funções de manipulação e processamento dos dados

## Tech

Tecnologias utilizadas para o desenvolvimento

- Python 3
- RabbitMQ 
- FastAPI
- Docker 


## Run
```sh
cd 
docker-compose up
```

```sh
Application running on 127.0.0.1:8000
```

## Requests Examples
```sh
...
POST http://
```


Link para collection do Postman:
https://