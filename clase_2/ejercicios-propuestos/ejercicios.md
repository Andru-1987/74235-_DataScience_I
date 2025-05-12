# Análisis de Retrocesos en el Valor de la Acción - Compañía X

Se tiene una lista con los valores promedio diarios del precio de la acción de la compañía **X** durante la semana pasada:

```py
valores = [200, 225, 232, 221, 243, 256, 255]
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

```

## Objetivo

Determinar los días en los que **hubo un retroceso** en el valor de la acción respecto al día anterior.


```python
import numpy as np 

Valores = [200, 225, 232, 221, 243, 256, 255]
Dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

# Calcular las diferencias entre días consecutivos
diferencias = np.diff(Valores)

# Iterar desde el segundo día (índice 1) ya que diff devuelve un arreglo con n-1 elementos
for i, cambio in enumerate(diferencias, start=1):
    if cambio < 0:
        print(f"Hubo un retroceso el día {Dias[i]} (valor: {Valores[i]} vs día anterior: {Valores[i-1]})")
```


---
