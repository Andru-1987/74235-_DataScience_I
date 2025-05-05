## 📘 Clase: Fundamentos de Data Science en la Transformación Digital e Industria 4.0

### 🎯 Objetivos de la clase

1. Identificar los componentes importantes de una estrategia de Data Science.
2. Comprender el rol de los datos en la organización desde una perspectiva de Transformación Digital y en la Industria 4.0.
3. Facilitar la identificación de oportunidades del uso de los datos para la transformación digital y la estrategia de negocios.
4. Clasificar las principales herramientas para un Científico de Datos y sus características.

---

## 1️⃣ ¿Qué es una estrategia de Data Science?

Una estrategia de Data Science busca extraer valor de grandes volúmenes de datos mediante técnicas estadísticas, aprendizaje automático e inteligencia artificial. Es clave para la automatización y optimización de decisiones complejas.

### Componentes clave:

* **Adquisición de datos**: Recopilación estructurada (bases SQL) y no estructurada (texto, imágenes, sensores).
* **Limpieza y procesamiento**: Eliminación de ruido y preparación para análisis (ETL, pipelines).
* **Modelado predictivo**: Uso de machine learning y estadística para hacer predicciones o clasificaciones.
* **Despliegue de modelos**: Implementación en producción (APIs, automatización).
* **Evaluación continua**: Revisión de performance del modelo y actualización constante.

---

## 2️⃣ Rol de los datos en la Transformación Digital e Industria 4.0

### Transformación Digital

* Automatización de decisiones con algoritmos.
* Personalización con modelos de recomendación.
* Procesamiento masivo en tiempo real.

### Industria 4.0

* IoT + Data Science → mantenimiento predictivo.
* Visión artificial en control de calidad.
* Robótica inteligente con entrenamiento supervisado.

Ejemplo:

> Un modelo de predicción de fallas en sensores industriales puede prevenir paradas costosas.

---

## 3️⃣ ¿Cómo detectar oportunidades de aplicación de Data Science?

Preguntas guía:

* ¿Qué procesos generan muchos datos y tienen margen de mejora?
* ¿Dónde hay patrones ocultos que podríamos detectar?
* ¿Qué tareas repetitivas pueden ser automatizadas con modelos?

Ejemplo práctico:

> Un banco puede usar clasificación automática de riesgo crediticio para acelerar aprobaciones.

---

## 4️⃣ Herramientas clave para el Científico de Datos

| Herramienta                 | Propósito                                 | Características                                       |
| --------------------------- | ----------------------------------------- | ----------------------------------------------------- |
| **Python**                  | Principal lenguaje                        | Bibliotecas como NumPy, Pandas, Scikit-learn, PyTorch |
| **Jupyter Notebooks**       | Experimentación y documentación           | Ideal para prototipos y enseñanza                     |
| **Git & GitHub**            | Control de versiones                      | Buenas prácticas colaborativas                        |
| **Docker**                  | Contenerización de modelos                | Facilita despliegue reproducible                      |
| **Cloud (AWS, GCP, Azure)** | Escalabilidad y entrenamiento distribuido | Uso de notebooks, AutoML y pipelines                  |
| **MLflow / DVC**            | Gestión del ciclo de vida de modelos      | Seguimiento de experimentos y datasets                |

---

## 📚 Bibliografía recomendada

1. **Joel Grus (2019)** – *Data Science from Scratch*. O’Reilly.
2. **Aurélien Géron (2019)** – *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow*.
3. **Sebastian Raschka (2022)** – *Python Machine Learning*.
4. Cursos recomendados:

   * [IBM Data Science Professional Certificate – Coursera](https://www.coursera.org/professional-certificates/ibm-data-science)
   * [Google Advanced Data Science – edX](https://www.edx.org/)

---

En Machine Learning (ML), los algoritmos se clasifican principalmente en **supervisados** y **no supervisados** según el tipo de datos con los que trabajan y el objetivo del aprendizaje.

---

## 🧠 Aprendizaje Supervisado

**Definición**: Se entrena el modelo con un conjunto de datos etiquetado, es decir, se conoce la **respuesta correcta** (o *output*) para cada entrada (*input*). El objetivo es que el modelo aprenda una función que relacione entradas con salidas.

### Casos típicos:

* **Clasificación**: Predecir una categoría.

  * Ejemplo: ¿Este email es spam o no?
* **Regresión**: Predecir un valor numérico.

  * Ejemplo: ¿Cuál será el precio de una casa?

### Algoritmos comunes:

| Tipo                      | Algoritmo                             | Ejemplo práctico             |
| ------------------------- | ------------------------------------- | ---------------------------- |
| Clasificación             | Árboles de decisión                   | Diagnóstico médico           |
| Clasificación             | K-Nearest Neighbors (KNN)             | Recomendaciones de productos |
| Clasificación             | Support Vector Machines (SVM)         | Detección de fraude          |
| Clasificación / Regresión | Random Forest                         | Predicción de ventas         |
| Clasificación / Regresión | Gradient Boosting (XGBoost, LightGBM) | Marketing predictivo         |
| Regresión                 | Regresión lineal                      | Predicción de ingresos       |
| Regresión                 | Regresión polinómica                  | Modelado de trayectorias     |

---

## 🧠 Aprendizaje No Supervisado

**Definición**: Se trabaja con datos **no etiquetados**, es decir, no se conoce el resultado esperado. El modelo busca **estructuras, patrones o agrupamientos** dentro de los datos.

### Casos típicos:

* **Clustering**: Agrupar datos similares.

  * Ejemplo: Segmentar clientes según comportamiento.
* **Reducción de dimensionalidad**: Simplificar datos con muchas variables.

  * Ejemplo: Visualizar datos complejos en 2D.
* **Detección de anomalías**: Identificar datos fuera de lo común.

  * Ejemplo: Detectar fraudes bancarios.

### Algoritmos comunes:

| Tipo                     | Algoritmo                                 | Ejemplo práctico                    |
| ------------------------ | ----------------------------------------- | ----------------------------------- |
| Clustering               | K-Means                                   | Segmentación de clientes            |
| Clustering               | DBSCAN                                    | Agrupación con densidades variables |
| Reducción de dimensiones | PCA (Análisis de Componentes Principales) | Visualización de datos              |
| Reducción / Detección    | t-SNE, UMAP                               | Exploración de datos complejos      |
| Anomalías                | Isolation Forest                          | Monitoreo de sistemas en producción |


