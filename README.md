# T1 - Desarrollo de Software (Sergio / Sebastian)

Este repositorio contiene **dos programas en Python**:

- `p1DS.py`: solución del **Problema 1 (Simulador de enrutamiento)**.
- `p2DS.py`: solución del **Problema 2 (Cliente más fiel por socio)**.

---

## Archivos de entrada (input)

Para ejecutar y probar los programas, se utilizan **archivos `.txt` de entrada**:

- `input1.txt`
- `input2.txt`

Coloca estos archivos en el **mismo directorio** que `p1DS.py` y `p2DS.py` (o ajusta las rutas dentro del código si corresponde).

---

## 1) Simulador de enrutamiento — `p1DS.py`

**Qué hace:** dado un conjunto de rutas (algunas con parámetros como `/user/:id`) y una lista de transiciones, imprime el contenido asociado a cada transición.

- Si la ruta tiene parámetro, imprime: `contenido` + espacio + `valor_parametro`
  - Ejemplo: `/user/:id` con `UserPage` y transición `/user/42` → `UserPage 42`
- Si no coincide con ninguna ruta: imprime `404 Not Found`.

**Cómo ejecutar:**
```bash
python p1DS.py < input1.txt
```

---

## 2) Cliente más fiel por socio — `p2DS.py`

**Qué hace:** para cada socio, identifica el cliente con **más compras** realizadas a través de los terminales de ese socio.

- Si hay empate, elige el cliente con **ID más pequeño**.
- Si el socio no tiene transacciones, imprime `-1`.

**Cómo ejecutar:**
```bash
python p2DS.py < input2.txt
```
