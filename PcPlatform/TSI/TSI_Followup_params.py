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



## List of followup activities
followup_dev_activities = {
    "Seed --> Proyecto consultorios": {
        "No.": 1,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Proyecto consultorios --> Inicio": {
        "No.": 2,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Proyecto consultorios --> Diseño pantallas": {
        "No.": 3,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Diseño pantallas --> Personalización menú superior": {
        "No.": 4,
        "RevRob": 1.0,
        "Notas_Rob": "El menú contiene el logo de Punto Clínico, los colores correctos y las entradas adecuadas."
    },
    "Diseño pantallas --> Diseño de lateral izquierdo-buscador": {
        "No.": 5,
        "RevRob": 1.0,
        "Notas_Rob": "El buscador permite buscar las entradas correctas. Se puede buscar por nombre, teléfono y demás."
    },
    "Diseño pantallas --> Calendario de vista por mes con colores con acciones": {
        "No.": 6,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Diseño pantallas --> Calendario de vista por día": {
        "No.": 7,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Diseño pantallas --> Lista de pacientes": {
        "No.": 8,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Diseño pantallas --> Lista de Médicos": {
        "No.": 9,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Diseño pantallas --> Criterios de impresión": {
        "No.": 10,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Diseño pantallas --> Calendario de vista por semana": {
        "No.": 11,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Diseño pantallas --> Alta rapida de pacientes-buscador": {
        "No.": 12,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Diseño pantallas --> Busqueda avanzada, filtros de citas": {
        "No.": 13,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Diseño pantallas --> Detalles de citas:Alta, Consulta, Actualización": {
        "No.": 14,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Diseño pantallas --> Expediente clinico paciente": {
        "No.": 15,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Expediente clinico paciente --> Encabezado expediente clinico": {
        "No.": 16,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Expediente clinico paciente --> Lateral expediente clinico(iconos)": {
        "No.": 17,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Expediente clinico paciente --> Pantalla Datos demograficos": {
        "No.": 18,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Expediente clinico paciente --> Pantalla Contactos": {
        "No.": 19,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Expediente clinico paciente --> Pantalla Profesional a cargo": {
        "No.": 20,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Expediente clinico paciente --> Pantalla Relaciones": {
        "No.": 21,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Expediente clinico paciente --> Agenda rapida de cita del paciente": {
        "No.": 22,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Expediente clinico paciente --> Pantalla lateral izquierda, Historial de citas": {
        "No.": 23,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Expediente clinico paciente --> Pantalla Cita-Detalle de consulta": {
        "No.": 24,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Expediente clinico paciente --> Pantalla Cita-Mensajeria": {
        "No.": 25,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Expediente clinico paciente --> Pantalla Cita-Tarea": {
        "No.": 26,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Expediente clinico paciente --> Pantalla Cita-Recordatorio": {
        "No.": 27,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Expediente clinico paciente --> Pantalla Cita-Comunicaciones": {
        "No.": 28,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Expediente clinico paciente --> Pantalla Cita-Cargos a paciente": {
        "No.": 29,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Expediente clinico paciente --> Pantalla de administrar documentos": {
        "No.": 30,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Expediente clinico paciente --> Pantalla de carga de documentos": {
        "No.": 31,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Diseño pantallas --> Historia clinica del paciente": {
        "No.": 32,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Historia clinica del paciente --> Encabezado de la historia clinica": {
        "No.": 33,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Diseño pantallas --> Sección de Resumen medico": {
        "No.": 34,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Sección de Resumen medico --> Pantalla de Historial medico": {
        "No.": 35,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Sección de Resumen medico --> Pantalla lateral izquierda, Antecedentes y diagnosticos": {
        "No.": 36,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Sección de Resumen medico --> Pantalla de Alergias e intolerancia": {
        "No.": 37,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Sección de Resumen medico --> Pantalla Habitos sociales": {
        "No.": 38,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Sección de Resumen medico --> Pantalla Alertas y necesidades especiales": {
        "No.": 39,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Sección de Resumen medico --> Pantalla antecedentes familiares": {
        "No.": 40,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Sección de Resumen medico --> Pantalla Inmunizaciones": {
        "No.": 41,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Sección de Resumen medico --> Pantalla Medicamentos activos": {
        "No.": 42,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Sección de Resumen medico --> Pantalla signos vitales": {
        "No.": 43,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Sección de Resumen medico --> Control de escala de dolor": {
        "No.": 44,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Sección de Resumen medico --> Pantalla de aprobacion de historia clinica": {
        "No.": 45,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Sección de Resumen medico --> Notas de Evolución": {
        "No.": 46,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Notas de Evolución --> Pantalla de motivo de consulta": {
        "No.": 47,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Notas de Evolución --> Pantalla de Principio, Evolución, Estado": {
        "No.": 48,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Notas de Evolución --> Pantalla de Exploración": {
        "No.": 49,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Notas de Evolución --> Pantalla de notas manuscritas (cámara)": {
        "No.": 50,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Notas de Evolución --> Pantalla de imágenes": {
        "No.": 51,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Notas de Evolución --> Pantalla de otras notas": {
        "No.": 52,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Sección de Resumen medico --> Evaluación": {
        "No.": 53,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Evaluación --> Pantalla de Antecedentes y diagnosticos": {
        "No.": 54,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Sección de Resumen medico --> Plan": {
        "No.": 55,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Plan --> Pantalla de recetas": {
        "No.": 56,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Plan --> Pantalla de solicitud de examen": {
        "No.": 57,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Plan --> Pantalla de solicitud de interconsulta": {
        "No.": 58,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Plan --> Pantalla de seguimiento y plan": {
        "No.": 59,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Plan --> Pantalla de comunicaciones-Nuevo recordatorio": {
        "No.": 60,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Plan --> Pantalla de comunicaciones-Nuevo mensaje": {
        "No.": 61,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Plan --> Pantalla nuevo cargo": {
        "No.": 62,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Sección de Resumen medico --> Comunicaciones": {
        "No.": 63,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Comunicaciones --> Pantalla bandeja comunicaciones": {
        "No.": 64,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Comunicaciones --> Pantalla Recordatorios": {
        "No.": 65,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Pantalla Recordatorios --> Pantalla de recordatorio": {
        "No.": 66,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Comunicaciones --> Pantalla de mensajes": {
        "No.": 67,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Pantalla de mensajes --> Pantalla Mensajes-Enviados": {
        "No.": 68,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Pantalla de mensajes --> Pantalla Mensajes-Borrador": {
        "No.": 69,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Pantalla de mensajes --> Pantalla Mensajes-Archivo": {
        "No.": 70,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Pantalla de mensajes --> Pantalla Mensajes-Basura": {
        "No.": 71,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Comunicaciones --> Pantalla Tareas": {
        "No.": 72,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Pantalla Tareas --> Pantalla Tareas-Enviados": {
        "No.": 73,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Pantalla Tareas --> Pantalla Tareas-Borrador": {
        "No.": 74,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Pantalla Tareas --> Pantalla Tareas-Archivo": {
        "No.": 75,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Pantalla Tareas --> Pantalla Tareas-Basura": {
        "No.": 76,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Comunicaciones --> Nuevas pantallas": {
        "No.": 77,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Nuevas pantallas --> Apertura de horarios": {
        "No.": 78,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Nuevas pantallas --> Creación de horarios": {
        "No.": 79,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Nuevas pantallas --> Resultados": {
        "No.": 80,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Nuevas pantallas --> Pantalla de comunicaciones - nueva tarea": {
        "No.": 81,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Nuevas pantallas --> Portafolios": {
        "No.": 82,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Proyecto consultorios --> Analisis": {
        "No.": 83,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de usuarios": {
        "No.": 84,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de roles seguridad": {
        "No.": 85,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de politicas de seguridad": {
        "No.": 86,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de sucursales": {
        "No.": 87,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de figuras tributarias": {
        "No.": 88,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de especialidades": {
        "No.": 89,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de pacientes": {
        "No.": 90,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de lista de precios": {
        "No.": 91,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de Nemóticos": {
        "No.": 92,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de tipos de servicios": {
        "No.": 93,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de Servicios": {
        "No.": 94,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de Medicamentos e insumos": {
        "No.": 95,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de proveedor": {
        "No.": 96,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de consultorios": {
        "No.": 97,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de tipo de recurrencia": {
        "No.": 98,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de agendas": {
        "No.": 99,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de Doctores": {
        "No.": 100,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de instituciones de referencia": {
        "No.": 101,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de Historia clinica": {
        "No.": 102,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de notas clinicas": {
        "No.": 103,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Análisis de notas clinicas --> Nueva nota": {
        "No.": 104,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Análisis de notas clinicas --> Problemas activos": {
        "No.": 105,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Análisis de notas clinicas --> Historial médico": {
        "No.": 106,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Análisis de notas clinicas --> Historial quirúrgico": {
        "No.": 107,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Análisis de notas clinicas --> Historial psiquiátrico": {
        "No.": 108,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Análisis de notas clinicas --> Historial Gineco-Obstétrico": {
        "No.": 109,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Análisis de notas clinicas --> Medicamentos activos": {
        "No.": 110,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Análisis de notas clinicas --> Alergias e intolerancias": {
        "No.": 111,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Análisis de notas clinicas --> Hábitos sociales": {
        "No.": 112,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Análisis de notas clinicas --> Alertas y necesidades especiales": {
        "No.": 113,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Análisis de notas clinicas --> Inmunizaciones": {
        "No.": 114,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Análisis de notas clinicas --> Antecedentes familiares": {
        "No.": 115,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de Expediente de documentos": {
        "No.": 116,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de politicas de descuentos": {
        "No.": 117,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de Orden de servicio": {
        "No.": 118,
        "RevRob": 0.0,
        "Notas_Rob": "-"
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
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de Cajas": {
        "No.": 123,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Analisis de cajeros": {
        "No.": 124,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Analisis de cotizaciones": {
        "No.": 125,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de teleconsultas": {
        "No.": 126,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de reportes": {
        "No.": 127,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Analisis --> Análisis de encuesta de satisfacción y reportes": {
        "No.": 128,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Proyecto consultorios --> Desarrollo": {
        "No.": 129,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación modulo de seguridad": {
        "No.": 130,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementacion de figuras tributarias": {
        "No.": 131,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación de especialidades": {
        "No.": 132,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación catalogos varios define paciente": {
        "No.": 133,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación de lista de precios": {
        "No.": 134,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación de Nemóticos": {
        "No.": 135,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación de tipos de servicios": {
        "No.": 136,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación de servicios": {
        "No.": 137,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación de Medicamentos e insumos": {
        "No.": 138,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación de proveedor": {
        "No.": 139,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación de tipo de recurrencia": {
        "No.": 140,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación de catalogos de doctores": {
        "No.": 141,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación de instituciones de referencia": {
        "No.": 142,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación de pacientes": {
        "No.": 143,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación de consultorios": {
        "No.": 144,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Apertura de horarios": {
        "No.": 145,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Creación de horarios": {
        "No.": 146,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación de agenda": {
        "No.": 147,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de agenda --> Búsqueda de pacientes": {
        "No.": 148,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de agenda --> Detalle de pacientes": {
        "No.": 149,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de agenda --> 3 doctores por tipo de agenda": {
        "No.": 150,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "3 doctores por tipo de agenda --> Diaria": {
        "No.": 151,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "3 doctores por tipo de agenda --> Semanal": {
        "No.": 152,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "3 doctores por tipo de agenda --> Mensual": {
        "No.": 153,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de agenda --> Botones": {
        "No.": 154,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Botones --> Refrescar": {
        "No.": 155,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Botones --> Lista de pacientes por atender": {
        "No.": 156,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Botones --> Lista de médicos registrados.": {
        "No.": 157,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Botones --> Impresión": {
        "No.": 158,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de agenda --> Asignación de citas": {
        "No.": 159,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Asignación de citas --> Selección del Dr.": {
        "No.": 160,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Asignación de citas --> Selección del día de consulta de disponibilidad": {
        "No.": 161,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Asignación de citas --> Mostrar disponibilidad y seleccionar un horario": {
        "No.": 162,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Asignación de citas --> Actualizar la agenda y Google Calendar": {
        "No.": 163,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Asignación de citas --> Ingresar datos del paciente": {
        "No.": 164,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de agenda --> Alta de un nuevo paciente": {
        "No.": 165,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación servicio ambulatorio": {
        "No.": 166,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación de notas médicas": {
        "No.": 167,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de notas médicas --> Nueva nota": {
        "No.": 168,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de notas médicas --> Problemas activos": {
        "No.": 169,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de notas médicas --> Historial médico": {
        "No.": 170,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de notas médicas --> Historial quirúrgico": {
        "No.": 171,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de notas médicas --> Historial psiquiátrico": {
        "No.": 172,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de notas médicas --> Historial Gineco-Obstétrico": {
        "No.": 173,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de notas médicas --> Medicamentos activos": {
        "No.": 174,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de notas médicas --> Alergias e intolerancias": {
        "No.": 175,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de notas médicas --> Hábitos sociales": {
        "No.": 176,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de notas médicas --> Alertas y necesidades especiales": {
        "No.": 177,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de notas médicas --> Inmunizaciones": {
        "No.": 178,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de notas médicas --> Antecedentes familiares": {
        "No.": 179,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de notas médicas --> Comentarios de Historia Clínica (para todos)": {
        "No.": 180,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Comentarios de Historia Clínica (para todos) --> Historial médico": {
        "No.": 181,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Comentarios de Historia Clínica (para todos) --> Historial quirúrgico": {
        "No.": 182,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Comentarios de Historia Clínica (para todos) --> Historial psiquiátrico": {
        "No.": 183,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Comentarios de Historia Clínica (para todos) --> Historial Gineco-Obstétrico": {
        "No.": 184,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Comentarios de Historia Clínica (para todos) --> Medicamentos activos": {
        "No.": 185,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Comentarios de Historia Clínica (para todos) --> Alergias e intolerancias": {
        "No.": 186,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Comentarios de Historia Clínica (para todos) --> Hábitos sociales": {
        "No.": 187,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Comentarios de Historia Clínica (para todos) --> Alertas y necesidades especiales": {
        "No.": 188,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Comentarios de Historia Clínica (para todos) --> Inmunizaciones": {
        "No.": 189,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Comentarios de Historia Clínica (para todos) --> Antecedentes familiares": {
        "No.": 190,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación de notas clinicas": {
        "No.": 191,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de notas clinicas --> Notas de evolución": {
        "No.": 192,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Notas de evolución --> Motivo de consulta": {
        "No.": 193,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Notas de evolución --> Signos vitales": {
        "No.": 194,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Notas de evolución --> Exploración": {
        "No.": 195,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Notas de evolución --> Notas manuscritas": {
        "No.": 196,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Notas de evolución --> Laboratorio": {
        "No.": 197,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Notas de evolución --> Imágenes": {
        "No.": 198,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Notas de evolución --> Otras notas e intervenciones": {
        "No.": 199,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Notas de evolución --> Evaluación": {
        "No.": 200,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Evaluación --> Problemas activos": {
        "No.": 201,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Notas de evolución --> Receta": {
        "No.": 202,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Notas de evolución --> Solicitud de examen": {
        "No.": 203,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Notas de evolución --> Seguimiento y plan": {
        "No.": 204,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Notas de evolución --> Comunicaciones": {
        "No.": 205,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Comunicaciones --> Recordatorio": {
        "No.": 206,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Comunicaciones --> Mensaje": {
        "No.": 207,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Comunicaciones --> Tarea": {
        "No.": 208,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Comunicaciones --> Buzón de comunicaciones": {
        "No.": 209,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Notas de evolución --> Cargos": {
        "No.": 210,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación de expedientes de documentos": {
        "No.": 211,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de expedientes de documentos --> Capturar el archivo que contiene el docto": {
        "No.": 212,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de expedientes de documentos --> Vista y consulta en:": {
        "No.": 213,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Vista y consulta en: --> Repositorio": {
        "No.": 214,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Vista y consulta en: --> Historia clínica": {
        "No.": 215,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación de politicas de descuento": {
        "No.": 216,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación de orden de servicio": {
        "No.": 217,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación de generación de venta": {
        "No.": 218,
        "RevRob": 0.0,
        "Notas_Rob": "-"
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
    "Implementación de notas clinicas --> Restitución y envío de facturas por mail": {
        "No.": 232,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación de cuentas por cobrar": {
        "No.": 233,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación de turnos": {
        "No.": 234,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación de cajeros": {
        "No.": 235,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación de Cajas": {
        "No.": 236,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de Cajas --> Definición": {
        "No.": 237,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de Cajas --> Apertura": {
        "No.": 238,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de Cajas --> Asignación": {
        "No.": 239,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de Cajas --> Movimientos de cobro": {
        "No.": 240,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de Cajas --> Retiros de efectivo": {
        "No.": 241,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de Cajas --> Corte de caja": {
        "No.": 242,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación de cotizaciones": {
        "No.": 243,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de cotizaciones --> Lista de precios": {
        "No.": 244,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de cotizaciones --> Cotizaciones": {
        "No.": 245,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Implementación de cotizaciones --> Creación de paquetes": {
        "No.": 246,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementacion de teleconsultas": {
        "No.": 247,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Implementación de reportes": {
        "No.": 248,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Integración de encuentas de satisfacción": {
        "No.": 249,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Desarrollo --> Integracion de modulos": {
        "No.": 250,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Proyecto consultorios --> Pruebas": {
        "No.": 251,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Pruebas --> Generación de casos de uso y pruebas unitarias": {
        "No.": 252,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Pruebas --> Revisión interna": {
        "No.": 253,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Pruebas --> Integración y despliegue": {
        "No.": 254,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Pruebas --> Pruebas Integrales": {
        "No.": 255,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Pruebas --> Matriz de pruebas": {
        "No.": 256,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Pruebas --> Ajustes": {
        "No.": 257,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Pruebas --> Hoja de Implementación": {
        "No.": 258,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Proyecto consultorios --> Liberación": {
        "No.": 259,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Liberación --> Generar solicitud de migración": {
        "No.": 260,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Liberación --> Liberación": {
        "No.": 261,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Liberación --> Validación productiva": {
        "No.": 262,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    },
    "Proyecto consultorios --> Fin": {
        "No.": 263,
        "RevRob": 0.0,
        "Notas_Rob": "-"
    }
}
