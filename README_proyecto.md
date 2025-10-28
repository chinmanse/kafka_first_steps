## Introduccion Proyecto

Este readme es para poner en marcha el proyecto para el presente modulo

## Herramientas a usar

### Docker

Si no lo tienes instalado, que esperas?

### Zookeper



## Puesta en Marcha

La puesta en marcha es simple porque de momento estamos trabajando con las imagenes oficiales de kafka, por lo que solo se debe hacer lo siguiente:

### Importacion de las imagenes

En el archivo `docker-compose.proof.yml` se tiene la configuracion basica, por lo que este mismo tiene las imagenes necesarias y para descargarlas se debe ejcutar el siguient jJUnbhu/jniie comando

```bash
docker compose -f docker-compose.proof.yml pull
```

### Puesta en marcha de las imagenes

Para poner en marcha las imagenes debe ejecutar el siguiente comando:

```bash
docker compose -f docker-compose.proof.yml  up -d
```

### Validacion de las imagenes

Para poder visualizar los contenedores que se estan ejecutando puede hacer con el siguiente comando:

```bash
docker ps
```

### Creacion de Topico

Para la creacion de un topico debe ejecutar el siguiente comando:

```bash
docker exec -it maestria-kafka-1 kafka-topics --create --topic events --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

### Inicio del server para la escuha de los eventos

Para inciar el escucha de los eventos deje ejecutar lo siguiente:


```bash
docker exec -it maestria-kafka-1 kafka-topics --list --bootstrap-server localhost:9092
```

### Inicio del producer

Para iniciar el producer debe ejecutar el siguiente comando:

```bash
docker exec -it maestria-kafka-1 kafka-console-producer --topic events --bootstrap-server localhost:9092
```

Esto iniciara el stremaer que solicita se inserte datos, en este caso insertaremos objetos json para validar el funcionamiento de consumer

### Inicio del consumer

Para iniciar el consumer se debe ejecutar el siguiente comando:

```bash
docker exec -it maestria-kafka-1 kafka-console-consumer --topic events --bootstrap-server localhost:9092 --from-beginning
```

El consumer se encuentra vigilante del producer, por lo que los objetos que enviemos a este sera replicados aqui