#!/bin/bash

# Genera el archivo de migración con el mensaje que le pases
docker compose exec backend flask db migrate -m "$1"

# Aplica la migración a la base de datos 
docker compose exec backend flask db upgrade