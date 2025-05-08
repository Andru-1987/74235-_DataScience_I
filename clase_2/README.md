## 🧠 Clase: Fundamentos de Python para Ciencia de Datos

### **1. Introducción a Python**
[GUIA DE CLASE](https://docs.google.com/presentation/d/1jMeDrYaVZE7IYGxo6fF4dGYgT-KHFZJmzr-vAKvVGes/edit#slide=id.g2204f2a9531_0_0)

**Objetivo:** Comprender por qué Python es tan usado en ciencia de datos.

**Contenido:**

* Breve historia de Python.
* Sintaxis limpia, comunidad activa.
* Ecosistema (NumPy, pandas, matplotlib, scikit-learn).
* Entornos comunes: Jupyter, Google Colab, VSCode.

**Ejercicio breve:**

```python
# Tu primer notebook: imprime tu nombre y tu lenguaje favorito
nombre = "Andru"
print(f"Hola, mi nombre es {nombre} y estoy aprendiendo Python para ciencia de datos.")
```

---

### **2. Estructuras de Datos y Operaciones Básicas**

**Objetivo:** Usar listas, diccionarios, tuplas y sets.

**Contenido:**

* Tipos de datos: `int`, `float`, `str`, `bool`
* Contenedores: `list`, `tuple`, `set`, `dict`
* Indexing, slicing, comprensión de listas

**Ejercicio guiado:**

```python
edades = [25, 30, 22, 40, 29]
print(f"Edad máxima: {max(edades)}")
print(f"Edad promedio: {sum(edades)/len(edades):.2f}")
```

**Ejercicio práctico:**

```python
# Crear un diccionario de nombres y edades, luego imprimir los mayores de 30
personas = {"Ana": 28, "Luis": 34, "Carla": 22, "Jorge": 41}
for nombre, edad in personas.items():
    if edad > 30:
        print(f"{nombre} tiene {edad} años")
```

---

### **3. Control de Flujo y Funciones**

**Objetivo:** Aplicar condicionales, bucles y funciones propias.

**Contenido:**

* `if`, `elif`, `else`
* `for`, `while`
* Funciones con `def`, argumentos, retorno

**Ejercicio guiado:**

```python
def es_par(num):
    return num % 2 == 0

print(es_par(4))  # True
```

**Ejercicio práctico:**

```python
# Escribir una función que reciba una lista de números y devuelva cuántos son positivos
def contar_positivos(lista):
    return sum(1 for n in lista if n > 0)

print(contar_positivos([-1, 2, 5, -3, 0, 7]))
```

---

### **4. Programación Orientada a Objetos**

**Objetivo:** Entender clases, atributos y métodos.

**Contenido:**

* `class`, `__init__`, `self`
* Métodos de instancia
* Representación con `__str__` o `__repr__`

**Ejercicio guiado:**

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

juan = Persona("Juan", 30)
juan.saludar()
```

**Ejercicio práctico:**

```python
# Crear una clase `Producto` con atributos: nombre, precio y categoría.
# Agregar un método para mostrar la información con formato.
class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def mostrar_info(self):
        return f"{self.nombre} (${self.precio}) - Categoría: {self.categoria}"

p = Producto("Notebook", 3500, "Electrónica")
print(p.mostrar_info())
```

## 🧪 Ejercicio: Referencias de Objetos en Python (Punteros implícitos)

```python
# Creamos una lista
a = [1, 2, 3]
b = a  # b no es una copia de a, ¡es la misma referencia!

b.append(4)

print("a:", a)
print("b:", b)

print("¿a y b son el mismo objeto?", a is b)
```

### 🧠 ¿Qué demuestra esto?

* `a` y `b` apuntan al mismo objeto en memoria.
* Modificar uno **afecta al otro**.
* `is` compara **identidad** (referencia), no contenido.

---

## 🔁 Contraste: Copia real (nueva referencia)

```python
# Ahora hacemos una copia real de la lista
a = [1, 2, 3]
b = a.copy()  # o list(a)

b.append(4)

print("a:", a)
print("b:", b)
print("¿a y b son el mismo objeto?", a is b)
```

---

## 🧰 Extra: Con objetos propios

```python
class Caja:
    def __init__(self, contenido):
        self.contenido = contenido

c1 = Caja("gatito")
c2 = c1  # Misma referencia

c2.contenido = "perrito"

print("Contenido de c1:", c1.contenido)
print("¿c1 y c2 son el mismo objeto?", c1 is c2)
```


---

### 🏁 Cierre y Desafío Final

**Mini Desafío:** Crear una clase `Alumno` con métodos para guardar calificaciones y calcular el promedio.