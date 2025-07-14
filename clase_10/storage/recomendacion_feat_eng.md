### Análisis del Dataset `insurance.csv`

**Características del dataset:**
- **Variables numéricas**: `income`, `age`, `claims`
- **Variables categóricas**: `sex`, `approval`, `fraud`
- **Target**: `approval` (categórico: Approved/Denied)
- **Tipo de problema**: Clasificación binaria

### Método Recomendado: **Enfoque Combinado**

#### Para Variables Numéricas (`income`, `age`, `claims`):
- **Método primario**: **ANOVA F-test**
  - Ideal para evaluar si estas variables numéricas tienen diferencias significativas entre grupos (Approved/Denied)
  - Rápido y estadísticamente robusto
  
- **Método secundario**: **Información Mutua**
  - Como validación para detectar posibles relaciones no lineales

#### Para Variables Categóricas (`sex`, `fraud`):
- **Método recomendado**: **Chi-cuadrado**
  - Perfecto para evaluar la independencia entre variables categóricas y el target
  - Estadísticamente apropiado para este tipo de datos

### Implementación Sugerida:

```python
from sklearn.feature_selection import SelectKBest, chi2, f_classif, mutual_info_classif

# Para variables numéricas
numeric_features = ['income', 'age', 'claims']
selector_numeric = SelectKBest(score_func=f_classif, k=2)

# Para variables categóricas
categorical_features = ['sex', 'fraud']  
selector_categorical = SelectKBest(score_func=chi2, k=1)
```

### Justificación:
1. **Datos balanceados**: Tu dataset parece tener suficientes ejemplos para ambos métodos
2. **Relaciones esperadas**: Probablemente lineales/monotónicas (ingresos, edad vs aprobación)
3. **Interpretabilidad**: Importante en contexto de seguros para explicar decisiones
4. **Eficiencia**: Métodos rápidos apropiados para el tamaño del dataset