Retomando el vuelo con un mini-repaso de graficos con python usando matplotlib

# 🎨 Visualizaciones con Matplotlib

Esta guía muestra cómo crear gráficos básicos con `matplotlib`, superponer líneas en gráficos de dispersión, y cómo combinar múltiples visualizaciones en una misma figura.

## 1. 📈 Gráfico básico con Matplotlib

```python
import matplotlib.pyplot as plt
import numpy as np

# Datos
t = np.linspace(0, 10, 100)
y = np.sin(t)

# Crear gráfico
plt.figure(figsize=(8, 4))
plt.plot(t, y, label='sin(t)', color='blue', linestyle='-', marker='')
plt.title('Gráfico de la función seno')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
````

## 2. 🔁 Superponer líneas sobre un Scatterplot

```python
np.random.seed(42)
x = np.random.rand(50)
y = 2 * x + 1 + np.random.normal(scale=0.1, size=50)

# Línea de regresión esperada
x_line = np.linspace(0, 1, 100)
y_line = 2 * x_line + 1

# Crear scatter + línea
plt.figure(figsize=(6, 4))
plt.scatter(x, y, label='Datos', color='darkorange')
plt.plot(x_line, y_line, color='blue', label='y = 2x + 1')
plt.title('Scatterplot con línea superpuesta')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
```

## 3. 📊 Figura con 3 visualizaciones

```python
fig, axs = plt.subplots(1, 3, figsize=(15, 4))

# 1. Scatterplot
axs[0].scatter(x, y, color='darkorange')
axs[0].plot(x_line, y_line, color='blue')
axs[0].set_title('Scatterplot')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')
axs[0].grid(True)

# 2. Histograma
axs[1].hist(y, bins=10, color='green', alpha=0.7)
axs[1].set_title('Histograma de y')
axs[1].set_xlabel('y')
axs[1].set_ylabel('Frecuencia')
axs[1].grid(True)

# 3. Función seno
axs[2].plot(t, np.sin(t), color='purple')
axs[2].set_title('Función seno')
axs[2].set_xlabel('t')
axs[2].set_ylabel('sin(t)')
axs[2].grid(True)

plt.tight_layout()
plt.show()
```
