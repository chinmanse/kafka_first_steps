## Introduccion Proyecto

Este readme es para poner en marcha el proyecto para el presente modulo

## Herramientas a usar

### Docker

Si no lo tienes instalado, que esperas?

## Puesta en marcha

### Construccion de las imagenes

```
docker build . -f compose/kafka/Dockerfile -t proy_cron
docker build . -f compose/mongo/Dockerfile -t proy_mongo
```

### Puesta en marcha

```
docker compose -f docker-compose.proyecto.yml up -d
```

### Parada de los dockers

```
docker compose -f docker-compose.proyecto.yml down
```