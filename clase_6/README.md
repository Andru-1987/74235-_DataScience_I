# Inicio -> tipos de variables
### 🧠 1. **Según su naturaleza:**

#### a. **Cuantitativas (Numéricas)**

* Representan cantidades o valores numéricos.
* Se subdividen en:

##### 🔹 *Continuas*

* Pueden tomar **infinitos valores dentro de un rango**.
* Se miden, no se cuentan.
* **Ejemplos**:

  * Altura (1.75 m, 1.76 m, etc.)
  * Peso (65.5 kg, 66.2 kg)
  * Tiempo (2.5 horas)

##### 🔹 *Discretas*

* Solo pueden tomar **valores enteros o finitos**.
* Se cuentan.
* **Ejemplos**:

  * Número de hijos (0, 1, 2…)
  * Número de autos en una familia
  * Cantidad de errores en una prueba

---

#### b. **Cualitativas (Categoricas)**

* Representan **categorías o cualidades**.
* No implican operaciones matemáticas.

##### 🔹 *Nominales*

* No tienen orden lógico.
* **Ejemplos**:

  * Color de ojos (azul, verde, marrón)
  * Género (masculino, femenino, otro)
  * Nacionalidad (argentina, chilena)

##### 🔹 *Ordinales*

* Tienen **orden o jerarquía**, pero no hay distancia precisa entre categorías.
* **Ejemplos**:

  * Nivel educativo (primario, secundario, universitario)
  * Grado de satisfacción (bajo, medio, alto)
  * Rango militar (soldado, cabo, sargento)

---

### 🔁 2. **Según su variabilidad:**

#### 🔹 *Dependientes*

* Son afectadas por otras variables.
* **Ejemplo**: La presión arterial depende del nivel de actividad física.

#### 🔹 *Independientes*

* Se manipulan para ver su efecto.
* **Ejemplo**: Horas de estudio como variable que afecta al rendimiento académico.

---

### 📊 3. **Otras clasificaciones útiles:**

#### 🔹 *Binarias o dicotómicas*

* Solo tienen **dos categorías posibles**.
* **Ejemplo**: Sí / No, Aprobado / Reprobado

#### 🔹 *Polinómicas*

* Tienen más de dos categorías.
* **Ejemplo**: Tipo de sangre (A, B, AB, O)
---
Las **series temporales** son un tipo especial de conjunto de datos en el que **las observaciones están ordenadas en el tiempo**. Se utilizan para analizar y predecir cómo cambian los valores de una variable a lo largo del tiempo.

---


## Consideracion de otras variables sobre Temporalidades

### 🕒 ¿Qué es una serie temporal?

Una **serie temporal** es una **secuencia de datos** registrados a lo largo del tiempo, **en intervalos regulares** (diarios, mensuales, anuales, etc.).

* **Ejemplos**:

  * Temperatura diaria de una ciudad
  * Precio del dólar por mes
  * Ventas de una empresa por trimestre
  * Cantidad de pasajeros por hora en un subte

---

### 🧩 Cualidades distintivas de las series temporales:

1. ### 📐 **Secuencialidad**

   * El orden cronológico **es fundamental**.
   * A diferencia de otros conjuntos de datos, **reordenar los datos rompe la estructura** de la serie.

2. ### 🔁 **Dependencia temporal**

   * Los valores sucesivos están **relacionados entre sí**.
   * El valor en el tiempo `t` suele depender del valor en `t-1`, `t-2`, etc.
   * Esto permite usar modelos que capturan esa dependencia, como **ARIMA, LSTM, Prophet**, etc.

3. ### ⏳ **Estructura del tiempo**

   * El tiempo tiene **características particulares** que afectan los datos:

     * **Estacionalidad**: patrones que se repiten en intervalos regulares (ej. más helado en verano).
     * **Tendencia**: crecimiento o disminución a lo largo del tiempo.
     * **Ciclos**: fluctuaciones más irregulares que pueden durar años (ej. economía).
     * **Eventos especiales**: feriados, años bisiestos, pandemias, etc.
     * **Cambio de estaciones del año**: especialmente relevante en fenómenos naturales o de consumo.

4. ### 📏 **Frecuencia**

   * Puede ser **horaria, diaria, semanal, mensual, trimestral, anual**, etc.
   * La elección de la frecuencia afecta el tipo de análisis (por ejemplo, análisis de estacionalidad mensual vs diaria).

---

### 🎯 Aplicaciones típicas:

* Predicción de ventas o demanda
* Análisis financiero (acciones, divisas)
* Meteorología
* Series biomédicas (ritmo cardíaco, glucosa)
* Sensores IoT (temperatura, vibraciones)

