## DATE RELATED TO PROJECT DEVELOPMENT TASKS, DEADLINES AND ADVANCEMENTS
#### Author: Rob (GH: Roberto919)
#### Date: 25 June 2020





'------------------------------------------------------------------------------------------'
#############
## Imports ##
#############

from datetime import *





'------------------------------------------------------------------------------------------'
################
## Parameters ##
################


## Definition dictionary
def_dict = {
    'No.': {
        'relevant': False
    },
    'Nombre de tarea': {
        'relevant': False
    },
    'Duración': {
        'relevant': False
    },
    'Comienzo': {
        'relevant': False
    },
    'Fin': {
        'relevant': False
    },
    'Comienzo.1': {
        'relevant': True,
        'gantt_name': 'Start'
    },
    'Fin.1': {
        'relevant': True,
        'gantt_name': 'Finish'
    },
    'Predecesoras': {
        'relevant': False
    },
    '% completado': {
        'relevant': True,
        'gantt_name': 'Complete'
    },
    'Tarea_strip': {
        'relevant': True,
        'gantt_name': 'Task'
    },
    'RevRobf': {
        'relevant': True,
        'gantt_name': 'Complete'
    }
}



## List of followup activities.
#### Code related to revisions' status:
###### 0.0 -> not reviewed yet.
###### 0.5 -> reviewed but not clear if its functioning well.
###### 1.0 -> reviewed and validated that its working properly.
followup_dev_activities = {
    "Seed --> Proyecto consultorios": {
        "No.": 1,
        "RevRob": 0.5,
        "Notas_Rob": "En proceso"
    },
    "Proyecto consultorios --> Inicio": {
        "No.": 2,
        "RevRob": 0.5,
        "Notas_Rob": "En proceso"
    },
    "Proyecto consultorios --> Diseño pantallas": {
        "No.": 3,
        "RevRob": 0.5,
        "Notas_Rob": "Todavía no están listas todas las secciones del diseño de pantallas."
    },
    "Diseño pantallas --> Personalización menú superior": {
        "No.": 4,
        "RevRob": 0.5,
        "Notas_Rob": "- [ ] En Configuración/Catálogos/ hay dos entradas relacionadas con proveedores que no sé si sean redundantes. - [X] El botón Pacientes parece que no hace nada         "
    },
    "Diseño pantallas --> Diseño de lateral izquierdo-buscador": {
        "No.": 5,
        "RevRob": 1.0,
        "Notas_Rob": "- [X] El buscador si filtra por nombres correctamente. - [X] El buscador filtra por número telefónico correctamente (parcial o completo). - [X] También se puede buscar por número de expediente.         "
    },
    "Diseño pantallas --> Calendario de vista por mes con colores con acciones": {
        "No.": 6,
        "RevRob": 0.5,
        "Notas_Rob": "- [ ] Según yo no hay colores en este calendario. - [X] Los botones día de este calendario funcionan bien. - [ ] No se muestran las citas y colores asocuados a la semana.         "
    },
    "Diseño pantallas --> Calendario de vista por día": {
        "No.": 7,
        "RevRob": 0.5,
        "Notas_Rob": "- [X] El calendario cambia de color cuando se realizan acciones. - [ ] Ver calendarios de distintos médicos al mismo tiempo. - [X] Los espcios cancelados ya se pueden reutilizar.  - [ ] Parece que hay un bug en el que de repente se divide la pantalla de un médico 'undefined'- [ ] (Bug) Cuando están en un calendario vista por semana y cambias de médico se ve raro el calendario.        "
    },
    "Diseño pantallas --> Lista de pacientes": {
        "No.": 8,
        "RevRob": 0.5,
        "Notas_Rob": "No está claro a qué se refieren con la lista de pacientes."
    },
    "Diseño pantallas --> Lista de Médicos": {
        "No.": 9,
        "RevRob": 0.5,
        "Notas_Rob": "No está claro a lo que se refieren con este concepto."
    },
    "Diseño pantallas --> Criterios de impresión": {
        "No.": 10,
        "RevRob": 0.5,
        "Notas_Rob": "No está claro a lo que se refieren con este concepto."
    },
    "Diseño pantallas --> Calendario de vista por semana": {
        "No.": 11,
        "RevRob": 1.0,
        "Notas_Rob": "- [X] La vista por semana sí muestra las distintas citas con colores y demás.        "
    },
    "Diseño pantallas --> Alta rapida de pacientes-buscador": {
        "No.": 12,
        "RevRob": 0.5,
        "Notas_Rob": "- [X] La funcionalidad sí opera correctamente- [ ] Tarda mucho en que se carguen los resultados del calendario.- [X] Ya solo se despliegan los horarios laborales en lugar de todos.- [X] Las citas canceladas ya aparecen aquí.        "
    },
    "Diseño pantallas --> Busqueda avanzada, filtros de citas": {
        "No.": 13,
        "RevRob": 0.5,
        "Notas_Rob": "No está claro a lo que se refieren con este concepto."
    },
    "Diseño pantallas --> Detalles de citas:Alta, Consulta, Actualización": {
        "No.": 14,
        "RevRob": 0.5,
        "Notas_Rob": "\
- [X] Cuando se le da click a una cita sí se abre correctamente.\
- [ ] Se había solicitado que se agreguen leyendas debajo del nombre del paciente.\
        "
    },
    "Diseño pantallas --> Expediente clinico paciente": {
        "No.": 15,
        "RevRob": 1.0,
        "Notas_Rob": "\
- [X] Se observó la funcionalidad de las distintas pantallas del expediente\
        "
    },
    "Expediente clinico paciente --> Encabezado expediente clinico": {
        "No.": 16,
        "RevRob": 0.5,
        "Notas_Rob": "\
- [ ] Solicitamos cambio para ver historial de citas del paciente\
- [ ] Solicitamos cambio para ver resumen\
        "
    },
    "Expediente clinico paciente --> Lateral expediente clinico (iconos)": {
        "No.": 17,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrian"
    },
    "Expediente clinico paciente --> Pantalla Datos demograficos": {
        "No.": 18,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrian"
    },
    "Expediente clinico paciente --> Pantalla Contactos": {
        "No.": 19,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrian"
    },
    "Expediente clinico paciente --> Pantalla Profesional a cargo": {
        "No.": 20,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrian"
    },
    "Expediente clinico paciente --> Pantalla Relaciones": {
        "No.": 21,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrian"
    },
    "Expediente clinico paciente --> Agenda rapida de cita del paciente": {
        "No.": 22,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrian; es la lupa."
    },
    "Expediente clinico paciente --> Pantalla lateral izquierda, Historial de citas": {
        "No.": 23,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrian."
    },
    "Expediente clinico paciente --> Pantalla Cita-Detalle de consulta": {
        "No.": 24,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrian."
    },
    "Expediente clinico paciente --> Pantalla Cita-Mensajeria": {
        "No.": 25,
        "RevRob": 0.5,
        "Notas_Rob": "Se revisó con Adrian. Hay que ver si se cambia algo."
    },
    "Expediente clinico paciente --> Pantalla Cita-Tarea": {
        "No.": 26,
        "RevRob": 0.5,
        "Notas_Rob": "Se revisó con Adrian. Hay que ver si se cambia algo."
    },
    "Expediente clinico paciente --> Pantalla Cita-Recordatorio": {
        "No.": 27,
        "RevRob": 0.5,
        "Notas_Rob": "Se revisó con Adrian. Hay que ver si se cambia algo."
    },
    "Expediente clinico paciente --> Pantalla Cita-Comunicaciones": {
        "No.": 28,
        "RevRob": 0.0,
        "Notas_Rob": "Se revisó con Adrian. Hay que ver si se cambia algo."
    },
    "Expediente clinico paciente --> Pantalla Cita-Cargos a paciente": {
        "No.": 29,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrian."
    },
    "Expediente clinico paciente --> Pantalla de administrar documentos": {
        "No.": 30,
        "RevRob": 0.5,
        "Notas_Rob": "Se revisó con Adrian. Se intetó cargar una radiografía como ejemplo pero falló."
    },
    "Expediente clinico paciente --> Pantalla de carga de documentos": {
        "No.": 31,
        "RevRob": 0.5,
        "Notas_Rob": "Se intentó hacer un ejemplo y falló."
    },
    "Diseño pantallas --> Historia clinica del paciente": {
        "No.": 32,
        "RevRob": 0.5,
        "Notas_Rob": "No estoy seguro de la diferencia entre el historial y el expediente clínico."
    },
    "Historia clinica del paciente --> Encabezado de la historia clinica": {
        "No.": 33,
        "RevRob": 1.0,
        "Notas_Rob": "Revisado y está bien."
    },
    "Diseño pantallas --> Sección de Resumen medico": {
        "No.": 34,
        "RevRob": 1.0,
        "Notas_Rob": "\
- [X] Se probaron y revisaron las funcionalidades de esta sección con el Dr. Said.\
        "
    },
    "Sección de Resumen medico --> Pantalla de Historial medico": {
        "No.": 35,
        "RevRob": 1.0,
        "Notas_Rob": "\
- [X] La pantalla sí muestra los elementos del historial médico.\
        "
    },
    "Sección de Resumen medico --> Pantalla lateral izquierda, Antecedentes y diagnosticos": {
        "No.": 36,
        "RevRob": 1.0,
        "Notas_Rob": "\
- [X] Se probaron y revisaron las funcionalidades de esta sección con el Dr. Said.\
        "
    },
    "Sección de Resumen medico --> Pantalla de Alergias e intolerancia": {
        "No.": 37,
        "RevRob": 0.5,
        "Notas_Rob": "\
- [ ] Se solicitó que se activaran algunas alarmas relacionadas con intolerancias.\
        "
    },
    "Sección de Resumen medico --> Pantalla Habitos sociales": {
        "No.": 38,
        "RevRob": 1.0,
        "Notas_Rob": "\
- [X] Se probaron y revisaron las funcionalidades de esta sección con el Dr. Said.\
        "
    },
    "Sección de Resumen medico --> Pantalla Alertas y necesidades especiales": {
        "No.": 39,
        "RevRob": 0.5,
        "Notas_Rob": "\
- [ ] Se solicitó que se activaran algunas alarmas relacionadas con intolerancias.\
        "
    },
    "Sección de Resumen medico --> Pantalla antecedentes familiares": {
        "No.": 40,
        "RevRob": 1.0,
        "Notas_Rob": "\
- [X] Se probaron y revisaron las funcionalidades de esta sección con el Dr. Said.\
        "
    },
    "Sección de Resumen medico --> Pantalla Inmunizaciones": {
        "No.": 41,
        "RevRob": 0.5,
        "Notas_Rob": "\
- [ ] Se había solicitado que se cambiaran 'cc' por 'ml'. No se ha podido verificar que sea así.\
        "
    },
    "Sección de Resumen medico --> Pantalla Medicamentos activos": {
        "No.": 42,
        "RevRob": 0.5,
        "Notas_Rob": "\
- [ ] Se habían solicitado varios cambios que al parecer todavía no están todos.\
        "
    },
    "Sección de Resumen medico --> Pantalla signos vitales": {
        "No.": 43,
        "RevRob": 1.0,
        "Notas_Rob": "\
- [X] Se probaron y revisaron las funcionalidades de esta sección con el Dr. Said.\
        "
    },
    "Sección de Resumen medico --> Control de escala de dolor": {
        "No.": 44,
        "RevRob": 1.0,
        "Notas_Rob": "\
- [X] Se probaron y revisaron las funcionalidades de esta sección con el Dr. Said.\
        "
    },
    "Sección de Resumen medico --> Pantalla de aprobacion de historia clinica": {
        "No.": 45,
        "RevRob": 1.0,
        "Notas_Rob": "Revisión con Adrián."
    },
    "Sección de Resumen medico --> Notas de Evolución": {
        "No.": 46,
        "RevRob": 0.5,
        "Notas_Rob": "Faltan algunas cosillas."
    },
    "Notas de Evolución --> Pantalla de motivo de consulta": {
        "No.": 47,
        "RevRob": 1.0,
        "Notas_Rob": "\
- [X] La pantalla se activa correctamente\
        "
    },
    "Notas de Evolución --> Pantalla de Principio, Evolución, Estado": {
        "No.": 48,
        "RevRob": 1.0,
        "Notas_Rob": "\
- [X] La pantalla se activa correctamente\
        "
    },
    "Notas de Evolución --> Pantalla de Exploración": {
        "No.": 49,
        "RevRob": 1.0,
        "Notas_Rob": "\
- [X] La pantalla se activa correctamente\
        "
    },
    "Notas de Evolución --> Pantalla de notas manuscritas (cámara)": {
        "No.": 50,
        "RevRob": 1.0,
        "Notas_Rob": "\
- [X] La pantalla se activa correctamente y la camara sí se activa\
        "
    },
    "Notas de Evolución --> Pantalla de imágenes": {
        "No.": 51,
        "RevRob": 1.0,
        "Notas_Rob": "\
- [X] La pantalla se activa correctamente\
        "
    },
    "Notas de Evolución --> Pantalla de otras notas": {
        "No.": 52,
        "RevRob": 1.0,
        "Notas_Rob": "\
- [X] La pantalla se activa correctamente\
        "
    },
    "Sección de Resumen medico --> Evaluación": {
        "No.": 53,
        "RevRob": 1.0,
        "Notas_Rob": "\
- [X] Se probaron y revisaron las funcionalidades de esta sección con el Dr. Said.\
        "
    },
    "Evaluación --> Pantalla de Antecedentes y diagnosticos": {
        "No.": 54,
        "RevRob": 0.5,
        "Notas_Rob": "\
- [ ] Se solicitó el cambio menor de eliminar 'Historial Gineco-Obstetricio'\
        "
    },
    "Sección de Resumen medico --> Plan": {
        "No.": 55,
        "RevRob": 1.0,
        "Notas_Rob": "\
- [X] Se probaron y revisaron las funcionalidades de esta sección con el Dr. Said.\
        "
    },
    "Plan --> Pantalla de recetas": {
        "No.": 56,
        "RevRob": 0.5,
        "Notas_Rob": "\
- [ ] Una vez que se le da recetar al medicamento hay que agregar la posibilidad de que se pueda modificar la receta. No se podrá hacer después de picar 'Aprobar'.\
- [ ] Agregar opción de poder modificar las notas médicas del paciente después de 'Aprobadas'.\
        "
    },
    "Plan --> Pantalla de solicitud de examen": {
        "No.": 57,
        "RevRob": 0.5,
        "Notas_Rob": "\
- [ ] Modificar etiqueta 'Razón'→ 'Estudio'.\
- [ ] Agregar botón para imprimir solicitudes de examen y enviar por correo.\
        "
    },
    "Plan --> Pantalla de solicitud de interconsulta": {
        "No.": 58,
        "RevRob": 0.5,
        "Notas_Rob": "No estoy seguro qué es esto"
    },
    "Plan --> Pantalla de seguimiento y plan": {
        "No.": 59,
        "RevRob": 1.0,
        "Notas_Rob": "\
- [X] La pantalla se activa correctamente\
        "
    },
    "Plan --> Pantalla de comunicaciones-Nuevo recordatorio": {
        "No.": 60,
        "RevRob": 0.5,
        "Notas_Rob": "Se debería eliminar según doctor Said; podemos desactivarlo."
    },
    "Plan --> Pantalla de comunicaciones-Nuevo mensaje": {
        "No.": 61,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Dr. Said."
    },
    "Plan --> Pantalla nuevo cargo": {
        "No.": 62,
        "RevRob": 0.5,
        "Notas_Rob": "Se pidieron cambios."
    },
    "Sección de Resumen medico --> Comunicaciones": {
        "No.": 63,
        "RevRob": 0.5,
        "Notas_Rob": "Está pendiente por revisar con el Dr. Said."
    },
    "Comunicaciones --> Pantalla bandeja comunicaciones": {
        "No.": 64,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián."
    },
    "Comunicaciones --> Pantalla Recordatorios": {
        "No.": 65,
        "RevRob": 0.5,
        "Notas_Rob": "\
- [ ] El Dr. Said comentó que no deberían haber recordatorios.\
"
    },
    "Pantalla Recordatorios --> Pantalla de recordatorio": {
        "No.": 66,
        "RevRob": 0.5,
        "Notas_Rob": "\
- [ ] El Dr. Said comentó que no deberían haber recordatorios.\
"
    },
    "Comunicaciones --> Pantalla de mensajes": {
        "No.": 67,
        "RevRob": 1.0,
        "Notas_Rob": "\
- [X] Se revisó con el Dr. Said y funciona bien.\
"
    },
    "Pantalla de mensajes --> Pantalla Mensajes-Enviados": {
        "No.": 68,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián."
    },
    "Pantalla de mensajes --> Pantalla Mensajes-Borrador": {
        "No.": 69,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián."
    },
    "Pantalla de mensajes --> Pantalla Mensajes-Archivo": {
        "No.": 70,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián."
    },
    "Pantalla de mensajes --> Pantalla Mensajes-Basura": {
        "No.": 71,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián."
    },
    "Comunicaciones --> Pantalla Tareas": {
        "No.": 72,
        "RevRob": 0.5,
        "Notas_Rob": "\
- [ ] Se deberían eliminar las tareas según Dr. Said.\
"
    },
    "Pantalla Tareas --> Pantalla Tareas-Enviados": {
        "No.": 73,
        "RevRob": 0.5,
        "Notas_Rob": "\
- [ ] Se deberían eliminar las tareas según Dr. Said.\
"
    },
    "Pantalla Tareas --> Pantalla Tareas-Borrador": {
        "No.": 74,
        "RevRob": 0.5,
        "Notas_Rob": "\
- [ ] Se deberían eliminar las tareas según Dr. Said.\
"
    },
    "Pantalla Tareas --> Pantalla Tareas-Archivo": {
        "No.": 75,
        "RevRob": 0.5,
        "Notas_Rob": "\
- [ ] Se deberían eliminar las tareas según Dr. Said.\
"
    },
    "Pantalla Tareas --> Pantalla Tareas-Basura": {
        "No.": 76,
        "RevRob": 0.5,
        "Notas_Rob": "\
- [ ] Se deberían eliminar las tareas según Dr. Said.\
"
    },
    "Comunicaciones --> Nuevas pantallas": {
        "No.": 77,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián."
    },
    "Nuevas pantallas --> Apertura de horarios": {
        "No.": 78,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián."
    },
    "Nuevas pantallas --> Creación de horarios": {
        "No.": 79,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián."
    },
    "Nuevas pantallas --> Resultados": {
        "No.": 80,
        "RevRob": 0.5,
        "Notas_Rob": "Revisé con Adrián pero no llegamo a conclusión."
    },
    "Nuevas pantallas --> Pantalla de comunicaciones - nueva tarea": {
        "No.": 81,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián."
    },
    "Nuevas pantallas --> Portafolios": {
        "No.": 82,
        "RevRob": 0.5,
        "Notas_Rob": "Se omitió según Adrian."
    },
    "Proyecto consultorios --> Analisis": {
        "No.": 83,
        "RevRob": 0.5,
        "Notas_Rob": "Según Adrián no es relevante para las estadísticas."
    },
    "Analisis --> Análisis de usuarios": {
        "No.": 84,
        "RevRob": 0.5,
        "Notas_Rob": "No estamos seguros."
    },
    "Analisis --> Análisis de roles seguridad": {
        "No.": 85,
        "RevRob": 0.5,
        "Notas_Rob": "Está pendiente de nuestro lado acabarlo."
    },
    "Analisis --> Análisis de politicas de seguridad": {
        "No.": 86,
        "RevRob": 0.5,
        "Notas_Rob": "Están creandose perfiles. Están acabando el trabajo. Revisar el viernes 13 de Nov."
    },
    "Analisis --> Análisis de sucursales": {
        "No.": 87,
        "RevRob": 0.5,
        "Notas_Rob": "Podremos revisarlos el viernes 13."
    },
    "Analisis --> Análisis de figuras tributarias": {
        "No.": 88,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de especialidades": {
        "No.": 89,
        "RevRob": 1.0,
        "Notas_Rob": "Revisión con Adrián"
    },
    "Analisis --> Análisis de pacientes": {
        "No.": 90,
        "RevRob": 1.0,
        "Notas_Rob": "Revisión con Adrián"
    },
    "Analisis --> Análisis de lista de precios": {
        "No.": 91,
        "RevRob": 1.0,
        "Notas_Rob": "Revisión con Adrián"
    },
    "Analisis --> Análisis de Nemóticos": {
        "No.": 92,
        "RevRob": 1.0,
        "Notas_Rob": "Asociación de claves con elementos de la plataforma."
    },
    "Analisis --> Análisis de tipos de servicios": {
        "No.": 93,
        "RevRob": 1.0,
        "Notas_Rob": "Revisión con Adrián; se basó en catálogo que nosotros mandamos."
    },
    "Analisis --> Análisis de Servicios": {
        "No.": 94,
        "RevRob": 1.0,
        "Notas_Rob": "Revisión con Adrián"
    },
    "Analisis --> Análisis de Medicamentos e insumos": {
        "No.": 95,
        "RevRob": 0.5,
        "Notas_Rob": "Revisión con Adrián; falta cargar catálogo; ¿quién lo carga?"
    },
    "Analisis --> Análisis de proveedor": {
        "No.": 96,
        "RevRob": 1.0,
        "Notas_Rob": "Revisión con Adrián; solo falta cargar nosotros los proveedores."
    },
    "Analisis --> Análisis de consultorios": {
        "No.": 97,
        "RevRob": 1.0,
        "Notas_Rob": "No fue implementada. Ahorita no se utiliza."
    },
    "Analisis --> Análisis de tipo de recurrencia": {
        "No.": 98,
        "RevRob": 0.5,
        "Notas_Rob": "No estámos seguros pero parece que no es relevante."
    },
    "Analisis --> Análisis de agendas": {
        "No.": 99,
        "RevRob": 0.5,
        "Notas_Rob": "Pensamos que el tema de creación de horarios es muy complicado."
    },
    "Analisis --> Análisis de Doctores": {
        "No.": 100,
        "RevRob": 1.0,
        "Notas_Rob": "Revisión con Adrián la configuración de médicos y los guardados."
    },
    "Analisis --> Análisis de instituciones de referencia": {
        "No.": 101,
        "RevRob": 1.0,
        "Notas_Rob": "Revisión con Adrián"
    },
    "Analisis --> Análisis de Historia clinica": {
        "No.": 102,
        "RevRob": 1.0,
        "Notas_Rob": "Revisión con Adrián"
    },
    "Analisis --> Análisis de notas clinicas": {
        "No.": 103,
        "RevRob": 1.0,
        "Notas_Rob": "Revisión con Adrián"
    },
    "Análisis de notas clinicas --> Nueva nota": {
        "No.": 104,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Análisis de notas clinicas --> Problemas activos": {
        "No.": 105,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Análisis de notas clinicas --> Historial médico": {
        "No.": 106,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Análisis de notas clinicas --> Historial quirúrgico": {
        "No.": 107,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Análisis de notas clinicas --> Historial psiquiátrico": {
        "No.": 108,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián. Implícito en quirúrgico."
    },
    "Análisis de notas clinicas --> Historial Gineco-Obstétrico": {
        "No.": 109,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Análisis de notas clinicas --> Medicamentos activos": {
        "No.": 110,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Análisis de notas clinicas --> Alergias e intolerancias": {
        "No.": 111,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián; ya se implementaron las alertas."
    },
    "Análisis de notas clinicas --> Hábitos sociales": {
        "No.": 112,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Análisis de notas clinicas --> Alertas y necesidades especiales": {
        "No.": 113,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Análisis de notas clinicas --> Inmunizaciones": {
        "No.": 114,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Análisis de notas clinicas --> Antecedentes familiares": {
        "No.": 115,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Analisis --> Análisis de Expediente de documentos": {
        "No.": 116,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Analisis --> Análisis de politicas de descuentos": {
        "No.": 117,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Analisis --> Análisis de Orden de servicio": {
        "No.": 118,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián."
    },
    "Analisis --> Análisis de generación de venta": {
        "No.": 119,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de facturación": {
        "No.": 120,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de cuentas por cobrar": {
        "No.": 121,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de turnos": {
        "No.": 122,
        "RevRob": 0.5,
        "Notas_Rob": "Parece que no son necesarios."
    },
    "Analisis --> Análisis de Cajas": {
        "No.": 123,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián."
    },
    "Analisis --> Analisis de cajeros": {
        "No.": 124,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián."
    },
    "Analisis --> Analisis de cotizaciones": {
        "No.": 125,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián."
    },
    "Analisis --> Análisis de teleconsultas": {
        "No.": 126,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Analisis --> Análisis de reportes": {
        "No.": 127,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de encuesta de satisfacción y reportes": {
        "No.": 128,
        "RevRob": 0.5,
        "Notas_Rob": "Todavía no está lista."
    },
    "Proyecto consultorios --> Desarrollo": {
        "No.": 129,
        "RevRob": 0.5,
        "Notas_Rob": "En proceso"
    },
    "Desarrollo --> Implementación modulo de seguridad": {
        "No.": 130,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián."
    },
    "Desarrollo --> Implementacion de figuras tributarias": {
        "No.": 131,
        "RevRob": 0.5,
        "Notas_Rob": "Se revisó con Adrián pero no estamos seguros."
    },
    "Desarrollo --> Implementación de especialidades": {
        "No.": 132,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián."
    },
    "Desarrollo --> Implementación catalogos varios define paciente": {
        "No.": 133,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián."
    },
    "Desarrollo --> Implementación de lista de precios": {
        "No.": 134,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián."
    },
    "Desarrollo --> Implementación de Nemóticos": {
        "No.": 135,
        "RevRob": 0.5,
        "Notas_Rob": "Se revisó con Adrían pero no estamos seguros."
    },
    "Desarrollo --> Implementación de tipos de servicios": {
        "No.": 136,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián."
    },
    "Desarrollo --> Implementación de servicios": {
        "No.": 137,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián."
    },
    "Desarrollo --> Implementación de Medicamentos e insumos": {
        "No.": 138,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián; insumos están con medicamentos."
    },
    "Desarrollo --> Implementación de proveedor": {
        "No.": 139,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián."
    },
    "Desarrollo --> Implementación de tipo de recurrencia": {
        "No.": 140,
        "RevRob": 0.5,
        "Notas_Rob": "Se revisó con Adrián; pero no nos acordamos."
    },
    "Desarrollo --> Implementación de catalogos de doctores": {
        "No.": 141,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián."
    },
    "Desarrollo --> Implementación de instituciones de referencia": {
        "No.": 142,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián."
    },
    "Desarrollo --> Implementación de pacientes": {
        "No.": 143,
        "RevRob": 0.5,
        "Notas_Rob": "\
- [ ] Tengo dudas acerca del funcionamiento del botón de pacientes.\
"
    },
    "Desarrollo --> Implementación de consultorios": {
        "No.": 144,
        "RevRob": 0.5,
        "Notas_Rob": "Se revisó con Adrián. Lista en detalles de la cita. Al parecer no es relevante. Se omitió al parecer."
    },
    "Desarrollo --> Apertura de horarios": {
        "No.": 145,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián."
    },
    "Desarrollo --> Creación de horarios": {
        "No.": 146,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián."
    },
    "Desarrollo --> Implementación de agenda": {
        "No.": 147,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián."
    },
    "Implementación de agenda --> Búsqueda de pacientes": {
        "No.": 148,
        "RevRob": 1.0,
        "Notas_Rob": "\
- [X] La búsqueda de pacientes se puede hacer correctamente.\
        "
    },
    "Implementación de agenda --> Detalle de pacientes": {
        "No.": 149,
        "RevRob": 1.0,
        "Notas_Rob": "\
- [X] Los detalles del paciente se ven bien.\
        "
    },
    "Implementación de agenda --> 3 doctores por tipo de agenda": {
        "No.": 150,
        "RevRob": 0.5,
        "Notas_Rob": "Lo están viendo ahorita."
    },
    "3 doctores por tipo de agenda --> Diaria": {
        "No.": 151,
        "RevRob": 0.5,
        "Notas_Rob": "En desarrollo."
    },
    "3 doctores por tipo de agenda --> Semanal": {
        "No.": 152,
        "RevRob": 0.5,
        "Notas_Rob": "En desarrollo."
    },
    "3 doctores por tipo de agenda --> Mensual": {
        "No.": 153,
        "RevRob": 0.5,
        "Notas_Rob": "En desarrollo."
    },
    "Implementación de agenda --> Botones": {
        "No.": 154,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrian."
    },
    "Botones --> Refrescar": {
        "No.": 155,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrian."
    },
    "Botones --> Lista de pacientes por atender": {
        "No.": 156,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrian."
    },
    "Botones --> Lista de médicos registrados.": {
        "No.": 157,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Botones --> Impresión": {
        "No.": 158,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Implementación de agenda --> Asignación de citas": {
        "No.": 159,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Asignación de citas --> Selección del Dr.": {
        "No.": 160,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Asignación de citas --> Selección del día de consulta de disponibilidad": {
        "No.": 161,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Asignación de citas --> Mostrar disponibilidad y seleccionar un horario": {
        "No.": 162,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Asignación de citas --> Actualizar la agenda y Google Calendar": {
        "No.": 163,
        "RevRob": 0.5,
        "Notas_Rob": "\
- [ ] Revisión con Adrián pero todavía faltan notificaciones a cliente.\
- [X] El google calendar del doctor sí se actualizó.\
        "
    },
    "Asignación de citas --> Ingresar datos del paciente": {
        "No.": 164,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Implementación de agenda --> Alta de un nuevo paciente": {
        "No.": 165,
        "RevRob": 0.5,
        "Notas_Rob": "\
- [ ] Se vio un pequeño error cuando, en detalles de cita, se crea un nuevo paciente, después se selecciona un almacenado (al que le quieres agendar), el sistema guarda el pasado.\
        "
    },
    "Desarrollo --> Implementación servicio ambulatorio": {
        "No.": 166,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián."
    },
    "Desarrollo --> Implementación de notas médicas": {
        "No.": 167,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián."
    },
    "Implementación de notas médicas --> Nueva nota": {
        "No.": 168,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Implementación de notas médicas --> Problemas activos": {
        "No.": 169,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Implementación de notas médicas --> Historial médico": {
        "No.": 170,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Implementación de notas médicas --> Historial quirúrgico": {
        "No.": 171,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Implementación de notas médicas --> Historial psiquiátrico": {
        "No.": 172,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Implementación de notas médicas --> Historial Gineco-Obstétrico": {
        "No.": 173,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Implementación de notas médicas --> Medicamentos activos": {
        "No.": 174,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Implementación de notas médicas --> Alergias e intolerancias": {
        "No.": 175,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Implementación de notas médicas --> Hábitos sociales": {
        "No.": 176,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Implementación de notas médicas --> Alertas y necesidades especiales": {
        "No.": 177,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Implementación de notas médicas --> Inmunizaciones": {
        "No.": 178,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Implementación de notas médicas --> Antecedentes familiares": {
        "No.": 179,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Implementación de notas médicas --> Comentarios de Historia Clínica (para todos)": {
        "No.": 180,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrian. Parece que estas no serán de mucha utilidad según el Dr. Said."
    },
    "Comentarios de Historia Clínica (para todos) --> Historial médico": {
        "No.": 181,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Comentarios de Historia Clínica (para todos) --> Historial quirúrgico": {
        "No.": 182,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Comentarios de Historia Clínica (para todos) --> Historial psiquiátrico": {
        "No.": 183,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Comentarios de Historia Clínica (para todos) --> Historial Gineco-Obstétrico": {
        "No.": 184,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Comentarios de Historia Clínica (para todos) --> Medicamentos activos": {
        "No.": 185,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Comentarios de Historia Clínica (para todos) --> Alergias e intolerancias": {
        "No.": 186,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Comentarios de Historia Clínica (para todos) --> Hábitos sociales": {
        "No.": 187,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Comentarios de Historia Clínica (para todos) --> Alertas y necesidades especiales": {
        "No.": 188,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Comentarios de Historia Clínica (para todos) --> Inmunizaciones": {
        "No.": 189,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Comentarios de Historia Clínica (para todos) --> Antecedentes familiares": {
        "No.": 190,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Desarrollo --> Implementación de notas clinicas": {
        "No.": 191,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Implementación de notas clinicas --> Notas de evolución": {
        "No.": 192,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Notas de evolución --> Motivo de consulta": {
        "No.": 193,
        "RevRob": 0.5,
        "Notas_Rob": "Se revisó pero está fallando ahorita."
    },
    "Notas de evolución --> Signos vitales": {
        "No.": 194,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrian."
    },
    "Notas de evolución --> Exploración": {
        "No.": 195,
        "RevRob": 0.5,
        "Notas_Rob": "Se revisó pero está fallando ahorita."
    },
    "Notas de evolución --> Notas manuscritas": {
        "No.": 196,
        "RevRob": 0.5,
        "Notas_Rob": "Se revisó pero está fallando ahorita."
    },
    "Notas de evolución --> Laboratorio": {
        "No.": 197,
        "RevRob": 0.5,
        "Notas_Rob": "Se revisó pero está fallando ahorita."
    },
    "Notas de evolución --> Imágenes": {
        "No.": 198,
        "RevRob": 0.5,
        "Notas_Rob": "Se revisó pero está fallando ahorita."
    },
    "Notas de evolución --> Otras notas e intervenciones": {
        "No.": 199,
        "RevRob": 0.5,
        "Notas_Rob": "Se revisó pero está fallando ahorita."
    },
    "Notas de evolución --> Evaluación": {
        "No.": 200,
        "RevRob": 0.5,
        "Notas_Rob": "Se revisó pero está fallando ahorita."
    },
    "Evaluación --> Problemas activos": {
        "No.": 201,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Notas de evolución --> Receta": {
        "No.": 202,
        "RevRob": 0.5,
        "Notas_Rob": "Se revisó pero está fallando ahorita."
    },
    "Notas de evolución --> Solicitud de examen": {
        "No.": 203,
        "RevRob": 0.5,
        "Notas_Rob": "Se revisó pero está fallando ahorita."
    },
    "Notas de evolución --> Seguimiento y plan": {
        "No.": 204,
        "RevRob": 0.5,
        "Notas_Rob": "Se revisó pero está fallando ahorita."
    },
    "Notas de evolución --> Comunicaciones": {
        "No.": 205,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Comunicaciones --> Recordatorio": {
        "No.": 206,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Comunicaciones --> Mensaje": {
        "No.": 207,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Comunicaciones --> Tarea": {
        "No.": 208,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Comunicaciones --> Buzón de comunicaciones": {
        "No.": 209,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Notas de evolución --> Cargos": {
        "No.": 210,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Desarrollo --> Implementación de expedientes de documentos": {
        "No.": 211,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Implementación de expedientes de documentos --> Capturar el archivo que contiene el docto": {
        "No.": 212,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrian."
    },
    "Implementación de expedientes de documentos --> Vista y consulta en:": {
        "No.": 213,
        "RevRob": 0.5,
        "Notas_Rob": "No estamos seguros cual es."
    },
    "Vista y consulta en: --> Repositorio": {
        "No.": 214,
        "RevRob": 0.5,
        "Notas_Rob": "No estamos seguros cual es."
    },
    "Vista y consulta en: --> Historia clínica": {
        "No.": 215,
        "RevRob": 0.5,
        "Notas_Rob": "No estamos seguros cual es."
    },
    "Desarrollo --> Implementación de politicas de descuento": {
        "No.": 216,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Desarrollo --> Implementación de orden de servicio": {
        "No.": 217,
        "RevRob": 1.0,
        "Notas_Rob": "Esta actividad no se consideró necesaria."
    },
    "Desarrollo --> Implementación de generación de venta": {
        "No.": 218,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Desarrollo --> Implementación de facturación": {
        "No.": 219,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de facturación --> Diseño de la factura": {
        "No.": 220,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de facturación --> Creación de los catálogos del SAT": {
        "No.": 221,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de facturación --> Prueba de comunicaciones con proveedor": {
        "No.": 222,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de facturación --> Armado de la cadena a timbrar": {
        "No.": 223,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de facturación --> Interpretación de la cadena recibida del timbrado": {
        "No.": 224,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de facturación --> Prueba de timbrado": {
        "No.": 225,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de facturación --> Creación de las estructuras del PDF y XML": {
        "No.": 226,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de facturación --> Pruebas de redondeo": {
        "No.": 227,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de facturación --> Pruebas de factura global": {
        "No.": 228,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Pruebas de factura global --> Con descuentos": {
        "No.": 229,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Pruebas de factura global --> Sin descuentos": {
        "No.": 230,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de notas clinicas --> Cancelación de facturas": {
        "No.": 231,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de notas clinicas --> Facturación por grupo de servicio": {
        "No.": 232,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de notas clinicas --> Restitución y envío de facturas por mail": {
        "No.": 233,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación de cuentas por cobrar": {
        "No.": 234,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación de turnos": {
        "No.": 235,
        "RevRob": 1.0,
        "Notas_Rob": "Actualmente se tiene implementado 1 solo turno, el del todo el día."
    },
    "Desarrollo --> Implementación de cajeros": {
        "No.": 236,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Desarrollo --> Implementación de Cajas": {
        "No.": 237,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Implementación de Cajas --> Definición": {
        "No.": 238,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Implementación de Cajas --> Apertura": {
        "No.": 239,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Implementación de Cajas --> Asignación": {
        "No.": 240,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián"
    },
    "Implementación de Cajas --> Movimientos de cobro": {
        "No.": 241,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de Cajas --> Retiros de efectivo": {
        "No.": 242,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de Cajas --> Corte de caja": {
        "No.": 243,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación de cotizaciones": {
        "No.": 244,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián."
    },
    "Implementación de cotizaciones --> Lista de precios": {
        "No.": 245,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián."
    },
    "Implementación de cotizaciones --> Cotizaciones": {
        "No.": 246,
        "RevRob": 1.0,
        "Notas_Rob": "Se revisó con Adrián."
    },
    "Implementación de cotizaciones --> Creación de paquetes": {
        "No.": 247,
        "RevRob": 0.5,
        "Notas_Rob": "Creo que habíamos visto temas con los paquetes."
    },
    "Desarrollo --> Implementacion de teleconsultas": {
        "No.": 248,
        "RevRob": 0.5,
        "Notas_Rob": "Habíamos sugerido unas mejoras menores (que el médico pudiera ir anotando cosas)."
    },
    "Desarrollo --> Implementación de reportes": {
        "No.": 249,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de reportes --> Productividad": {
        "No.": 250,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de reportes --> Pagos": {
        "No.": 251,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de reportes --> Auditoria": {
        "No.": 252,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de reportes --> Ingresos": {
        "No.": 253,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Integración de encuentas de satisfacción": {
        "No.": 254,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Integracion de modulos": {
        "No.": 255,
        "RevRob": 0.5,
        "Notas_Rob": "En proceso."
    },
    "Proyecto consultorios --> Pruebas": {
        "No.": 256,
        "RevRob": 0.5,
        "Notas_Rob": "En proceso."
    },
    "Pruebas --> Generación de casos de uso y pruebas unitarias": {
        "No.": 257,
        "RevRob": 0.5,
        "Notas_Rob": "En proceso."
    },
    "Pruebas --> Revisión interna": {
        "No.": 258,
        "RevRob": 0.5,
        "Notas_Rob": "En proceso."
    },
    "Pruebas --> Integración y despliegue": {
        "No.": 259,
        "RevRob": 0.5,
        "Notas_Rob": "En proceso."
    },
    "Pruebas --> Pruebas Integrales": {
        "No.": 260,
        "RevRob": 0.5,
        "Notas_Rob": "En proceso."
    },
    "Pruebas --> Matriz de pruebas": {
        "No.": 261,
        "RevRob": 0.5,
        "Notas_Rob": "En proceso."
    },
    "Pruebas --> Ajustes": {
        "No.": 262,
        "RevRob": 0.5,
        "Notas_Rob": "En proceso."
    },
    "Pruebas --> Hoja de Implementación": {
        "No.": 263,
        "RevRob": 0.5,
        "Notas_Rob": "En proceso."
    },
    "Proyecto consultorios --> Liberación": {
        "No.": 264,
        "RevRob": 0.5,
        "Notas_Rob": "En proceso."
    },
    "Liberación --> Generar solicitud de migración": {
        "No.": 265,
        "RevRob": 0.5,
        "Notas_Rob": "En proceso."
    },
    "Liberación --> Liberación": {
        "No.": 266,
        "RevRob": 0.5,
        "Notas_Rob": "En proceso."
    },
    "Liberación --> Validación productiva": {
        "No.": 267,
        "RevRob": 0.5,
        "Notas_Rob": "En proceso."
    },
    "Proyecto consultorios --> Fin": {
        "No.": 268,
        "RevRob": 0.5,
        "Notas_Rob": "En proceso."
    }
}
