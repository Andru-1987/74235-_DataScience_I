### **¿Qué es Machine Learning?**  
**Machine Learning (ML)** o *Aprendizaje Automático* es una rama de la **Inteligencia Artificial (IA)** que se centra en desarrollar algoritmos y modelos capaces de aprender patrones a partir de datos, **sin ser programados explícitamente**. En lugar de seguir reglas predefinidas, los sistemas de ML **mejoran su desempeño con la experiencia** (datos).  

Su objetivo principal es **generalizar** a partir de ejemplos para realizar predicciones o tomar decisiones en situaciones nuevas.

---

### **Particularidades y Características Principales**  

1. **Aprendizaje basado en datos**  
   - ML requiere **datos históricos o de entrenamiento** para identificar patrones y relaciones.  
   - A diferencia de la programación tradicional (donde las reglas son fijas), en ML **el modelo "aprende" de los datos**.  

2. **Capacidad predictiva y adaptativa**  
   - Los modelos de ML pueden **predecir resultados futuros** (ej.: ventas, fallos en equipos) o **clasificar información** (ej.: spam/no spam).  
   - Algunos sistemas se adaptan a cambios en los datos (ej.: recomendaciones en tiempo real en Netflix o Amazon).  

3. **Tipos principales de aprendizaje**  
   - **Supervisado**: Usa datos etiquetados (ej.: predecir precios de casas basado en ejemplos pasados).  
   - **No supervisado**: Encuentra patrones en datos sin etiquetas (ej.: agrupación de clientes por comportamiento).  
   - **Por refuerzo**: Aprende mediante prueba/error y recompensas (ej.: robots que aprenden a caminar).  

4. **Automatización y escalabilidad**  
   - ML permite automatizar tareas complejas (ej.: diagnóstico médico, detección de fraudes).  
   - Escala bien con grandes volúmenes de datos (*Big Data*).  

5. **Énfasis en la evaluación**  
   - Los modelos se validan con métricas como **precisión, recall o error cuadrático medio** para garantizar su fiabilidad.  

6. **Dependencia de la calidad de los datos**  
   - El rendimiento del ML está ligado a la **calidad, cantidad y representatividad** de los datos.  
   - Problemas como *sesgos* o *datos incompletos* afectan los resultados.  

7. **Uso de algoritmos diversos**  
   - Desde métodos clásicos (*regresión lineal, árboles de decisión*) hasta técnicas avanzadas (*redes neuronales, deep learning*).  

---

### **Diferencia clave con Data Science**  
Mientras **Data Science** abarca todo el ciclo de análisis de datos (limpieza, visualización, estadística, etc.), **ML es una herramienta dentro de DS** enfocada específicamente en **automatizar el aprendizaje** para predicción o toma de decisiones.  

**Ejemplo práctico**:  
- Un modelo de ML podría predecir el *churn* (abandono) de clientes en una empresa, mientras que un data scientist también analizaría *por qué* ocurre y cómo comunicarlo.  

En resumen, **Machine Learning es la tecnología que permite a las máquinas "aprender" de los datos para resolver problemas complejos de manera autónoma o semiautónoma**. 

---


### _Si quisiéramos resolver un problema donde tenemos información georeferenciada de clientes ¿cómo podríamos utilizar el ML para incrementar las ventas de un producto?_

Para incrementar las ventas de un producto utilizando **Machine Learning (ML)** con datos georreferenciados de clientes, puedes aplicar diversas estrategias basadas en análisis espacial y modelos predictivos. Aquí te detallo un enfoque estructurado:

---

### **1. Análisis Exploratorio de Datos (EDA) Geoespacial**  
- **Visualización de datos**:  
  - Usar mapas de calor (*heatmaps*) para identificar zonas con alta concentración de clientes o ventas.  
  - Segmentar por zonas geográficas (barrios, ciudades, códigos postales).  
- **Detección de patrones**:  
  - Correlacionar ubicación con variables como ingresos, edad, clima o proximidad a puntos de interés (ej.: centros comerciales).  

**Herramientas**: Python (`geopandas`, `folium`), Power BI (integrado con Mapas).  

---

### **2. Segmentación de Clientes por Ubicación**  
- **Clustering no supervisado** (ej.: *K-means* o *DBSCAN*) para agrupar clientes con características similares:  
  - Crear clusters basados en:  
    - Ubicación (coordenadas).  
    - Comportamiento de compra + datos demográficos locales.  
  - Ejemplo: Identificar "zonas de alto potencial" con clientes similares a los que ya compran el producto.  

---

### **3. Modelos Predictivos para Ventas**  
- **Aprendizaje supervisado** (ej.: *Random Forest, XGBoost*) para predecir:  
  - **Propensión de compra**: Qué clientes (o zonas) tienen mayor probabilidad de comprar el producto.  
  - **Demanda geográfica**: Dónde habrá mayor demanda en función de variables temporales (ej.: festividades locales).  