---

### 📘 **Resumen General: Medidas de Resumen y Distribuciones**

Las medidas de resumen se dividen en dos grandes grupos:

1. **Cuantitativas** (valores numéricos):

   * **Media**: Promedio aritmético, sensible a valores extremos.
   * **Mediana**: Valor central, resistente a outliers.
   * **Moda**: Valor más frecuente.
   * **Varianza**: Mide cuán dispersos están los datos respecto a la media.
   * **Desviación estándar**: Dispersión en las mismas unidades que los datos.
   * **Cuartiles y percentiles**: Dividen el conjunto de datos en segmentos para analizar la distribución.

2. **Cualitativas** (valores categóricos):

   * **Conteo de observaciones**: Frecuencia de cada categoría.
   * **Moda**: Categoría más frecuente.

También se analizan **distribuciones**:

* **Distribución uniforme**: Todos los valores tienen igual probabilidad.
* **Distribución normal**: Forma de campana, simétrica, con mayor densidad de datos en torno a la media.

Y se interpretan gráficamente mediante:

* **Histogramas**: Muestran frecuencias por intervalos.
* **Correlación lineal**: Mide fuerza y dirección de la relación entre dos variables (coeficiente de correlación de −1 a 1).

---

### 📊 **Tabla Resumen: Medidas y Distribuciones**

| **Concepto**                | **Tipo de Variable**     | **Descripción**                                                   | **Ventajas**                               | **Limitaciones**                                      |
| --------------------------- | ------------------------ | ----------------------------------------------------------------- | ------------------------------------------ | ----------------------------------------------------- |
| **Media**                   | Cuantitativa             | Promedio de todos los valores                                     | Fácil de calcular e interpretar            | Afectada por valores extremos (outliers)              |
| **Mediana**                 | Cuantitativa             | Valor central de los datos ordenados                              | Robusta frente a outliers                  | No refleja toda la información del conjunto           |
| **Moda**                    | Cualitativa/Cuantitativa | Valor o categoría más frecuente                                   | Intuitiva y útil en cualitativas           | Puede haber más de una o ninguna moda                 |
| **Varianza**                | Cuantitativa             | Promedio de los cuadrados de las desviaciones respecto a la media | Evalúa dispersión con detalle              | Difícil interpretación directa (unidades al cuadrado) |
| **Desviación estándar**     | Cuantitativa             | Raíz cuadrada de la varianza                                      | Más intuitiva que la varianza              | Sensible a valores extremos                           |
| **Cuartiles / Percentiles** | Cuantitativa             | Dividen los datos ordenados en partes iguales                     | Permiten comparar posiciones relativas     | No indican dispersión general completa                |
| **Conteo de observaciones** | Cualitativa              | Número de veces que aparece cada categoría                        | Simple y clara                             | No indica relación entre categorías                   |
| **Distribución uniforme**   | Cualitativa/Cuantitativa | Todos los valores tienen igual probabilidad                       | Ideal para procesos aleatorios controlados | Poco realista en fenómenos naturales                  |
| **Distribución normal**     | Cuantitativa             | Datos concentrados alrededor de la media con forma de campana     | Base de muchos métodos estadísticos        | No todos los fenómenos la siguen                      |
| **Histograma**              | Cualitativa/Cuantitativa | Representa frecuencias por intervalos                             | Visualiza forma de la distribución         | Depende del número de intervalos                      |
| **Correlación lineal**      | Cuantitativa             | Relación entre dos variables (de −1 a 1)                          | Detecta patrones lineales                  | No implica causalidad                                 |

---

### RESPUESTA DE LA FILMINA pag.8 

**índice trimestral de inflación se considera una serie de tiempo**?

### ¿Por qué?

Una **serie de tiempo** es un conjunto de observaciones recogidas **en momentos sucesivos del tiempo**, generalmente a intervalos regulares (diarios, mensuales, trimestrales, etc.). El **índice trimestral de inflación** cumple con estas características:

* **Observaciones ordenadas en el tiempo:** cada dato representa la inflación de un trimestre específico (por ejemplo, Q1 2022, Q2 2022, etc.).
* **Intervalos regulares:** los datos se recopilan **cada tres meses**, lo que constituye un intervalo de tiempo constante.
* **Análisis temporal posible:** se puede analizar su tendencia, estacionalidad, ciclos económicos y variabilidad a lo largo del tiempo.

### En pocas palabras:

✅ **Sí, el índice trimestral de inflación es una serie de tiempo**, y puede ser analizado mediante métodos estadísticos y econométricos propios del análisis de series temporales.
