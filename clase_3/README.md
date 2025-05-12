# 🧪 Clase: Introducción a NumPy y Pandas


## 🎯 Objetivos de la clase

- Comprender la importancia de usar bibliotecas optimizadas como **NumPy** y **Pandas** en proyectos de ciencia de datos.
- Manipular estructuras de datos con **NumPy**: arrays, operaciones vectorizadas, álgebra lineal.
- Explorar los componentes fundamentales de **Pandas**: Series y DataFrames.
- Aplicar técnicas de indexación, selección y transformación de datos reales.

---

## 📌 ¿Por qué es importante NumPy?

En ciencia de datos, trabajamos con **grandes volúmenes de datos numéricos**. Las listas de Python funcionan bien, pero no están optimizadas para cálculos científicos.

**NumPy**:
- Permite realizar **operaciones vectorizadas** (sin bucles explícitos).
- Ofrece estructuras de datos eficientes como `ndarray` (arrays multidimensionales).
- Integra funciones de **álgebra lineal**, estadísticas y manipulación matemática.

✅ Usar NumPy puede significar mejoras de **10x a 100x en performance** comparado con listas nativas de Python.

---

## 📚 Parte 1: NumPy

### ✳️ Importación de la librería

```python
import numpy as np
````

### 🔢 Ejercicio 1: Crear vectores

```python
# Crear un vector desde una lista
v = np.array([1, 2, 3, 4])
print(v)
```

### 🔁 Ejercicio 2: Operaciones vectorizadas

```python
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

# Suma elemento a elemento
print(a + b)

# Multiplicación escalar
print(a * 2)

# Potencia
print(b ** 2)
```

### 🧮 Ejercicio 3: Matrices y álgebra lineal

```python
# Matriz 2x2
A = np.array([[1, 2], [3, 4]])

# Transpuesta
print(A.T)

# Inversa
print(np.linalg.inv(A))

# Producto matricial
B = np.array([[5, 6], [7, 8]])
print(np.dot(A, B))
```

---

## 📚 Parte 2: Pandas

### ✳️ ¿Qué es Pandas?

Pandas es la **librería base para manipular datos en forma tabular** en Python. Provee dos estructuras fundamentales:

* `Series`: vector unidimensional con índice.
* `DataFrame`: tabla bidimensional con columnas e índices.

```python
import pandas as pd
```

---

### 📊 Ejercicio 1: Crear Series

```python
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)
```

### 📊 Ejercicio 2: Crear DataFrames

```python
data = {
    'nombre': ['Ana', 'Luis', 'Juan'],
    'edad': [23, 35, 29],
    'ciudad': ['Córdoba', 'Buenos Aires', 'Rosario']
}

df = pd.DataFrame(data)
print(df)
```

---

### 🔍 Ejercicio 3: Selección e indexación

```python
# Seleccionar columna
print(df['edad'])

# Filtrar por condición
print(df[df['edad'] > 30])

# Acceder por etiqueta o posición
print(df.loc[1])   # Fila con índice 1
print(df.iloc[0])  # Primera fila
```

---

## 💬 Discusión guiada

* ¿Cuáles son las ventajas prácticas de usar NumPy frente a listas?
* ¿Por qué Pandas es más útil que un diccionario de listas?
* ¿Qué errores comunes hay al manipular DataFrames?

---

## 📝 Actividad práctica final

1. Crear un array de 100 números aleatorios entre 0 y 10.
2. Calcular la media, la desviación estándar y el valor máximo.
3. Crear un DataFrame con información ficticia de 5 personas: nombre, edad, altura.
4. Filtrar a quienes tienen más de 25 años y altura mayor a 1.70.

---

## ✅ Cierre

NumPy y Pandas son **pilares fundamentales** de cualquier flujo de trabajo en ciencia de datos. Entender su lógica y sintaxis es clave para trabajar con datos reales, modelado estadístico, visualizaciones y machine learning.
