### **Modelos de Aprendizaje No Supervisado: Clustering y Reducción de Dimensionalidad**  

Los modelos de **aprendizaje no supervisado** se utilizan cuando **no tenemos etiquetas** (datos sin respuestas conocidas). Su objetivo es **descubrir patrones ocultos**, estructuras o relaciones en los datos.  

Se dividen principalmente en dos categorías:  
1. **Clustering**: Agrupar datos similares.  
2. **Reducción de dimensionalidad**: Simplificar datos conservando su esencia.  

---

## **¿Por qué se llaman "no supervisados"?**  
Porque **no requieren datos etiquetados** para entrenar. El algoritmo trabaja con los datos "en crudo" y trata de encontrar **estructuras por sí mismo**.  

- **Ejemplo**:  
  - Si tienes datos de clientes sin categorías predefinidas, un algoritmo de clustering puede agruparlos en segmentos naturales (ej.: "clientes que compran de noche", "clientes ocasionales").  

---

## **1. Modelos de Clustering**  
**Objetivo**: Dividir datos en grupos (**clusters**) donde los elementos dentro de un grupo son similares entre sí y diferentes a los de otros grupos.  

### **Algoritmos comunes**  

| Modelo               | Idea Básica                                                                 | Ejemplo de Uso                     |  
|----------------------|-----------------------------------------------------------------------------|------------------------------------|  
| **K-Means**          | Divide los datos en *k* grupos basados en distancia al centroide (ej.: Euclidean). | Segmentación de clientes. |  
| **DBSCAN**           | Agrupa datos en zonas de alta densidad, dejando outliers fuera.            | Detección de fraudes atípicos.     |  
| **Hierarchical Clustering** | Crea un árbol de clusters (dendrograma) para elegir el nivel de agrupamiento. | Biología (clasificación de especies). |  
| **GMM (Gaussian Mixture Models)** | Asume que los datos vienen de una mezcla de distribuciones Gaussianas. | Reconocimiento de voz. |  

#### **Ejemplo en código (K-Means - Python)**  
```python
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Datos de ejemplo: X = features (ej.: ingreso vs. gasto anual)
kmeans = KMeans(n_clusters=3)  # Definir número de clusters
kmeans.fit(X)  # Entrenamiento SIN etiquetas
labels = kmeans.predict(X)  # Asignación de clusters: [0, 1, 2, 0...]

# Visualización
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.show()
```
**Salida**:  
![K-Means Clustering](https://miro.medium.com/max/1200/1*9hYX3Zf5Q5O0eY5pX3x6qQ.png)  

---

## **2. Reducción de Dimensionalidad**  
**Objetivo**: Reducir el número de variables (features) manteniendo la información relevante. Útil para visualización o eliminar ruido.  

### **Algoritmos comunes**  

| Modelo               | Idea Básica                                                                 | Ejemplo de Uso                     |  
|----------------------|-----------------------------------------------------------------------------|------------------------------------|  
| **PCA (Análisis de Componentes Principales)** | Transforma datos a un nuevo sistema de ejes ortogonales (componentes). | Compresión de imágenes. |  
| **t-SNE**            | Reduce dimensión preservando distancias locales (ideal para visualización). | Exploración de datos genómicos. |  
| **UMAP**             | Similar a t-SNE, pero más rápido y escalable.                               | Análisis de scRNA-seq (biología). |  

#### **Ejemplo en código (PCA - Python)**  
```python
from sklearn.decomposition import PCA

# Datos de ejemplo: X (alta dimensión, ej.: 100 features)
pca = PCA(n_components=2)  # Reducir a 2 dimensiones
X_reduced = pca.fit_transform(X)  # Transformación SIN etiquetas

# Visualización
plt.scatter(X_reduced[:, 0], X_reduced[:, 1])
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.show()
```
**Salida**:  
![PCA Visualization](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_iris_001.png)  

---

## **Diferencia Clave entre Supervisado y No Supervisado**  
| Característica      | Aprendizaje Supervisado               | Aprendizaje No Supervisado         |  
|---------------------|---------------------------------------|------------------------------------|  
| **Datos**           | Requiere etiquetas (y_train).         | Trabaja sin etiquetas.             |  
| **Objetivo**        | Predecir etiquetas o valores.         | Descubrir patrones ocultos.        |  
| **Métricas**        | Precisión, MSE, etc.                  | Inercia (K-Means), silueta (DBSCAN). |  
| **Ejemplo**         | Clasificar spam.                      | Agrupar clientes no etiquetados.   |  

---

### **Aplicaciones Comunes de No Supervisado**  
- **Marketing**: Segmentación de clientes.  
- **Genómica**: Agrupamiento de células por expresión génica.  
- **Anomalías**: Detección de transacciones fraudulentas (outliers).  

---

### **Resumen**  
- **Clustering**: Para agrupar datos (ej.: K-Means, DBSCAN).  
- **Reducción de dimensionalidad**: Para simplificar datos (ej.: PCA, t-SNE).  
- **No supervisado**: No necesita respuestas conocidas, solo datos en crudo.  