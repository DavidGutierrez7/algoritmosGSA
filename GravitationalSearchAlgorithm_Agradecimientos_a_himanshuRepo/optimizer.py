# -*- coding: utf-8 -*-
import GSA as gsa
import benchmarks
import csv
import numpy
import time
import matplotlib.pyplot as plt

def selector(algo, func_details, popSize, Iter):
    function_name = func_details[0]
    lb = func_details[1]
    ub = func_details[2]
    dim = func_details[3]
    
    if algo == 0:
        return gsa.GSA(getattr(benchmarks, function_name), lb, ub, dim, popSize, Iter)

# Configuración
GSA = True
F1 = True
PopSize = 50
iterations = 500
Export = True
ExportToFile = "experiment" + time.strftime("%Y-%m-%d-%H-%M-%S") + ".csv"

# Ejecutar
if GSA and F1:
    func_details = benchmarks.getFunctionDetails(0)
    x = selector(0, func_details, PopSize, iterations)

    # Mostrar resultados
    print("\n--- Resultados finales ---")
    print("Mejor solución encontrada:", x.bestIndividual)
    print("Mejor fitness:", x.best)
    print("Tiempo de ejecución:", x.executionTime, "segundos")

    # Plot de fitness inicial
    plt.figure(figsize=(10, 6))
    plt.scatter(range(len(x.initialFitness)), x.initialFitness, color='blue', marker='o', label='Fitness Inicial')
    plt.title("Distribución de Fitness en la Primera Iteración")
    plt.xlabel("Individuo")
    plt.ylabel("Fitness")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot de convergencia
    plt.figure(figsize=(10, 6))
    plt.plot(x.convergence, label='Convergencia')
    plt.title("Convergencia de GSA para " + func_details[0])
    plt.xlabel("Iteración")
    plt.ylabel("Fitness")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot de fitness final
    plt.figure(figsize=(10, 6))
    plt.scatter(range(len(x.finalFitness)), x.finalFitness, color='red', marker='o', label='Fitness Final')
    plt.title("Distribución de Fitness en la Última Iteración")
    plt.xlabel("Individuo")
    plt.ylabel("Fitness")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Exportar a CSV
    if Export:
        with open(ExportToFile, 'w', newline='') as out:
            writer = csv.writer(out)
            writer.writerow(["Iteración", "Fitness"])
            for i, val in enumerate(x.convergence):
                writer.writerow([i + 1, val])
