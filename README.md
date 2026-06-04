# CaféCol CloudApp

Enlace al video demostrativo:
https://youtu.be/dkQJtM9nZF8


Proyecto# 2
Cloud Computing
Presentado por:

David Guillermo Naranjo Ochoa; 
Sebastian Berrio; 
Sebastian Amaya

## Descripción

CaféCol CloudApp es una aplicación web serverless desplegada en AWS para registrar pedidos de café.

La solución utiliza servicios administrados de AWS para proporcionar una arquitectura escalable, económica y fácil de mantener.

## Arquitectura

Servicios utilizados:

* Amazon S3
* Amazon API Gateway
* AWS Lambda
* Amazon DynamoDB
* Amazon CloudWatch

## Flujo de funcionamiento

1. El usuario accede al sitio web alojado en Amazon S3.
2. El formulario envía una solicitud HTTP POST.
3. Amazon API Gateway recibe la solicitud.
4. AWS Lambda procesa el pedido.
5. DynamoDB almacena la información.
6. CloudWatch registra métricas y logs.

## Tecnologías

### Frontend

* HTML
* JavaScript

### Backend

* Python
* AWS Lambda

### Base de Datos

* Amazon DynamoDB

## Arquitectura AWS

El diagrama de arquitectura se encuentra en:

```text
infrastructure/arquitectura-drawio.png
```

## Estimación de Costos

Costo mensual estimado:

```text
USD 2.09
```

Costo anual estimado:

```text
USD 25.08
```

## Autor

Proyecto académico desarrollado para la asignatura de Cloud Computing.
David Guillermo Naranjo;  Sebastian Berrio;   Sebastian Amaya.

