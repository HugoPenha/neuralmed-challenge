# Neuralmed Challenge

Objetivo:
Implemente uma API REST que recebe uma imagem e envie a imagem através de uma fila para uma segunda aplicação que a redimensione para o tamanho de 384x384.

## Features

- Endpoint para receber uma imagem e enviar para uma fila
- Validações
- Consumir conteúdo da fila
- Redimensionar o tamanho do conteúdo para 384x384 e salvar imagem modificada

## File Structure - First Application (API - Producer)

- Main - Arquivo principal de configurações servidor e endpoint
- Services - Responsável por contes as funções de manipulação, conexão com o RabbitMQ e processamento dos dados

## File Structure - Second Application (Consumer)

- Main - Core do script contendo as funções para consumo de fila e redimensionamento da mensagem recebida

## Tech

Tecnologias utilizadas para o desenvolvimento

- Python 3
- RabbitMQ 
- FastAPI
- Docker 


## Run
```sh
cd neuralmed-challenge
docker-compose up
```

```sh
Application running on 127.0.0.1:8000
```

## Requests Examples
```sh
...
POST http://127.0.0.1:8000/uploadfile/
Body (form-data):
key: file value:image.jpg
```

## Extras
- **Se o tamanho for parametrizável como você mudaria a sua arquitetura?**
-- Seria necessário uma alteração na camada da API para o recebimento desses parametros de dimensão, e assim, os enviando em conjunto na mensagem para fila onde ao chegar na aplicação de consumir utilizaria esses valores de forma dinamica. Também seria importante realizar uma validação ou até uma restrição para tamanhos muito grandes que possam impactar o sistema, possívelmente um tratamento a parte para esses casos. 

- **É possível melhorar a performance da solução? Como as melhorias impactam a leitura e manutenção do código?**
-- Sim é possível. A utilização de background tasks poderia otimizar a aplicação em conjunto com utilização de mais filas para determinados casos específicos de acordo com sua prioridade. Uma alternativa poderia ser em relação a uma solução que utilizasse mais filas e mais consumers onde por exemplo tendo range de tamanho para definir em qual fila uma mensagem iria, e assim, definindo a prioridade e tamanho dessas filas para que as mais simples fossem executadas com uma prioridade maior. Ex: 
    50 - 100mb : Fila 1
    100 - 150mb : Fila 2
    ...
Algumas configurações também são importantes para uma performance maior como por exemplo setar um tamanho máximo de fila, dividir as filas em diferentes clusters e entre outras. A manutenção numa solução planejada dessa forma seria sempre referente a entender qual tamanho estamos lidando, lidando por blocos e assim acabaria facilitando numa leitura de código pois cada caso teria seu lugar específico de execução.  
 

- **De que forma o sistema pode escalar com a arquitetura planejada?**
-- Conforme o sistema fosse crescendo, como a solução foi pensada sendo uma arquitetura de microserviços com a utilização de filas, a escalabilidade da aplicação pode ser feita de forma horizontal, aumentando os clusters responsáveis conforme a necessidade. A arquitetura de microserviços facilita nesse ponto, podendo sempre incluir novos microserviços para determinados problemas ou para otimização de algo já existente, e isso também cria a facilidade de adotar por novas aplicações com a liberdade de escolher as melhores tecnologias para tal, já que um microserviço não impacta diretamente o outro. 