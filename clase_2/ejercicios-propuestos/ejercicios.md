# 📉 Análisis de Retrocesos en el Valor de la Acción - Compañía X

Se cuenta con una lista de valores promedio diarios del precio de la acción de la compañía **X** durante la semana pasada. Cada valor representa un día de la semana:

```python
valores = [200, 225, 232, 221, 243, 256, 255]
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
````

---

## 🎯 Objetivo

Identificar los días en los que **hubo un retroceso** (una baja) en el valor de la acción respecto al día anterior.

---

## 🧪 Código de Ejemplo

A continuación se presenta una solución utilizando Python y NumPy:

```python
import numpy as np

valores = [200, 225, 232, 221, 243, 256, 255]
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

# Calcular la diferencia entre valores consecutivos
diferencias = np.diff(valores)

# Detectar retrocesos en los valores
for i, cambio in enumerate(diferencias, start=1):
    if cambio < 0:
        print(f"🔻 Hubo un retroceso el día {dias[i]} (valor: {valores[i]} vs día anterior: {valores[i-1]})")
```

📌 Este código compara el valor de cada día con el anterior y reporta si hubo una disminución.

---

# 📊 Actividad: Análisis Estadístico de Acciones con Pandas

En esta actividad trabajaremos con un conjunto de datos que contiene los precios de diferentes acciones a lo largo del tiempo. Usaremos **Python** y la librería **Pandas** para realizar el análisis.

---

## 🔍 Consigna 1

✅ Utilizando un ciclo (`for` o `while`), obtené las siguientes métricas para **cada columna del DataFrame** (cada acción):

* Media (promedio)
* Desviación estándar
* Varianza

📌 *Sugerencia:* Podés utilizar las funciones:

```python
.mean(), .std(), .var()
```

---

## 🔍 Consigna 2

✅ Crear una función que recorra cada columna del DataFrame e identifique:

* El valor **máximo**
* El valor **mínimo**

📌 *Sugerencia:* Usá:

```python
.min(), .max()
```

---

## 💡 Tip Extra

Asegurate de importar Pandas correctamente y de tener tu dataset cargado:

```python

#Crear un archivo de prueba
import pandas as pd
df = pd.read_csv("acciones.csv")  # Reemplazá con el nombre real de tu archivo
```

