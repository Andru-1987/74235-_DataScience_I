[Material Diapositivas](https://docs.google.com/presentation/d/14g5eAuGgTasx_D4dJ7w7txt2qOZEY7EqvrTVTMddh74/edit#slide=id.p44)

## 🧠 ¿Qué es el Clustering?

El **clustering** es una técnica de aprendizaje no supervisado que agrupa objetos similares dentro de un mismo grupo (o clúster), separándolos de objetos diferentes que pertenecen a otros grupos. Es ampliamente utilizado para segmentación de clientes, análisis de imágenes, detección de patrones y más.

---

## 🧩 Principales enfoques de Clustering y sus características

### 1. 🔹 Particiones

Divide los datos en *k* grupos predefinidos maximizando la similitud dentro de los clústeres y minimizando la similitud entre ellos.

* **K-means**: Asigna puntos al centroide más cercano; requiere definir *k*.
* **PAM**: Usa *medoides* (puntos reales) en lugar de centroides.
* **CLARA**: Versión optimizada de PAM para grandes volúmenes.
* **FCM**: Clustering difuso; un punto puede pertenecer parcialmente a varios clústeres.

👉 *Ventajas:* Simple y rápido.
👉 *Desventajas:* Sensible a la inicialización y a la forma de los clústeres.

---

### 2. 🔹 Jerárquico

Crea una estructura tipo árbol (dendrograma) que refleja cómo se agrupan los datos paso a paso.

* **Aglomerativo**: Funde clústeres de abajo hacia arriba.
* **Divisivo**: Divide de arriba hacia abajo.
* **BIRCH**: Usa árboles para resumir datos y facilitar el clustering.
* **ROCK**: Usa conexiones entre vecinos para agrupar datos categóricos.
* **CURE**: Usa puntos representativos para detectar clústeres no esféricos.

👉 *Ventajas:* No necesita predefinir *k*.
👉 *Desventajas:* Costoso computacionalmente.

---

### 3. 🔹 Densidad

Agrupa puntos que están densamente conectados entre sí.

* **DBSCAN**: Forma clústeres basados en regiones densas; detecta outliers.
* **OPTICS**: Variante de DBSCAN que maneja variaciones de densidad.
* **DBCLASD**: Detecta estructuras arbitrarias de clústeres.
* **DENCLUE**: Usa funciones de densidad para modelar la distribución de puntos.

👉 *Ventajas:* Detecta clústeres de forma arbitraria, maneja ruido.
👉 *Desventajas:* Difícil elegir parámetros óptimos.

---

### 4. 🔹 Basado en Grid

Divide el espacio en celdas y agrupa según densidad local en cada celda.

* **Wavecluster**: Usa transformación de onda para agrupar.
* **STING**: Usa una estructura jerárquica basada en grillas estadísticas.
* **CLIQUE**: Apto para datos de alta dimensión.
* **OptiGrid**: Variante optimizada de grilla para clusters complejos.

👉 *Ventajas:* Eficiente en altas dimensiones.
👉 *Desventajas:* Sensible al tamaño de grilla.

---

### 5. 🔹 Basado en Modelos

Asume que los datos se generan a partir de un modelo estadístico.

* **GMM (Gaussian Mixture Model)**: Supone que los datos provienen de varias distribuciones normales.
* **COBWEB**: Crea un árbol jerárquico categórico en línea.
* **CLASSIT**: Similar a COBWEB, incorpora componentes probabilísticos.
* **SOMs (Self-Organizing Maps)**: Red neuronal que mapea datos a una grilla de baja dimensión.

👉 *Ventajas:* Modelos probabilísticos flexibles.
👉 *Desventajas:* Requiere supuestos sobre la distribución de datos.

