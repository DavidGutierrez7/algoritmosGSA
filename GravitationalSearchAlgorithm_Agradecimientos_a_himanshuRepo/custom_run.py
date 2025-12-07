import GSA as gsa
from benchmarks import F1

# Configuración
dim = 10      # Dimensión (cambiar a 30 para seguir el benchmark)
PopSize = 50  # Tamaño de población
iters = 500   # Iteraciones

# Ejecutar GSA
result = gsa.GSA(F1, -100, 100, dim, PopSize, iters)

# Resultados
print("Mejor solución:", result.bestIndividual)
print("Mejor fitness:", result.best)

import matplotlib.pyplot as plt

plt.plot(result.convergence)
plt.title("Convergencia de GSA")
plt.xlabel("Iteración")
plt.ylabel("Fitness")
plt.show()