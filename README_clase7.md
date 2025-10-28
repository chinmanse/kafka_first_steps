## Introduccion

Este readme solo expresa lo avanzado en la clase 8, se mantiene muchos conceptos de la clase anterior

## Puesta en Marcha

### Paso 1

```bash
docker exec -it [container_name] kafka-topics --create --topic user_events --bootstrap-server localhost:9092 --replication-factor 1 --partitions 3
```

### Paso 2


```bash
docker exec -it [container_name] kafka-topics --create --topic user_events --bootstrap-server localhost:9092 --replication-factor 1 --partitions 3
```

### Paso 3


```bash
docker exec -it [container_name] kafka-topics --list --bootstrap-server localhost:9092
```
