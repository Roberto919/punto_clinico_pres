# Punto Clínico
**Author: Rob**

## ⏬ Descarga de datos de Myle

### La información procesada proveniente de Myle fue descargada siguiendo estos pasos:

1. Descarga de datos relacionados con citas
   1. INFORME
   2. LISTA DETALLADA DE LAS CITAS
   3. Ajustar fechas para la descarga de información
   4. Descarga de tabla con todos los datos registrados
2. Descarga de datos relacionados con ventas
   1. FACTURACIÓN
   2. VENTAS
   3. Ajuste de las fechas para abarcar todos los datos
   4. Descarga de los datos

------

## 🔎 Clasificacion de especialidades

### Para identificar la especialidad asociada a una entrada específica de ventas o citas, se sigue el siguiente procedimiento:

1. Buscar alguna de las palabras claves del diccionario `specialties_ref` (Anexo 1) en el campo "Asunto" de la cita o registro de venta.
2. Buscar con base en el doctor asociado a la cita o registro de venta. La búsqueda se basa en la lista de doctores llamada `meds_dict_ref` (Anexo 2)
3. En caso de que el paso 1 o el paso 2 no hayan dado resultado, se registra la entrada con la etiqueta "OTRA_ESP"

------

------

## 📌 Clasificación por línea de negocio

### Para identificar la línea de negocio asociada a una entrada específica de ventas o citas, se sigue el siguiente procedimiento:

1. Las entradas asociada a una ubicación/sucursal que incluya la palabra "LABORATORIO" es clasificada automáticamente con la línea de negocio "LABORATORIO"
2. Búsqueda de coincidencias entre la descripción del registro de ventas o cita y el diccionario de palabras claves de líneas de negocio `business_line_ref` (Anexo 3)
3. En caso de que el paso 1 o el paso 2 no hayan dado resultado, se registra la entrada con la etiqueta "OTRA_LN"

------