- **Variables de entrada**:  
  - Datos geográficos (latitud, longitud, distancia a tiendas).  
  - Datos socioeconómicos de la zona (nivel de ingresos, densidad poblacional).  
  - Historial de ventas en la región.  

---

### **4. Recomendaciones Geo-Personalizadas**  
- **Sistemas de recomendación** con filtrado colaborativo o basado en contenido:  
  - Sugerir productos populares en la zona (ej.: "En tu barrio, otros clientes compran X").  
  - Adaptar promociones según el perfil geográfico (ej.: descuentos en zonas con menor penetración).  

---

### **5. Optimización Logística y Ubicación de Puntos de Venta**  
- **Modelos de ubicación óptima**:  
  - Usar *algoritmos de optimización* (ej.: *p-median*) para decidir dónde abrir nuevas tiendas o colocar anuncios.  
  - Ejemplo: "Las zonas con radio de 5 km sin cobertura tienen un 20% de clientes potenciales sin atender".  

---

### **6. Campañas de Marketing Dirigido**  
- **Geo-targeting publicitario**:  
  - Entrenar modelos para identificar zonas donde campañas específicas (ej.: SMS, redes sociales) tendrán mayor ROI.  
  - Ejemplo: Anuncios en Facebook Ads para un radio de 10 km alrededor de tiendas con stock alto.  

---

### **7. Ejemplo Práctico**  
**Problema**: Una cadena de cafeterías quiere aumentar ventas en Ciudad de México.  
**Solución con ML**:  
1. Agrupa clientes por colonia usando *DBSCAN*.  
2. Entrena un modelo para predecir ventas según:  
   - Proximidad a estaciones de metro.  
   - Nivel socioeconómico (datos del INEGI).  
3. Descubre que las colonias *Roma* y *Condesa* tienen alta demanda los fines de semana.  
4. Lanza promociones "2x1" los sábados en esas zonas via WhatsApp.  

---

### **Beneficios**  
- **Reducción de costos**: Enfoque en zonas de alto impacto.  
- **Personalización**: Ofertas relevantes por ubicación.  
- **Escalabilidad**: Aplicable a múltiples regiones o productos.  

---
# ML

*  ## [Aprendizaje Supervizado](clase_7/aprendizaje-supervisado.md)
* ## [Aprendizaje no Supervisado](clase_7/aprendizaje-no-supervisado.md)

* ## [Paso a paso para un ML funcional](clase_7/paso-a-pas.md)


---
### Apartado especial para lo que es Feature Selection

### 🧹 1. Métodos de Filtro (*Filter Methods*)

Piensa en estos como un primer filtro rápido.

* **Cómo funcionan:** Evalúan cada característica de forma individual usando pruebas estadísticas que miden su relación con la variable objetivo (la etiqueta).
* **Velocidad:** Muy rápidos, ya que no requieren entrenar modelos.
* **Ejemplos:**

  * **Prueba de Chi-cuadrado** (para variables categóricas)
  * **Prueba ANOVA**
  * **Información mutua**
  * **Coeficiente de correlación**

📌 **Ventajas:** Rápidos y no dependen del modelo
📌 **Desventajas:** No consideran las interacciones entre características

---

### 🧪 2. Métodos Envolventes (*Wrapper Methods*)

Estos son como probar diferentes combinaciones de ropa para ver cuál te queda mejor.

* **Cómo funcionan:** Prueban múltiples subconjuntos de características entrenando modelos, y eligen el subconjunto que da el mejor rendimiento.
* **Velocidad:** Lentos, porque entrenan muchos modelos.
* **Ejemplos:**

  * **Eliminación recursiva de características (RFE)**
  * **Selección hacia adelante**
  * **Eliminación hacia atrás**

📌 **Ventajas:** Tienen en cuenta interacciones entre características
📌 **Desventajas:** Muy costosos en tiempo y recursos computacionales

---

### ⚙️ 3. Métodos Embebidos (*Embedded Methods*)

Estos seleccionan características **mientras entrenan** el modelo.

* **Cómo funcionan:** La selección ocurre como parte del proceso de entrenamiento.
* **Ejemplos:**

  * **Lasso (regularización L1)** – reduce coeficientes a cero
  * **Árboles de decisión / Bosques aleatorios** – calculan importancia de cada variable
  * **Elastic Net** – combina L1 y L2

📌 **Ventajas:** Más eficientes y consideran interacciones
📌 **Desventajas:** Dependientes del modelo utilizado

---

### Tabla Resumen:

