[FEATURE SELECTION](https://machinelearningmastery.com/feature-selection-with-real-and-categorical-data/)

# Guía de Métodos de Selección de Características

## Clasificación por Tipo de Datos

### 1. Variables Numéricas → Target Categórico (Clasificación)

#### **ANOVA F-Test**
- **Cuándo usar**: Variables numéricas continuas con target categórico
- **Ventajas**: Rápido, fácil de interpretar, maneja bien relaciones lineales
- **Desventajas**: Solo detecta relaciones lineales
- **Aplicación**: Ideal para datos con distribución normal y relaciones lineales

#### **Información Mutua (Mutual Information)**
- **Cuándo usar**: Variables numéricas con target categórico, especialmente cuando sospechas relaciones no lineales
- **Ventajas**: Detecta relaciones tanto lineales como no lineales
- **Desventajas**: Más computacionalmente costoso, puede ser sensible al ruido
- **Aplicación**: Mejor para datos complejos con patrones no lineales

### 2. Variables Categóricas → Target Categórico (Clasificación)

#### **Chi-Cuadrado (Chi-Square)**
- **Cuándo usar**: Variables categóricas con target categórico
- **Ventajas**: Específicamente diseñado para datos categóricos, estadísticamente robusto
- **Desventajas**: Requiere frecuencias suficientes en cada categoría
- **Aplicación**: Estándar para evaluar independencia entre variables categóricas

#### **Información Mutua para Categóricas**
- **Cuándo usar**: Variables categóricas con target categórico, como alternativa al Chi-cuadrado
- **Ventajas**: Basado en teoría de la información, maneja bien categorías desbalanceadas
- **Desventajas**: Menos interpretable que Chi-cuadrado
- **Aplicación**: Útil cuando Chi-cuadrado no es apropiado

### 3. Variables Numéricas → Target Numérico (Regresión)

#### **Correlación de Pearson**
- **Cuándo usar**: Variables numéricas con target numérico, relaciones lineales
- **Ventajas**: Simple, rápido, fácil de interpretar
- **Desventajas**: Solo detecta relaciones lineales
- **Aplicación**: Ideal para relaciones lineales simples

#### **Información Mutua para Regresión**
- **Cuándo usar**: Variables numéricas con target numérico, relaciones complejas
- **Ventajas**: Detecta relaciones no lineales
- **Desventajas**: Más costoso computacionalmente
- **Aplicación**: Mejor para relaciones complejas y no lineales

### 4. Datos Mixtos (Numéricos + Categóricos)

#### **Enfoque Combinado**
- **Estrategia**: Aplicar diferentes métodos según el tipo de variable
- **Implementación**: 
  - Chi-cuadrado para categóricas
  - ANOVA F-test para numéricas
  - Combinar resultados usando ranking o puntajes normalizados

#### **Información Mutua Unificada**
- **Ventaja**: Maneja ambos tipos de datos en un solo método
- **Aplicación**: Útil para datasets heterogéneos

## Criterios de Selección

### Por Complejidad Computacional
1. **Más Rápido**: Correlación de Pearson, Chi-cuadrado
2. **Moderado**: ANOVA F-test
3. **Más Lento**: Información Mutua

### Por Tipo de Relación
1. **Relaciones Lineales**: Correlación de Pearson, ANOVA F-test
2. **Relaciones No Lineales**: Información Mutua
3. **Relaciones Categóricas**: Chi-cuadrado

### Por Interpretabilidad
1. **Más Interpretable**: Correlación de Pearson, Chi-cuadrado
2. **Moderadamente Interpretable**: ANOVA F-test
3. **Menos Interpretable**: Información Mutua

---