# geoperfil-etl
Extracción, procesamiento de artículos y guardado de entidades

## SetUp del entorno

- sudo apt-get update
- sudo apt install python3-pip
- sudo apt-get install -y build-essential
- sudo apt-get install -y python3.X-dev
- sudo apt-get install -y libpq-dev

(opcional, ya que las librerias se instalan dentro el virtualenv)
- pip3 install -U spacy
- python3 -m spacy download es_core_news_md

## Preparación

1. Agregar el virtualenv dentro de la carpeta del proyecto: python3 -m venv .venv/

2. Activar el virtualenv: source ./bin/activate

3. Actualizar pip: pip install --upgrade pip wheel

4. Instalar las dependencias: pip install -r requirements.txt

## Despliegue

Ejecutar el comando `python main.py` con el entorno virtual activado.

## Notas

En caso de que falle la instalación de las librerias en algun punto, buscar la forma de instalarlos aparte ya que python es muy facil de romper y trae problemas de compatibilidad la mayor parte del tiempo.