| Tipo de método | ¿Usa modelo? | ¿Considera interacciones? | Velocidad | Ejemplos                      |
| -------------- | ------------ | ------------------------- | --------- | ----------------------------- |
| Filtro         | ❌ No         | ❌ No                      | 🚀 Rápido | Chi-cuadrado, correlación     |
| Envolvente     | ✅ Sí         | ✅ Sí                      | 🐢 Lento  | RFE, selección hacia adelante |
| Embebido       | ✅ Sí         | ✅ Sí                      | ⚡ Medio   | Lasso, árboles de decisión    |


## Recomendaciones para aprender:
¡Claro! Vamos a ver cada uno de estos métodos de selección de características supervisadas con **ejemplos, ventajas y desventajas**, relacionándolos con los tipos que ya vimos: filtro, envolvente o embebido.

---

### 📉 1. **Variance Threshold**

🔹 **Tipo:** Filtro
🔹 **Qué hace:** Elimina características con **baja varianza**, es decir, que no cambian mucho entre ejemplos (por ejemplo, una columna donde casi todos los valores son iguales).

#### ✅ Ventajas:

* Muy simple y rápido de aplicar
* No necesita etiquetas (también se puede usar en problemas no supervisados)

#### ❌ Desventajas:

* No considera la relación con la variable objetivo
* Puede eliminar características útiles si tienen poca varianza pero alta relevancia

#### 🧪 Ejemplo en Python:

```python
from sklearn.feature_selection import VarianceThreshold
selector = VarianceThreshold(threshold=0.01)
X_reduced = selector.fit_transform(X)
```

---

### ⭐ 2. **SelectKBest**

🔹 **Tipo:** Filtro
🔹 **Qué hace:** Selecciona las **k mejores características** según una métrica estadística que mide la relación con la variable objetivo (como ANOVA, chi-cuadrado, etc.).

#### ✅ Ventajas:

* Fácil de interpretar y aplicar
* Rápido y eficiente
* Permite usar distintas métricas

#### ❌ Desventajas:

* No considera interacciones entre variables
* Necesita que tú elijas el valor de *k* (el número de características a conservar)

#### 🧪 Ejemplo en Python:

```python
from sklearn.feature_selection import SelectKBest, f_classif
selector = SelectKBest(score_func=f_classif, k=10)
X_kbest = selector.fit_transform(X, y)
```

---

### 🔄 3. **RFE (Recursive Feature Elimination)**

🔹 **Tipo:** Envolvente
🔹 **Qué hace:** Usa un modelo (como una regresión o un SVM) para eliminar **recursivamente** las características menos importantes hasta quedarse con las más relevantes.

#### ✅ Ventajas:

* Considera interacciones entre variables
* Da muy buenos resultados si se elige bien el modelo base

#### ❌ Desventajas:

* Lento, especialmente con muchos datos o características
* Depende fuertemente del modelo usado

#### 🧪 Ejemplo en Python:

```python
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
rfe = RFE(estimator=model, n_features_to_select=5)
X_rfe = rfe.fit_transform(X, y)
```

---

### 🌳 4. **Boruta**

🔹 **Tipo:** Envolvente (basado en árboles, como Random Forest)
🔹 **Qué hace:** Crea versiones "aleatorias" de las características y las compara con las reales. Solo conserva las que son mejores que las versiones aleatorias (shadow features).

#### ✅ Ventajas:

* Muy robusto y preciso
* Tiene en cuenta interacciones y relaciones no lineales
* Funciona bien con datos complejos

#### ❌ Desventajas:

* Bastante lento (usa muchos modelos de Random Forest)
* No está en `scikit-learn` directamente (hay que usar una librería aparte como `boruta_py`)

#### 🧪 Ejemplo con `boruta_py`:

```python
from boruta import BorutaPy
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_jobs=-1, class_weight='balanced', max_depth=5)
boruta_selector = BorutaPy(estimator=model, n_estimators='auto', random_state=42)
boruta_selector.fit(X.values, y.values)
```

---

### 🔍 Resumen Comparativo

| Método             | Tipo       | Interacción | Velocidad    | Modelo requerido | Ventaja principal                    |
| ------------------ | ---------- | ----------- | ------------ | ---------------- | ------------------------------------ |
| Variance Threshold | Filtro     | ❌ No        | 🚀 Rápido    | ❌ No             | Muy simple y rápido                  |
| SelectKBest        | Filtro     | ❌ No        | 🚀 Rápido    | ❌ No             | Métricas estadísticas supervisadas   |
| RFE                | Envolvente | ✅ Sí        | 🐢 Lento     | ✅ Sí             | Preciso si el modelo es adecuado     |
| Boruta             | Envolvente | ✅ Sí        | 🐌 Muy lento | ✅ Sí             | Robusto frente a ruido y redundancia |

