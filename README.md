Desarrollo del curso Análisis de Datos con Python (300 horas) por freeCodeCamp


# Entornos Virtuales en python

## Crear un entrono virtual con anaconda
´´´python
conda create -n {NOMBRE_ENTORNO} python={VERSION_PYTHON}
´´´

## Activar un entorno virtual
´´´python
conda activate {NOMBRE_ENTORNO}
´´´

## Desactivar un entorno virtual
conda deactivate

## Visualizar paquetes con su versión
pip freeze

### Entornos virtuales para administración de paquetes
### Instalación del paquete
pip install virtualenv

#### Creación del entorno virtual
virtualenv {NOMBRE_ENTORNO}

#### Activar el entorno virtual
.\{NOMBRE_ENTORNO}\Scripts\activate

#### Desactivar el entorno virtual
deactivate

## Instalar paquetes en python según version
pip install {NOMBRE_PAQUETE}-contrib-python=={VERSION_PAQUETE}