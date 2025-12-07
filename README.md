# Trabajo Teorico de Algoritmos
**Las explicaciones teoricas del algoritmo GSA y otros datos importantes estan en el pdf**


**El código es una modificación del algoritmo GSA del repositorio de Himanshu Mittal de nombre HimanshuRepo**
# Guía de Instalación y Ejecución del Algoritmo GSA

## 1. Instalar Python

Asegúrate de tener Python instalado (versión 3.6 o superior):

- Descarga Python desde [python.org](https://www.python.org/downloads/)
- Durante la instalación, marca la opción **"Add Python to PATH"**
- Verifica la instalación abriendo CMD y ejecutando:

```bash
python --version
```

## 2. Clonar o descargar los archivos

OPCIÓN 1: descargar este si desea el original
```bash
git clone https://github.com/himanshuRepo/Gravitational-Search-Algorithm.git
```

OPCIÓN 2: descargar el modificado desde este git
```bash
git clone https://github.com/TheSweetPancake/trabajoTeoricoAlgoritmos.git
```
## 3. Instalar dependencias

Abre CMD/PowerShell y navega a la carpeta del proyecto:

```bash
cd C:\GSA_Project
```

Instala las dependencias:
```bash
pip install numpy scipy scikit-learn matplotlib
```

## 4. Ejecutar el algoritmo
```bash
python optimizer.py
```

## Descripción del Comando

Este comando realiza las siguientes acciones:

1. **Ejecuta GSA** con la función **F1 (esfera)** definida en `benchmarks.py`.
2. **Genera un archivo CSV** con los resultados del experimento, nombrado como:  
   `experiment<fecha-hora>.csv`
3. **Muestra gráficos fitness** al finalizar la ejecución.
