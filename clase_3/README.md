# 🧪 Clase: Introducción a NumPy y Pandas

[Presentacion](https://docs.google.com/presentation/d/135XQdDjAvsoXtqDWhASGQ8-YWBFS5bDgxyJjfycykYs/edit?slide=id.g2204e13b0d5_2_631#slide=id.g2204e13b0d5_2_631)

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
[Video sobre Numpy](https://www.youtube.com/watch?v=cYm3DBG6KfI&t=16s)
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

# 📝 Actividad práctica 

## Actividad Práctica: NumPy y Pandas en Python

## 1. NumPy: Manipulación de Arrays

**Creación de arrays básicos:**

```python
import numpy as np

# Crear un array simple
array_simple = np.array([1, 2, 3, 4, 5])
print("Array simple:", array_simple)

# Crear una matriz 2D
matriz_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Matriz 2D:\n", matriz_2d)

# Crear arrays con valores específicos
zeros = np.zeros((3, 3))
ones = np.ones((2, 4))
print("Array de ceros:\n", zeros)
print("Array de unos:\n", ones)
```

**Operaciones matemáticas con arrays:**

```python
# Operaciones aritméticas básicas
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Suma:", a + b)  # o np.add(a, b)
print("Resta:", a - b)  # o np.subtract(a, b)
print("Multiplicación:", a * b)  # o np.multiply(a, b)
print("División:", a / b)  # o np.divide(a, b)
print("Exponenciación:", a ** 2)  # o np.power(a, 2)

# Operaciones estadísticas
print("Suma de elementos:", np.sum(a))
print("Media:", np.mean(a))
print("Desviación estándar:", np.std(a))
```

## 2. Pandas como Herramienta de Analítica

### Series en Pandas

```python
import pandas as pd

# Crear una Serie desde una lista
serie_lista = pd.Series([10, 20, 30, 40])
print("Serie desde lista:\n", serie_lista)

# Crear una Serie desde un diccionario
datos_diccionario = {"día1": 420, "día2": 380, "día3": 390}
serie_dict = pd.Series(datos_diccionario)
print("Serie desde diccionario:\n", serie_dict)

# Selección específica con índice
serie_filtrada = pd.Series(datos_diccionario, index=["día1", "día2"])
print("Serie filtrada:\n", serie_filtrada)
```

### DataFrames en Pandas

```python
# Crear DataFrame desde diccionario
datos = {
    "Nombre": ["Juan", "María", "Pedro"],
    "Edad": [30, 25, 40],
    "Ciudad": ["Caracas", "Maracaibo", "Valencia"]
}
df = pd.DataFrame(datos)
print("DataFrame desde diccionario:\n", df)

# Acceder a datos del DataFrame
print("\nColumna de nombres:\n", df["Nombre"])
print("\nPrimeras filas:\n", df.head(2))
print("\nInformación del DataFrame:\n", df.info())
print("\nEstadísticas descriptivas:\n", df.describe())
```

### Operaciones Básicas con DataFrames

```python
# Filtrado de datos
mayores_30 = df[df["Edad"] > 30]
print("Personas mayores de 30:\n", mayores_30)

# Añadir nueva columna
df["Activo"] = [True, False, True]
print("\nDataFrame con nueva columna:\n", df)

# Operaciones en columnas
df["Edad_en_meses"] = df["Edad"] * 12
print("\nEdad en meses:\n", df)

# Agrupar y resumir datos
promedio_edad_por_ciudad = df.groupby("Ciudad")["Edad"].mean()
print("\nPromedio de edad por ciudad:\n", promedio_edad_por_ciudad)
```

## 3. Métodos de Lectura de Archivos con Pandas

### Lectura de archivos CSV

```python
# Leer archivo CSV local
# df_csv = pd.read_csv('datos.csv')

# Leer CSV desde URL
url_csv = 'https://raw.githubusercontent.com/JJTorresDS/stocks-ds-edu/main/stocks.csv'
df_stocks = pd.read_csv(url_csv)
print("Primeras filas del CSV:\n", df_stocks.head())

# Opciones de lectura CSV
df_csv_options = pd.read_csv(url_csv, 
                            # skiprows=1,         # Saltar filas
                            # usecols=['MSFT', 'AMZN'],  # Seleccionar columnas
                            index_col='formatted_date',  # Establecer columna como índice
                            parse_dates=['formatted_date'])  # Parsear fechas
print("\nCSV con opciones de lectura:\n", df_csv_options.head())
```

### Lectura de archivos JSON

```python
# Leer archivo JSON (ejemplo)
# Comentado para no generar errores si no existe el archivo
"""
url_json = 'https://raw.githubusercontent.com/tu_usuario/tu_repo/main/datos.json'
df_json = pd.read_json(url_json)
print("Datos del JSON:\n", df_json.head())

# Leer JSON con líneas múltiples
df_json_lines = pd.read_json(url_json, lines=True)
print("\nJSON con múltiples líneas:\n", df_json_lines.head())
"""
```

### Otros formatos de lectura

```python
# Leer Excel (comentado para evitar errores)
# df_excel = pd.read_excel('datos.xlsx', sheet_name='Hoja1')

# Leer SQL (ejemplo conceptual)
"""
from sqlalchemy import create_engine
engine = create_engine('sqlite:///mi_base.db')
df_sql = pd.read_sql('SELECT * FROM mi_tabla', con=engine)
"""

# Ejemplos de escritura de datos
df.to_csv('mi_dataframe.csv', index=False)
# df.to_excel('mi_dataframe.xlsx', index=False)
# df.to_json('mi_dataframe.json', orient='records')
```

## Ejercicio Práctico

Para consolidar los conocimientos adquiridos, se propone el siguiente ejercicio:

1. Cargar el archivo de stocks desde GitHub
2. Calcular el rendimiento promedio mensual de cada acción
3. Identificar la acción con mayor volatilidad
4. Crear un gráfico que muestre la evolución de las 3 acciones con mejor rendimiento

```python
# Solución parcial del ejercicio
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos
url = 'https://raw.githubusercontent.com/JJTorresDS/stocks-ds-edu/main/stocks.csv'
stocks_df = pd.read_csv(url)
stocks_df['formatted_date'] = pd.to_datetime(stocks_df['formatted_date'])

# Establecer la fecha como índice
stocks_df = stocks_df.set_index('formatted_date')

# Las primeras filas del dataset
print(stocks_df.head())
```