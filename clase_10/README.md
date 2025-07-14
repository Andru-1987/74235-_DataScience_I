## Clase 10 - CLase Final y Recomendaciones para el proyecto Final

- [DIAPOSITIVA](https://docs.google.com/presentation/d/1pYAm0WjIsU8mDrXxVUtetFwZEOvJvufgpEE-zVZbc2I/edit?slide=id.g221c7b9e280_0_471#slide=id.g221c7b9e280_0_471)

---
### Propuesta de solución con Machine Learning

| Objetivo del negocio                         | Enfoque ML propuesto                                                                                          |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Predecir día de arribo**                   | Modelo de regresión que estime el *lead time* (días entre despacho y entrega).                                |
| **Predecir franja horaria (mañana / tarde)** | Clasificador binario supervisado, alimentado con la misma matriz de características.                          |
| **Avisar al usuario**                        | API de inferencia en línea ‑o un microservicio event‑driven‑ que consulta el modelo y dispara notificaciones. |
| **Optimizar la logística**                   | Explicar la predicción (SHAP) para entender cuellos de botella y replanificar rutas o asignaciones.           |
| **Mejorar la experiencia**                   | Predicciones probabilísticas (p95‑p05) → comunicamos fecha y margen de error; genera confianza.               |

---

## 1. Formulación del problema

* **Regresión multiclase discreta**
  Convertir la fecha destino en *días hasta la entrega* (`eta_days`) y predecir un valor entero ≥ 0.
  Ventaja: elimina la complejidad de trabajar con calendarios y feriados en la capa de modelado.

* **Clasificación binaria**
  Etiqueta `slot = {0: mañana, 1: tarde}` definida por hora real de entrega.

* **Posibilidad avanzada**: Modelo multi‑tarea (e.g. LightGBM con objetivos múltiples) que aprenda simultáneamente ambos targets y capture interdependencias.

---

## 2. Datos necesarios

| Tipo de dato                       | Ejemplos de campos                                                     | Motivo                                               |
| ---------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------- |
| **Paquete**                        | peso, volumen, servicio (exprés / estándar), valor declarado           | Impacto en priorización y manipulación.              |
| **Origen‑destino**                 | código postal, distancia, densidad poblacional                         | Relaciona con tráfico, disponibilidad de sucursales. |
| **Temporal**                       | fecha/hora de admisión, día de semana, feriados, temporada alta        | Influye en capacidad y congestión.                   |
| **Logística interna**              | centro de distribución de salida/llegada, ruta planificada, driver\_id | Explica cuellos de transporte y carga de trabajo.    |
| **Contexto externo (enriquecido)** | pronóstico de clima, alertas de tránsito, huelgas                      | Reduce varianza causada por factores exógenos.       |

Crear un **Feature Store** (p. ej. Feast o Tecton) para unificar estas fuentes y servir tanto offline como online.

---

## 3. Ingeniería de características

1. **Categóricas**

   * Codificación *target‑based* o *leave‑one‑out* para códigos postales, centros de distribución.
2. **Numéricas**

   * Distancia Haversine, densidad de bultos en la misma ruta, ratio peso/volumen.
3. **Frecuencias históricas**

   * Tiempo promedio por tramo logístico (CD → Sucursal, CD → Última Milla).
4. **Ventanas temporales**

   * Cálculo rolling de congestión: paquetes despachados en las últimas 4 h, 24 h.
5. **Calendario enriquecido**

   * Feriados nacionales y provinciales, quiebre mes, picos estacionales (CyberMonday, Navidad).
6. **Clima**

   * Proyecciones de lluvia/nieve a 48 h en destino; discretizar en niveles de severidad.

---

## 4. Modelos candidatos

| Modelo                                                      | Pros                                                                           | Contras                                                              |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------- |
| **Gradient Boosting Trees** (LightGBM / XGBoost / CatBoost) | Lidera en tabulares; manejo nulo de *data prep*; soporta cuantiles             | Interpretabilidad media; se entrena más lento con millones de filas. |
| **Redes tabulares** (TabNet, DeepGBM)                       | Capturan interacciones no lineales; funcionan bien con *embeddings*            | Mayor coste entrenamiento, requiere tuning fino.                     |
| **Survival Analysis / GBDT‑survival**                       | Modela explícitamente la distribución de tiempo; adecuado a eventos censurados | Más complejo de explicar a negocio.                                  |

**Recomendación inicial**: LightGBM ‑ rápido *time‑to‑value*, soporta modo *multiclass* + *quantile regression* (p50, p75, p90). 

---

## 5. Métricas de evaluación

| Target     | Métricas offline                         | Métricas online (post‑deploy)                                                            |
| ---------- | ---------------------------------------- | ---------------------------------------------------------------------------------------- |
| `eta_days` | MAE, RMSE, *pinball loss* para cuantiles | Desviación absoluta media vs. real; porcentaje de entregas dentro del intervalo p90‑p10. |
| `slot`     | Accuracy, F1‑score, ROC‑AUC              | Rate de correctas por día; impacto en re‑intentos de entrega.                            |

Establecer un **baseline** con reglas heurísticas (p. ej. promedio histórico por ruta) para medir uplift real del modelo.

---

## 6. Arquitectura end‑to‑end

```text
┌──────────────┐
│  Historian   │  ▸ BigQuery / Redshift / Lakehouse
└─────┬────────┘
      ▼ (batch ETL, Airflow)
┌──────────────┐
│ Feature Store│  ▸ offline + online
└─────┬────────┘
      ▼ (training job, Vertex AI / SageMaker / MLflow)
┌──────────────┐
│  Model Artf. │  ▸ LightGBM | requirementes.txt +  env
└─────┬────────┘
      ▼ (CI/CD, Docker, FastAPI)
┌──────────────┐
│ Inference API│  ▸ /predict ETA
└─────┬────────┘
      ▼ (Kafka event)
┌──────────────┐
│ Notification │  ▸ envía push/e‑mail/SMS al usuario
└──────────────┘
```

* **Retraining**: Orquestado cada semana o cuando se detecta deriva (Evidently, Prometheus).
* **Explainability**: SHAP valores medios para logística: identificar rutas con mayor incertidumbre.
* **A/B Testing**: Comparar contra heurística para validar KPIs (reintentos, NPS, in‑time deliveries).

---

## 7. Roadmap de implementación

1. **Mes 0‑1**

   * Auditar calidad de datos, definir diccionario y contratos.
   * Construir pipeline de features mínimas (origen‑destino, día de semana, distancia).
2. **Mes 2**

   * Entrenar LightGBM base, evaluar offline; entregar dashboard de métricas.
3. **Mes 3**

   * Desplegar servicio de inferencia. Activar notificaciones piloto en una región.
4. **Mes 4‑5**

   * Agregar variables de clima y congestión; experimentar con quantile regression.
   * Lanzar cobertura nacional; iniciar monitoreo de deriva.
5. **Mes 6+**

   * Migrar a modelo multi‑tarea o survival si la métrica se estanca.
   * Incorporar *reinforcement planning*: priorizar paquetes de alta penalidad SLA.

---

## 8. Beneficios esperados

* **Exactitud**: Reducción del MAE de X → X‑1 día; 80 % de franjas acertadas.
* **Logística**: Menos re‑intentos de entrega, mejor uso de vehículos y turnos.
* **Usuario final**: Mayor confianza al saber día y rango horario; disminución de reclamos.
* **Insight operativo**: Dashboard SHAP evidencia cuellos de ruta, clima o CD específicos.

---

### Por qué esta estrategia
* **Aligna con objetivos**: Predice exactamente lo que el negocio necesita (día + franja) y se integra sin fricciones vía API para alertar al cliente.
* **Escalable**: Funciona sobre datos tabulares, formatos ya presentes en la mayoría de TMS/WMS.
* **Iterativo**: Permite lanzar un MVP rápido y mejorar con más señales (tráfico en tiempo real, telemetría del vehículo).
* **Explainable**: Las direcciones de mejora logística salen de los drivers de la predicción, no de una “caja negra”.

---

## Tecnicas de recomendacion(ie Amazon, ML, otras)

### Filtrado colaborativo vs. Filtrado basado en contenido

Son dos estrategias principales utilizadas en sistemas de recomendación, con enfoques muy distintos:

---

## Filtrado colaborativo (Collaborative Filtering)

**¿Qué es?**
Recomienda ítems a un usuario utilizando el comportamiento o preferencias de otros usuarios. No se basa en las características de los ítems, sino en las interacciones previas entre usuarios e ítems.

**Ejemplos comunes:**

* Netflix: recomienda películas que vieron otros usuarios con gustos similares.
* Amazon: “Los usuarios que compraron este producto también compraron…”
* Spotify: listas generadas a partir de lo que escuchan personas con gustos similares.
* Goodreads: sugiere libros a partir de lo que otros usuarios con valoraciones similares han leído.
* Mercado Libre: productos que otros usuarios compraron junto con lo que estás viendo.

**Estrategias más usadas:**

* *User-based filtering*: encuentra usuarios parecidos y recomienda lo que ellos consumieron.
* *Item-based filtering*: encuentra ítems similares en función de los usuarios que los consumieron.

**Ventajas:**

* Personalización más profunda basada en la comunidad.
* Puede descubrir ítems que no se parecen superficialmente, pero resultan interesantes por asociación.

**Desventajas:**

* Problema de arranque en frío (cuando hay pocos usuarios o interacciones).
* Dificultad para recomendar ítems nuevos.

---

## Filtrado basado en contenido (Content-Based Filtering)

**¿Qué es?**
Recomienda ítems similares a los que el usuario ya consumió, basándose en las características del contenido.

**Ejemplos comunes:**

* YouTube: recomienda videos con descripciones, etiquetas o categorías similares a lo que viste.
* Spotify: recomendaciones en base a características acústicas de las canciones que escuchás.
* LinkedIn: sugiere cursos o empleos según el perfil profesional del usuario.
* Amazon Prime Video: te muestra más series con el mismo género, actores o director.
* Google News: presenta noticias con temáticas relacionadas a las que leíste.

**Estrategias más usadas:**

* Representación vectorial de los ítems (TF-IDF, embeddings).
* Similitud coseno entre ítems y el perfil del usuario.
* Clasificadores o modelos de puntuación que predicen la probabilidad de que un usuario consuma un ítem, en base a sus características.

**Ventajas:**

* Buen rendimiento con pocos usuarios, si hay datos sobre el contenido.
* Capacidad de recomendar ítems nuevos, siempre que tengan descripciones o atributos disponibles.

**Desventajas:**

* Riesgo de sobreespecialización (solo se recomienda contenido similar al consumido).
* Requiere buenas descripciones de los ítems.

---

## Diferencias clave entre ambos enfoques

| Característica                 | Filtrado colaborativo            | Filtrado basado en contenido         |
| ------------------------------ | -------------------------------- | ------------------------------------ |
| Fuente principal de datos      | Comportamiento de otros usuarios | Características del ítem             |
| Necesita conocer el ítem       | No necesariamente                | Sí, requiere metadatos               |
| Usuario nuevo (cold start)     | Problemático                     | Mejor si el perfil se puede inferir  |
| Ítem nuevo (cold start)        | Difícil recomendar               | Recomendable si se conoce su perfil  |
| Riesgo de sobreespecialización | Bajo (variedad por comunidad)    | Alto (tiende a repetir preferencias) |

---

## Estrategias para diferenciarlos

* Analizar si las recomendaciones provienen de información sobre ítems o sobre usuarios.
* Si el sistema sugiere ítems que *otros* usuarios similares consumieron, es colaborativo.
* Si el sistema sugiere ítems similares a los que *yo mismo* consumí, es basado en contenido.
* Revisar si puede recomendar ítems nuevos sin historial: si lo hace, probablemente use contenido.

